import phonemizer.phonemize as g2p
import regex
import re

def clean_string(text):
    #remove chrone phonème appuyé
    text = re.sub("[ːˑ]", "", text)
    text = re.sub("[\-]", " ", text)
    text = re.sub("\\s+", " ", text)
    return text

phonem_consons = {
    "b": "3",
    "d": "2",
    "f": "1",
    "g": "7",
    "ɡ": "7",
    "k": "5",
    "l": "4",
    "m": "1",
    "n": "3",
    "ŋ": "8",
    "ɲ": "4",
    "p": "2",
    "ʁ": "6",
    "s": "6",
    "ʃ": "4",
    "t": "1",
    "v": "5",
    "z": "5",
    "ʒ": "2",
    "j": "8",
    "w": "4",
    "ɥ": "3"
}
phonem_voyels = {
    "a": "C",
    "ɑ": "C",
    "e": "G",
    "ɛ": "M",
    "ɛː": "M",
    "ə": "P",
    "i": "B",
    "œ": "C",
    "ø": "P",
    "o": "C",
    "ɔ": "M",
    "u": "M",
    "y": "G",
    "ɑ̃": "B",
    "ɛ̃": "P",
    "œ̃": "G",
    "ɔ̃": "B"
}

phonem_visem = {
    "b": "p",
    "d": "t",
    "f": "f",
    "g": "k",
    "ɡ": "k",
    "k": "k",
    "l": "t",
    "m": "p",
    "n": "t",
    "ŋ": "k",
    "ɲ": "J",
    "p": "p",
    "ʁ": "k",
    "s": "s",
    "ʃ": "S",
    "t": "t",
    "v": "f",
    "z": "s",
    "ʒ": "S",
    "j": "i",
    "w": "u",
    "ɥ": "u",
    "a": "a",
    "ɑ": "a",
    "e": "e",
    "ɛ": "E",
    "ɛː": "E",
    "ə": "@",
    "i": "i",
    "œ": "O",
    "ø": "o",
    "o": "o",
    "ɔ": "O",
    "u": "u",
    "y": "u",
    "ɑ̃": "a",
    "ɛ̃": "E",
    "œ̃": "O",
    "ɔ̃": "O"
}

text = "Maître Corbeau sur un arbre perché"
# text = "Il était une fois 3 petits cochons. Le jour arriva pour eux de quitter la maison de leur maman. "
# text = "Un meunier qui avait trois fils s'extasie de ses fistules anales, Jean-françois, enfants ping-pong"

def process(text):
    phonems = clean_string(g2p.phonemize(text, language='fr-fr', backend='espeak', language_switch='remove-utterance', njobs=4))
    output_array = []
    current_code = ""
    current_visem = []
    for phonem_word in phonems.split():
        for phonem in regex.findall('\X', phonem_word):
            if current_code == "":
                if phonem in phonem_consons:
                    current_code = phonem_consons[phonem]
                    current_visem = [phonem_visem[phonem]]
                else:
                    current_code = f"1{phonem_voyels[phonem]}"
                    current_visem = [phonem_visem[phonem]]
                    output_array.append((current_code, current_visem))
                    current_visem = []
                    current_code = ""
            else:
                if phonem in phonem_voyels:
                    current_code = f"{current_code}{phonem_voyels[phonem]}"
                    current_visem.append(phonem_visem[phonem])
                    output_array.append((current_code, current_visem))
                    current_visem = []
                    current_code = ""
                else:
                    current_code = f"{current_code}C"
                    output_array.append((current_code, current_visem))
                    current_visem = [phonem_visem[phonem]]
                    current_code = f"{phonem_consons[phonem]}"

    if current_code != "":
        current_code = f"{current_code}C"
        output_array.append((current_code, current_visem))
        current_visem = [phonem_visem[phonem]]
        current_code = f"{phonem_consons[phonem]}"
    return (output_array)



def code(text):
    try:
        return "-".join([key for key,_ in process(text)])
    except:
        print(text)
        return None
