# Guide MCD / MLD

## Rappels
- une **entité** devient en général une **table** ;
- l'identifiant devient une **clé primaire** ;
- une association **1,N** se traduit par une clé étrangère du côté N ;
- une association **N,N** se traduit par une table d'association ;
- une association réflexive se traite comme une association entre deux occurrences de la même table.

À la fin de ce rappel, consulter également le document suivant :
- [Règles de passage du MCD au MLD (PDF)](../resources/Regles_de_passage_du_MCD_au_MLD.pdf)

Vous pouvez aussi utiliser Looping pour dessiner le MCD et préparer le passage au MLD :
- [Guide d'utilisation de Looping](LOOPING.md)

## Cas du sujet
- `Client` → `Commande` : un client passe plusieurs commandes ;
- `Commande` ↔ `Produit` via `Contient` : association N,N ;
- `Produit` ↔ `Fournisseur` via `Livre` : association N,N ;
- `Client` ↔ `Client` via `Recommande` : association réflexive ;
- `Commande` → `Facture` : `(0,1)` côté commande et `(1,1)` côté facture.
