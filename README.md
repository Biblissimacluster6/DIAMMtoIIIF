# DIAMMtoIIIFv2

## English documentation

The DIAMMtoIIIF project is carried out within the framework of the Biblissima+ Cluster 6, "The Challenges of Musical Heritage". DIAMMtoIIIF is a Python program that generates an IIIF (International Image Interoperability Framework) manifest from data extracted from the DIAMM (Digital Image Archive of Medieval Music) API and from the IIIF server of various libraries (BnF, Bayerische Staatsbibliothek, etc.).

### How DIAMMtoIIIF works

This code retrieves JSON data from a DIAMM API URL of the format https://www.diamm.ac.uk/sources/2387/?format=json. It uses the ManifestFactory (Prezy_iiif) module to generate and manipulate the IIIF manifest. The JSON data is processed by extracting specific information using regular expressions and the json module. Manipulations are performed on the extracted data, such as adding empty values for missing folios and handling composer duplicates. Information about each element of the manifest is added using loops and methods from the manifest factory.
The code is modular, and various DIAMM metadata can be added. In its current form, the program supports work titles, composers, genres, and their positions in the source. Finally, the generated manifest (JSON) is converted to a string and written to a text file (mymusicmanifest.txt).

![code](https://github.com/Biblissimacluster6/DIAMMtoIIIF/blob/main/img/Cordiforme%203.jpg)

### Getting started and prerequisites:

In addition to Python 3, you need to install the iiif-prezi library.

DIAMMtoIIIFv2 now features command-line functionality:

-u: DIAMM inventory URL (JSON)
-i : Image URI Base
-v: Number of first empty folios

Here's a typical command example:

python DIAMMtoIIIFv2.py -u "https://www.diamm.ac.uk/sources/2387/?format=json" -i "https://gallica.bnf.fr/iiif/ark:/12148/btv1b525044884" -v 9

To use DIAMMtoIIIF, you need to specify the desired DIAMM source URL (-u) and the IIIF image URI base of the source. For the BnF, up to the ARK identifier. For the Bayerische S., up to the pagination numbers (_00001, _00002): https://api.digitale-sammlungen.de/iiif/image/v2/bsb00079147. Be sure to respect the URL form. The number of first empty folios/pages (-v) (without music according to the DIAMM inventory!) should be provided so that the sequence of the IIIF manifest aligns with the different views. Therefore, this notion is highly dependent on the DIAMM inventory used and cannot compensate for a possible lack of precision or potential errors. 

Make sure to install the required modules and have a compatible version of Python to run this code. You can test it by executing it with the appropriate data to generate your own IIIF manifest.
The DIAMMtoIIIF program is currently experimental and requires a basic understanding of the Python programming language to be used. Due to its experimental nature, this software may be subject to bugs or limitations. These errors are often related to specificities of the DIAMM inventories, which may not always be standardized.

![code](https://github.com/Biblissimacluster6/DIAMMtoIIIF/blob/main/img/Chansonnier%20Lorraine.png)

### Library of musical IIIF manifests:

So far, the program has generated several manifests, available above, for musical manuscripts from the 12th century to the 15th century. Since the manifests do not yet have URIs, it is recommended to view them with MIRADOR.

# Beyond DIAMMtoIIIF 

Having created several musicological IIIF manifests, the question of additional annotations and metadata naturally arose. Tagging voices, their position, name and content goes far beyond the scope of traditional music inventories. For this reason, Cluster 6 Biblissima+ has taken a new direction: the generation of more semantic data and metadata using computer vision and deep learning techniques (convolutional neural networks). The first YOLO models of polyphonic/monodic vocal recognition for 13th and 14th century repertoires have been developed and are regularly trained to improve. Other models have been developed to improve the recognition of certain complex layouts by focusing on the staves.

![code](https://github.com/Biblissimacluster6/DIAMMtoIIIF/blob/main/img/Chansonnier%20Cordiforme%202.jpg)

Once the YOLO models have been applied, the aim is to retrieve the generated metadata and enrich it with the IIIF manifests. This aspect relies heavily on the potential of IIIF annotations, making it possible to tag musical parts and attribute content to them. Cluster 6 intends to use advanced OCR (Kraken) to integrate automatic (but verified) transcriptions into the annotations, and eventually to create recognition models adapted to more complex problems, such as identifying the style of certain medieval notations, assessing the proximity of certain hands or refining dating.

To train these models, Cluster 6 is relying on hundreds of digitisations collected mainly from the BnF. 

## Documentation française

Le projet DIAMMtoIIIF est le fruit du Cluster 6 Biblissima+ "Les défis du patrimoine musical". DIAMMtoIIIF est un programme Python qui génère un manifeste IIIF (International Image Interoperability Framework) à partir de données extraites de l'API DIAMM (Digital Image Archive of Medieval Music) et des serveurs IIIF de différentes bibliothèques (BnF, Bayerische Staatsbibliothek, etc.).

### Fonctionnement de DIAMMtoIIIF

Ce code récupère des données JSON à partir d'une URL de l'API DIAMM du type https://www.diamm.ac.uk/sources/2387/?format=json. Il utilise les modules ManifestFactory (Prezy_iiif) pour générer et manipuler le manifeste IIIF.
Les données JSON sont traitées en extrayant des informations spécifiques à l'aide d'expressions régulières et du module json. Des manipulations sont effectuées sur les données extraites, comme l'ajout de valeurs vides pour les folios manquants et la gestion des doublons de compositeurs. 
Les informations sur chaque élément du manifeste sont ajoutées à l'aide de boucles et de méthodes de la fabrique de manifestes.
Le code est modulable et diverses metadonnées DIAMM peuvent être ajoutées. Dans sa forme actuelle, le programme prend en charge les titres des oeuvres, les compositeurs, les genres et leur position dans la source. 
Finalement, le manifeste généré (JSON) est converti en une chaîne de caractères et écrit dans un fichier texte (mymusicmanifest.txt).

### Prise en main et prérequis :

En plus de disposer de Python 3, vous devez installer la bibliothèque iiif-prezi.

DIAMMtoIIIFv2 dispose désormais de ses fonctionnalités en ligne de commande :

-u : URL de l'inventaire DIAMM (JSON)
-i : Base de l'URI image
-v : Nombre de premiers folios vides

Voici un exemple de commande :

python DIAMMtoIIIFv2.py -u "https://www.diamm.ac.uk/sources/2387/?format=json" -i "https://gallica.bnf.fr/iiif/ark:/12148/btv1b525044884" -v 9

Pour utiliser DIAMMtoIIIF, vous devez spécifier l'URL de la source DIAMM souhaitée (-u) et la base de l'URI image de la source. Pour la BnF, rentrez l'URL jusqu'à l'identifiant ARK. Pour les URI de la Bayerische S., allez jusqu'aux numéros de pagination (_00001, _00002) : https://api.digitale-sammlungen.de/iiif/image/v2/bsb00079147. Veillez à respecter la forme de l'URL en fonction des conventions adoptées par chaque bibliothèque. Le nombre de premiers folios/pages vides (-v) (sans musique selon l'inventaire DIAMM!) doit être fourni afin que la séquence du manifeste IIIF s'aligne sur les différentes vues. Ce nombre est donc dépendant de l'inventaire DIAMM utilisé, le code ne pouvant donc compenser un manque de précision ou des erreurs potentielles. 

Le programme DIAMMtoIIIF est pour l'heure encore expérimental et nécessite une compréhension de base du langage de programmation Python pour être utilisé pleinement. En raison de son caractère expérimental, il peut être sujet à des bugs ou des limitations. Souvent, ces erreurs sont liées à des particularités des inventaires DIAMM qui, parfois, s'avèrent non standardisés.

### Bibliothèque de manifestes IIIF musicaux :

Jusqu'à maintenant, le programme a permis de générer plusieurs manifestes, disponibles ci-dessus, de manuscrits musicaux du XIIe siècle au XVe siècle de la BnF essentiellement. Dans la mesure où les manifestes ne disposent pas encore d'URI, il est conseillé de les visualiser avec MIRADOR.

