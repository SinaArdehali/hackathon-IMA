import io
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/home/malphonsus/projects/hackathon-ima/back/hackathon-ima-2019-751c334d5318.json"

# Imports the Google Cloud client library
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types
# Instantiates a client
client = speech.SpeechClient()



print("client instanciated")
# The name of the audio file to transcribe
file_name = "/home/malphonsus/projects/hackathon-ima/back/output.flac"


# Loads the audio into memory
with io.open(file_name, 'rb') as audio_file:
    content = audio_file.read()

print('audio loaded')
stream = [content]
requests = (types.StreamingRecognizeRequest(audio_content=chunk)
                for chunk in stream)

config = types.RecognitionConfig(
    encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code='fr-FR')

    # audio_channel_count=2,
    # enable_separate_recognition_per_channel=False,
    # language_code='fr-FR')

print("sent")
# Detects speech in the audio file
streaming_config = types.StreamingRecognitionConfig(config=config)

# streaming_recognize returns a generator.
responses = client.streaming_recognize(streaming_config, requests)

print('back')
for response in responses:
    # Once the transcription has settled, the first result will contain the
    # is_final result. The other results will be for subsequent portions of
    # the audio.
    for result in response.results:
        print('Finished: {}'.format(result.is_final))
        print('Stability: {}'.format(result.stability))
        alternatives = result.alternatives
        # The alternatives are ordered from most likely to least.
        for alternative in alternatives:
            print('Confidence: {}'.format(alternative.confidence))
            print(u'Transcript: {}'.format(alternative.transcript))