# Guide d'utilisation de Looping

## Présentation rapide
Looping est un logiciel de modélisation de données fréquemment utilisé dans l'enseignement pour créer des schémas Merise :
- MCD (Modèle Conceptuel de Données) ;
- MLD (Modèle Logique de Données) ;
- MPD selon les réglages choisis.

Dans ce CCF, Looping peut être utilisé pour :
- dessiner le MCD de l'application ;
- vérifier les cardinalités ;
- représenter les associations binaires, réflexives et éventuellement ternaires ;
- illustrer l'héritage / la généralisation-spécialisation ;
- préparer le passage du MCD au MLD.

## Installation
L'installation de Looping est facultative. Si vous ne l'utilisez pas, vous pouvez réaliser vos schémas avec tout autre outil accepté par votre enseignant.

Pour l'installation selon votre système, voir :
- [README](../../README.md) ;
- [Option 2 - Installation locale](../INSTALLATION-LOCALE.md).

## Prise en main
### 1. Créer un nouveau modèle
1. Ouvrir Looping.
2. Créer un nouveau projet.
3. Choisir un modèle orienté données / Merise selon la version installée.
4. Enregistrer immédiatement le fichier de travail.

### 2. Créer une entité
1. Ajouter une entité.
2. Donner un nom explicite à l'entité.
3. Ajouter les propriétés.
4. Identifier l'attribut identifiant.
5. Vérifier la cohérence du nommage.

Exemple dans le contexte BoutikPro :
- Client
- Commande
- Produit
- Fournisseur
- Facture
- Carte_fidelite

### 3. Créer une association
1. Ajouter une association entre deux entités.
2. Nommer clairement l'association.
3. Définir les cardinalités de chaque côté.
4. Ajouter si besoin des propriétés dans l'association.

Exemples :
- `Client` passe `Commande`
- `Commande` contient `Produit`
- `Produit` est livré par `Fournisseur`

### 4. Représenter une association réflexive
Une association réflexive relie une entité à elle-même.

Exemple :
- `Client` recommande `Client`

Dans Looping :
1. Créer l'entité `Client`.
2. Ajouter une association reliée deux fois à la même entité.
3. Donner un nom à l'association, par exemple `Recommande`.
4. Définir les cardinalités de chaque rôle.

### 5. Représenter un héritage
Selon la version de Looping, l'héritage peut être représenté avec une contrainte :
- pas de contrainte ;
- exclusivité ;
- totalité ;
- partition.

Dans le cadre d'un héritage :
1. Créer l'entité mère.
2. Créer les entités filles.
3. Ajouter le symbole d'héritage.
4. Choisir la contrainte adaptée.
5. Vérifier la cohérence métier.

### 6. Passer du MCD au MLD
Le passage du MCD au MLD se fait à partir des règles vues en cours :
- une entité devient une table ;
- l'identifiant devient clé primaire ;
- une association `1,N` devient en général une clé étrangère du côté `N` ;
- une association `N,N` devient une table d'association ;
- une association réflexive s'applique avec les mêmes règles générales ;
- selon le type d'héritage, plusieurs stratégies de traduction sont possibles.

Voir le rappel détaillé dans :
- [Guide MCD / MLD](MCD_MLD.md)
- [Règles de passage du MCD au MLD (PDF)](../resources/Regles_de_passage_du_MCD_au_MLD.pdf)

## Conseils de travail
- Nommer clairement les entités et associations.
- Vérifier les cardinalités avant de passer au MLD.
- Distinguer les attributs d'entité et les attributs d'association.
- Justifier vos choix lorsqu'il existe plusieurs traductions possibles.
- Exporter votre schéma en image ou PDF si votre enseignant le demande.

## Livrables possibles
Selon les consignes du CCF, vous pouvez fournir :
- un fichier source Looping ;
- une capture d'écran du MCD ;
- un export PDF ou image ;
- le MLD rédigé manuellement ou généré puis commenté.
