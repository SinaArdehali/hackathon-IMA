
reponse_garage_prix_direct = """Vous pouvez proposer :
    - Un garage agrée avec la réduction assureur pour la réparation
    - Un garage constructeur avec la réduction assureur pour la réparation
    """

reponse_garage_prix_indirect = """Vous pouvez proposer :
    - Un garage agrée avec la réduction assureur pour l'entretien
    - Un garage constructeur avec la réduction assureur pour l'entretien
    """

reponse_evenement_prix_direct = """Vous pouvez proposer :
    - Une location d'un véhicule pour finir le trajet
    """

reponse_evenement_prix_indirect = """Vous pouvez proposer :
    - Une assurance exceptionnelle pour les déplacements importants
    - Un service de location de véhicule partenaire pour des trajets importants
    """



def update_profile(label, profil):
    if label == 'PANNE_M':
        reponse_direct = ""
        reponse_indirect = ""
        profil.update({"PANNE" : "PANNE_M"})
        return reponse_direct, reponse_indirect, profil
    elif label == "PRIX_BAS":
        reponse_direct = ""
        reponse_indirect = ""
        if "GARAGE" in profil.keys():
            if "GARAGE_AUTRES" == profil.get('GARAGE'):
                reponse_direct = reponse_garage_prix_direct
                reponse_indirect = reponse_garage_prix_indirect
        profil.update({"PRIX" : "PRIX_BAS"})
        return reponse_direct, reponse_indirect, profil
    elif label == "GARAGE_AUTRES":
        reponse_direct = ""
        reponse_indirect = ""
        profil.update({"GARAGE" : "GARAGE_AUTRES"})
        return reponse_direct, reponse_indirect, profil
    elif label == "EVENEMENT_RARE":
        reponse_direct = ""
        reponse_indirect = ""
        if "PRIX" in profil.keys():
            if "PRIX_BAS" == profil.get('PRIX'):
                reponse_direct = reponse_evenement_prix_direct
                reponse_indirect = reponse_evenement_prix_indirect
        profil.update({"EVENEMENT" : "EVENEMENT_RARE"})
        return reponse_direct, reponse_indirect, profil
    elif label == "COMM_SMS":
        reponse_direct = ""
        reponse_indirect = ""
        profil.update({"COMM" : "COMM_SMS"})
        return reponse_direct, reponse_indirect, profil
    elif label == "FREQ_ELEVE":
        reponse_direct = ""
        reponse_indirect = ""
        profil.update({"FREQ" : "FREQ_ELEVE"})
        return reponse_direct, reponse_indirect, profil
    else:
        reponse_direct = ""
        reponse_indirect = ""
        return reponse_direct, reponse_indirect, profil


# for event in ["EVENEMENT_RARE",
# "PANNE_M",
# "EVENEMENT_RARE",
# "EVENEMENT_RARE",
# "PANNE_M",
# "PANNE_M",
# "GARAGE_AUTRES",
# "PRIX_BAS",
# "EVENEMENT_RARE",
# "COMM_SMS",
# "COMM_SMS",
# "FREQ_ELEVE",
# "COMM_SMS",
# "COMM_SMS",
# "COMM_SMS"]:
#     reponse_direct, reponse_indirect, profil = update_profile(event, profil)
#     print("event", event)
#     print("reponse_direct :" , reponse_direct)
#     print("reponse_indirect :" , reponse_indirect)
#     print("profil :" , profil)
#     print('\n\n\n\n\n')