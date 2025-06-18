# Contact Travel – Module Odoo

Ce module a été développé dans le cadre du test technique pour le poste de développeur junior Odoo chez Weasydoo.

## Objectif

Permettre la gestion des voyages associés à un contact (`res.partner`), avec :
- Un bouton intelligent affichant le nombre de voyages
- Une vue dédiée pour gérer les voyages
- Un calcul automatique du niveau de récompense du client

## Fonctionnalités

- ✅ Création d'un nouveau modèle `contact.travel.voyage` contenant :
  - Nom du voyage
  - Date de départ
  - Destination
  - Montant
  - Lien vers un contact
- ✅ Ajout d’un bouton intelligent dans la fiche contact affichant le nombre de voyages
- ✅ Ajout d’un champ calculé `reward_level` selon le total des montants des voyages :
  - **Argent** : > 0 DA
  - **Or** : ≥ 50 000 DA
  - **Platine** : ≥ 100 000 DA
- ✅ Ajout d’un onglet "Voyages" dans la fiche contact
- ✅ Sécurisation des accès via `ir.model.access.csv`

##  Structure du module

