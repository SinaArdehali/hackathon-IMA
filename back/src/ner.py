import back.src.model_data as md



nlp = md.space_loader()

with open("story_", "r") as f:
    story = f.read()


for text in story.replace("'", " ").split("- "):
    doc = nlp(text)
    for ent in doc.ents:
        # print(ent.label_)
        # print(ent.text)
        # print("*****")

        # if ent.label_ in ['FREQ_ELEVE']:
        #     print(ent.label_)
        #     print(ent.text)
        #     print("*****")

        if ent.label_ not in ['LOC', 'MISC', 'PER', 'ORG']:
            print(ent.label_)
            # print(ent.text)
            # print("*****")

