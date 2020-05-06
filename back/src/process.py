import pyphen
import phonemizer.phonemize as g2p
import re
import string

base_string = "Julien Lenne lait tape le CR d'une réunion d'avant vente complètement improvisée à l'arrache et une bande de couillon"
base_string = "Jean-François, stérile, s'exclame : les poules du couvent couvent les oeufs "
base_string = "boire madame femme grand bruit meilleur quatre malade maison astronome baigner parking pomme amoureux santé chat téléphone vrai soir raison aubergine deux neuf brun je table camembert marché neige sapin mille hôpital homme bon sous dur"
base_string = "bonjour adaptatif"
dic = pyphen.Pyphen(lang='fr_FR')


print(string.punctuation)
def clean_string(text):
    text = re.sub("[!\"#$%&\(\)\*\+,-\./:;<=>?@\[\\\]^_`{|}~]", " ", text)
    text = re.sub("\\s+", " ", text)
    return text


print(base_string.lower())
base_string = clean_string(base_string)
print(base_string)


print(g2p.phonemize(base_string, use_sampa=True))

syl = dic.inserted(base_string)
print(syl)
print(re.split("-|\s", syl))
