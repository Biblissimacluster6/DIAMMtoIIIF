# DIAMMtoIIIF

## English documentation

The DIAMMtoIIIF project is carried out within the framework of the Biblissima+ Cluster 6, "The Challenges of Musical Heritage". DIAMMtoIIIF is a Python program that generates an IIIF (International Image Interoperability Framework) manifest from data extracted from the DIAMM (Digital Image Archive of Medieval Music) API and the BnF IIIF server.

### How DIAMMtoIIIF works

This code retrieves JSON data from a DIAMM API URL of the format https://www.diamm.ac.uk/sources/2387/?format=json. It uses the ManifestFactory (Prezy_iiif) module to generate and manipulate the IIIF manifest. The JSON data is processed by extracting specific information using regular expressions and the json module. Manipulations are performed on the extracted data, such as adding empty values for missing folios and handling composer duplicates. Information about each element of the manifest is added using loops and methods from the manifest factory.
The code is modular, and various DIAMM metadata can be added. In its current form, the program supports work titles, composers, genres, and their positions in the source. Finally, the generated manifest (JSON) is converted to a string and written to a text file.

### Getting started and prerequisites:

To use DIAMMtoIIIF, you need to specify the desired DIAMM source URL and the IIIF image URL of the source (up to the ARK identifier) in the code. The number of empty folios/pages (without music, according to the DIAMM inventory) should be provided so that the sequence of the IIIF manifest aligns with the different views.
Make sure to install the required modules and have a compatible version of Python to run this code. You can test it by executing it with the appropriate data to generate your own IIIF manifest.
The DIAMMtoIIIF program is currently experimental and requires a basic understanding of the Python programming language to be used. Due to its experimental nature, this software may be subject to bugs or limitations. These errors are often related to specificities of the DIAMM inventories, which may not always be standardized. The program may not be able to handle all of them.

### Library of musical IIIF manifests:

So far, the program has generated several manifests, available above, for musical manuscripts from the 12th century to the 15th century. Since the manifests do not yet have URIs, it is recommended to view them with MIRADOR.

## Documentation française

The DIAMMtoIIIF project is carried out within the framework of the Biblissima+ Cluster 6, "Challenges of Musical Heritage". DIAMMtoIIIF is a Python program that generates an IIIF (International Image Interoperability Framework) manifest from data extracted from the DIAMM (Digital Image Archive of Medieval Music) API and the BnF IIIF server.

### Fonctionnement de DIAMMtoIIIF

Ce code récupère des données JSON à partir d'une URL de l'API DIAMM du type https://www.diamm.ac.uk/sources/2387/?format=json. Il utilise les modules ManifestFactory (Prezy_iiif) pour générer et manipuler le manifeste IIIF.
Les données JSON sont traitées en extrayant des informations spécifiques à l'aide d'expressions régulières et du module json. Des manipulations sont effectuées sur les données extraites, comme l'ajout de valeurs vides pour les folios manquants et la gestion des doublons de compositeurs. 
Les informations sur chaque élément du manifeste sont ajoutées à l'aide de boucles et de méthodes de la fabrique de manifestes.
Le code est modulable et diverses metadonnées DIAMM peuvent être ajoutées. Dans sa forme actuelle, le programme prend en charge les titres des oeuvres, les compositeurs, les genres et leur position dans la source. 
Finalement, le manifeste généré (JSON) est converti en une chaîne de caractères et écrit dans un fichier texte.

### Prise en main et prérequis :

Afin d'utiliser DIAMMtoIIIF, il est nécessaire d'indiquer dans le code l'URL DIAMM de la source souhaitée ainsi que l'URL des images IIIF de la source (jusqu'à l'identifiant ARK) qu'il est possible de retrouver dans Gallica. Le nombre de folios/pages vides (sans musique, suivant l'inventaire DIAMM) doit être renseigné afin que la séquence du manifeste IIIF s'aligne avec les différentes vues.
Assurez-vous en outre d'installer les modules requis et d'avoir une version de Python compatible pour exécuter ce code. Vous pouvez le tester en l'exécutant avec les données appropriées pour générer votre propre manifeste IIIF.

Le programme DIAMMtoIIIF est pour l'heure encore expérimental et nécessite une compréhension de base du langage de programmation Python pour être utilisé. En raison de son caractère expérimental, ce logiciel peut être sujet à des bugs ou des limitations.
Souvent, ces erreurs sont liées à des particularités des inventaires DIAMM qui, parfois, s'avèrent non standardisés. Le programme ne peut pas tous les prendre en charge. 

### Bibliothèque de manifestes IIIF musicaux :

Jusqu'à maintenant, le programme a permis de générer plusieurs manifestes, disponibles ci-dessus, de manuscrits musicaux du XIIe siècle au XVe siècle. Dans la mesure où les manifestes ne disposent pas encore d'URI, il est conseillé de les visualiser avec MIRADOR. 
