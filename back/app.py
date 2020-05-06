import io
import src.model_data as md
import src.model_reponse as mr

from flask import Flask, Blueprint, request, send_file
from flask_restplus import Resource, Api, fields, reqparse

from google.cloud import language, speech
from google.cloud.language import enums as enums_lang
from google.cloud.language import types as types_lang
from google.cloud.speech import enums as enums_speech
from google.cloud.speech import types as types_speech

import src.alpc.phonem_to_lpc as alpc

import spacy
from spacy.pipeline import EntityRuler

from PIL import Image
from io import BytesIO

# import pyaudio
# import audio_processing as audioRec

# FORMAT = pyaudio.paInt16
# CHANNELS = 2
# RATE = 44100
# CHUNK = 1024
# RECORD_SECONDS = 5

# audio1 = pyaudio.PyAudio()


nlp = md.space_loader()

client_lang = language.LanguageServiceClient()
client_speech = speech.SpeechClient()

app = Flask(__name__)
api = Api(app)

app.logger.info("ner model loaded")

@app.after_request
def add_headers(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    return response


sentiment_model = api.model('Sentiment', {
    'text': fields.String(required=True, description='Texte à analyser')
})
mood_model = api.model('Mood', {
    'text': fields.String(required=True, description='Texte à analyser')
})

@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

@api.route('/sentiment')
class Sentiment(Resource):
    @api.expect(sentiment_model)
    def post(self):
        text = api.payload['text']
        document = types_lang.Document(
            content=text,
            type=enums_lang.Document.Type.PLAIN_TEXT)
        sentiment = client_lang.analyze_sentiment(document=document).document_sentiment
        app.logger.info(sentiment)
        return {'text': text, 'sentiment': sentiment.score}


@api.route('/service_demo')
class ServiceDemo(Resource):
    def get(self):
        with open("/app/story_", "r") as f:
            story = f.read()
        textuser = story.replace("'", " ").split("- ")[1::2]
        text_ = story.replace("'", " ").split("- ")
        ents = []
        profil = dict()
        reponse_direct_list = list()
        reponse_indirect_list = list()
        sentiments  = []
        for text in textuser:
            document = types_lang.Document(
            content = text,
            type = enums_lang.Document.Type.PLAIN_TEXT)
            sentiments.append(client_lang.analyze_sentiment(document=document).document_sentiment.score)
            doc = nlp(text)
            ents.append([(ent.text, ent.start_char, ent.end_char, ent.label_) for ent in doc.ents])
            for ent in doc.ents:
                reponse_direct, reponse_indirect, profil = mr.update_profile(ent.label_, profil)
                reponse_direct_list.append(reponse_direct)
                reponse_indirect_list.append(reponse_indirect)
        return {
            "text" : text_,
            "ents" : ents,
            "sentiments" : sentiments,
            "reponse_direct" : reponse_direct_list,
            "reponse_indirect" : reponse_indirect_list,
            "profil" : profil}


@api.route('/stt')
class Stt(Resource):
    def post(self):
        file_name = "output.flac"
        with io.open(file_name, 'rb') as audio_file:
            content = audio_file.read()
            audio = types_speech.RecognitionAudio(content=content)
        config = types_speech.RecognitionConfig(
            audio_channel_count=2,
            enable_separate_recognition_per_channel=True,
            language_code='fr-FR')
        response = client_speech.recognize(config, audio)

        resp = {'results': []}
        for result in response.results:
            print('Transcript: {}'.format(result.alternatives[0].transcript))
            resp['results'].append(result.alternatives[0].transcript)

        return resp

@api.route('/user/<int:id>')
class User(Resource):
    def get(self, id):
        return {
            "id": 1,
            "name": "Taffi",
            "firstname": "Julie",
            "birthdate": "1990-03-21",
            "vehicle": {
                "id": 1,
                "client_id": 1,
                "brand": "Renault",
                "model": "Clio II"
            }
        }


alpc_model = api.model('ALPC', {
    'text': fields.String(required=True, description='Text to process')
})
@api.route('/alpc')
class Alpc(Resource):
    @api.expect(alpc_model)
    def post(self):
        text = request.get_json()['text']
        app.logger.debug(text)
        return alpc.process(text)

@api.route('/alpc/chatbot')
class AlpcChatbot(Resource):
    def post(self):
        app.logger.info(request.get_json())
        text = request.get_json()["queryResult"]["parameters"]["texttotranslate"]
        data = alpc.process(text)

        items = [{
            "simpleResponse": {
                "textToSpeech": f"Voici le résultat pour {text}"
            }
        }]

        codes = ",".join([code for code, _ in data])
        items.append({
            "basicCard": {
                "image": {
                    "url": f"https://swaggerui.ai-made-ez.com/alpc/gif?codes={codes}",
                    "accessibility_text": "Image contenant les positions de la main par rapport à la tête"
                }
            }
        })

        return {
            # "fulfillment_text": f"COPY THAT : {text}",
            # "fulfillment_messages" : messages
            "payload": {
                "google": {
                    "richResponse": {
                        "items": items
                    }
                }
            }
        }

head_pos = {
    "C": (-30, 980),
    "P": (150, 900),
    "B": (300, 1040),
    "M": (500, 1100),
    "G": (500, 1280)
}

@api.route('/alpc/<int:hand>/<string:head>')
@api.doc(params={"hand": "Hand Code", "head": "Head Code"})
class AlpcHandHead(Resource):
    def get(self, hand, head):
        background = Image.open('img/visages/pikachu.png')
        foreground = Image.open(f'img/mainsLPC/{hand}.png')
        foreground = foreground.resize((int(foreground.size[0]/1.5), int(foreground.size[1]/1.5)))

        background.paste(foreground, head_pos[head], foreground.convert('RGBA'))

        img_io = BytesIO()
        background = background.resize((int(background.size[0]/4), int(background.size[1]/4)))
        background.save(img_io, 'PNG', quality=100)
        img_io.seek(0)

        return send_file(img_io, mimetype='image/png')

gif_parser = reqparse.RequestParser()
gif_parser.add_argument(
    'codes',
    action='split',
    location='args',
    help='List of codes to translate'
)

@api.route('/alpc/gif')
class AlpcGif(Resource):
    @api.expect(gif_parser)
    def get(self):
        def gen_frame(im):
            alpha = im.getchannel('A')
            # Convert the image into P mode but only use 255 colors in the palette out of 256
            im = im.convert('RGB').convert('P', palette=Image.ADAPTIVE, colors=255)
            # Set all pixel values below 128 to 255 , and the rest to 0
            mask = Image.eval(alpha, lambda a: 255 if a <=128 else 0)
            # Paste the color of index 255 and use alpha as a mask
            im.paste(255, mask)
            # The transparency index is 255
            im.info['transparency'] = 255

            return im

        args = gif_parser.parse_args()
        img_io = BytesIO()
        background = Image.open('img/visages/pikachu.png')
        background = background.convert("RGBA")
        images = [
            gen_frame(background.resize((int(background.size[0]/4), int(background.size[1]/4))))
        ]

        for code in args['codes']:
            foreground = Image.open(f'img/mainsLPC/{code[0]}.png')
            foreground = foreground.convert("RGBA")
            foreground = foreground.resize((int(foreground.size[0]/1.5), int(foreground.size[1]/1.5)))
            background_tmp = background.copy().convert("RGBA")
            background_tmp.paste(foreground, head_pos[code[1]], foreground.convert('RGBA'))

            background_tmp = background_tmp.resize((int(background_tmp.size[0]/4), int(background_tmp.size[1]/4)))
            background_tmp = background_tmp.convert("RGBA")
            images.append(gen_frame(background_tmp))

        images[0].save(
            img_io,
            'GIF',
            save_all=True,
            append_images=images[1:],
            duration=1000,
            loop=0,
            quality=100,
            disposal=2
        )

        img_io.seek(0)
        return send_file(img_io, mimetype='image/gif')
