import spacy
from spacy.pipeline import EntityRuler

def space_loader():


    nlp=spacy.load('fr_core_news_md')

    ruler = EntityRuler(nlp, overwrite_ents=True)
    # pattern panne
    patterns_panne = [
        {"label": "panne_m".upper(), "pattern": "fumée"},
        {"label": "panne_m".upper(), "pattern": "vapeur"},
        {"label": "panne_r".upper(), "pattern": "pneu"},
        {"label": "panne_r".upper(), "pattern": "roue"},
        {"label": "panne_b".upper(), "pattern": "batterie"},
        {"label": "panne_b".upper(), "pattern": "alimentation"},
        {"label": "panne_m".upper(), "pattern": "moteur"},
        {"label": "phone".upper(), "pattern": [{"shape": "dddddddddd"}]}
    ]

    # pattern moyen de communication
    patterns_comm = [
        {"label": "comm_tel".upper(), "pattern": "portable"},
        {"label": "comm_tel".upper(), "pattern": "fixe"},
        {"label": "comm_tel".upper(), "pattern": "mobile"},
        {"label": "comm_sms".upper(), "pattern": "texto"},
        {"label": "comm_sms".upper(), "pattern": "message"},
        {"label": "comm_sms".upper(), "pattern": "sms"},
        {"label": "comm_mail".upper(), "pattern": [{"lower": "adresse"}, {"lower": "electronique"}]},
        {"label": "comm_mail".upper(), "pattern": [{"lower": "adresse"}, {"lower": "mail"}]},
        {"label": "comm_mail".upper(), "pattern": "mail"}
    ]

    # pattern frequence de communication
    patterns_frequence = [
        {"label": "freq_eleve".upper(), "pattern": [{"lower": "notifications"}, {"lower": "dès"}, {"lower": "qu"}, {"lower": "il"}, {"lower": "y"}, {"lower": "a"}]},
        {"label": "freq_eleve".upper(), "pattern": "souvent"},
        {"label": "freq_eleve".upper(), "pattern": "regulièrement"},
        {"label": "freq_eleve".upper(), "pattern": [{"lower": "à"}, {"lower": "intervalle"}, {"lower": "regulier"}]},
        {"label": "freq_moyenne".upper(), "pattern": [{"lower": "de"}, {"lower": "temps"}, {"lower": "en"}, {"lower": "temps"}]},
        {"label": "freq_moyenne".upper(), "pattern": "parfois"},
        {"label": "freq_moyenne".upper(), "pattern": [{"lower": "quelque"}, {"lower": "fois"}]},
        {"label": "freq_basse".upper(), "pattern": "peu"},
        {"label": "freq_basse".upper(), "pattern": "jamais"},
        {"label": "freq_basse".upper(), "pattern": "rarement"}
    ]

    # pattern type de garage
    patterns_garage = [
        {"label": "garage_agree".upper(), "pattern": "accepte"},
        {"label": "garage_agree".upper(), "pattern": "admis"},
        {"label": "garage_agree".upper(), "pattern": "approuve"},
        {"label": "garage_agree".upper(), "pattern": "associe"},
        {"label": "garage_partenaire".upper(), "pattern": "adherent"},
        {"label": "garage_partenaire".upper(), "pattern": "sponsor"},
        {"label": "garage_concessionaire".upper(), "pattern": "commerçant"},
        {"label": "garage_concessionaire".upper(), "pattern": "depositaire"},
        {"label": "garage_concessionaire".upper(), "pattern": "distributeur"},
        {"label": "garage_concessionaire".upper(), "pattern": "exploitant"},
        {"label": "garage_pas_de_garage".upper(), "pattern": "aucun"},
        {"label": "garage_autres".upper(), "pattern": "privé"},
        {"label": "garage_autres".upper(), "pattern": "personnalisé"},
        {"label": "garage_autres".upper(), "pattern": [{"lower": "pas"}, {"lower": "de"}, {"lower": "préférences"}]},
        {"label": "garage_autres".upper(), "pattern": [{"lower": "j"}, {"lower": "ai"}, {"lower": "déjà"}]}
    ]

    # pattern type de evenement
    patterns_evenement = [
        {"label": "evenement_rare".upper(), "pattern": "cérémonie"},
        {"label": "evenement_rare".upper(), "pattern": "anniversaire"},
        {"label": "evenement_rare".upper(), "pattern": [{"lower": "départ"}, {"lower": "de"}, {"lower": "vacances"}]},
        {"label": "evenement_rare".upper(), "pattern": [{"lower": "retour"}, {"lower": "de"}, {"lower": "vacances"}]},
        {"label": "evenement_rare".upper(), "pattern": "mariage"},
        {"label": "evenement_rare".upper(), "pattern": "fiançailles"},
        {"label": "evenement_rare".upper(), "pattern": "enterrement"},
        {"label": "evenement_rare".upper(), "pattern": "bapteme"},
        {"label": "evenement_rare".upper(), "pattern": "communion"},
        {"label": "evenement_rare".upper(), "pattern": [{"lower": "bar"}, {"lower": "mitzvah"}, {"lower": "vacances"}]}
    ]

    # pattern type de evenement
    patterns_prix = [
        {"label": "prix_bas".upper(), "pattern": [{"lower": "prix"}, {"lower": "bas"}]},
        {"label": "prix_bas".upper(), "pattern": [{"lower": "pas"}, {"lower": "cher"}]},
        {"label": "prix_bas".upper(), "pattern": [{"lower": "peu"}, {"lower": "cher"}]},
        {"label": "prix_bas".upper(), "pattern": "economique"},
        {"label": "prix_bas".upper(), "pattern": [{"lower": "bas"}, {"lower": "prix"}]},
        {"label": "prix_bas".upper(), "pattern": [{"lower": "moins"}, {"lower": "cher"}]},
        {"label": "prix_bas".upper(), "pattern": [{"lower": "moins"}, {"lower": "chère"}]},
        {"label": "prix_bas".upper(), "pattern": "modique"},
        {"label": "prix_bas".upper(), "pattern": [{"lower": "petit"}, {"lower": "prix"}]},
        {"label": "prix_bas".upper(), "pattern": [{"lower": "bon"}, {"lower": "prix"}]},
        {"label": "prix_bas".upper(), "pattern": [{"lower": "juste"}, {"lower": "prix"}]},
        {"label": "prix_bas".upper(), "pattern": "abordable"},
        {"label": "prix_bas".upper(), "pattern": [{"lower": "prix"}, {"lower": "léger"}]},
        {"label": "prix_bas".upper(), "pattern": [{"lower": "prix"}, {"lower": "doux"}]},
        {"label": "prix_moyen".upper(), "pattern": [{"lower": "prix"}, {"lower": "moyen"}]},
        {"label": "prix_moyen".upper(), "pattern": [{"lower": "prix"}, {"lower": "modéré"}]},
        {"label": "prix_moyen".upper(), "pattern": [{"lower": "prix"}, {"lower": "normal"}]},
        {"label": "prix_moyen".upper(), "pattern": [{"lower": "prix"}, {"lower": "marché"}]},
        {"label": "prix_moyen".upper(), "pattern": [{"lower": "prix"}, {"lower": "du"}, {"lower": "marché"}]},
        {"label": "prix_moyen".upper(), "pattern": [{"lower": "prix"}, {"lower": "classique"}]},
        {"label": "prix_eleve".upper(), "pattern": [{"lower": "prix"}, {"lower": "élevé"}]},
        {"label": "prix_eleve".upper(), "pattern": [{"lower": "de"}, {"lower": "qualité"}]},
        {"label": "prix_eleve".upper(), "pattern": [{"lower": "le"}, {"lower": "meilleur"}]},
        {"label": "prix_eleve".upper(), "pattern": "chere"},
        {"label": "prix_eleve".upper(), "pattern": "cher"},
        {"label": "prix_eleve".upper(), "pattern": "chic"},
        {"label": "prix_eleve".upper(), "pattern": "couteux"},
        {"label": "prix_eleve".upper(), "pattern": "luxe"},
        {"label": "prix_eleve".upper(), "pattern": "coté"}
    ]


    ruler.add_patterns(patterns_panne)
    ruler.add_patterns(patterns_comm)
    ruler.add_patterns(patterns_frequence)
    ruler.add_patterns(patterns_garage)
    ruler.add_patterns(patterns_evenement)
    ruler.add_patterns(patterns_prix)

    nlp.add_pipe(ruler)

    return nlp

