# DOCUMENTATION DES SCRIPTS

## LQ_scrap_script.py
Dans ce script on scrapp le site du journal 'Lacan Quotidien', chaque article est écrit dans un sous-dossier 'corpusLQ' en format txt. Le script parcourt le site dans l'ordre chronologique, récupère les pdfs (lorsque il s'agit de gros numéro), et sinon se contente d'en extraire le texte directement depuis le code HTML.

## extract_neologism.py
Ici on récupère une liste de néologismes candidats avec la technique de détéction des hapax. On parcourt le corpus dans un ordre chronologique puis on stock les candidats du jour dans un JSON.

## filter_glaff.py
Ici on revisite notre liste de néologismes potentiels en retirant tout les mots présents dans le GLAFF.

## filterlg.py
La liste finale de néologismes contenait des mots de langues étrangères car certains articles été écrits dans une autre langue que le français (anglais, italien, espagnol). Avec ce script nous supprimons tout les candidats non français.

## term_frequency.py
Ce script classe la liste final de néologismes en fonction de leur fréquence d'apparition dans le corpus entier, cela permet de mieux séléctionner les néologismes qui seront étudiés.

## stat_graphplot.py
Ce script à été modifié plusieurs fois et est changé à chaque nouvelle étude. Ici il est configurer pour faire des statistiques sur la distribution d'un groupe de néologismes dans le corpus.

