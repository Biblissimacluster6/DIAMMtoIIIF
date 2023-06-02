import json
import urllib.request
import re
from iiif_prezi.factory import ManifestFactory

url = "https://www.diamm.ac.uk/sources/2387/?format=json"
response = urllib.request.urlopen(url)
data = json.loads(response.read())

factory = ManifestFactory()
factory.set_base_prezi_uri("https://example.com/iiif/")
factory.set_base_image_uri("https://gallica.bnf.fr/iiif/ark:/12148/btv1b525044884/")
factory.set_iiif_image_info(version="2.0", lvl="2")

mf = factory.manifest(label=data["display_name"])
mf.viewingDirection = "left-to-right"
mf.set_metadata({
     "Metadata source": data["url"],
     "Shelfmark": data["display_name"],
     "Repository": data["archive"]["name"],
     "Date": data["date_statement"],
     "Type": data["source_type"],
     "Surface type": data["surface_type"],
     "Measurements": data["measurements"]
})
mf.description = data["notes"][0]['note']
mf.viewingHint = "paged"
d = str(data)

void_folios = 9 #adds the number of void views before music
y = void_folios + 1

def get_title():
    titlelist = []
    titlepattern = re.compile("'composition':\s*(.*?)\s*, 'composers'")
    titlematches = titlepattern.findall(d)
    for match in titlematches:
        titlelist.append(match)
    return titlelist
titleliste = get_title()

def get_composer(d):
    composer_list = []
    composer_pattern = re.compile("'full_name':\s*(.*?)\s*, 'uncertain':\s*(?: False}],| True}],)")
    composer_matches = composer_pattern.findall(d)
    for match in composer_matches:
        composer_list.append(match)
    return composer_list
composerliste = get_composer(d)

def manage_double_composer(composerliste):
    clean = list(composerliste)
    for i in range(len(clean)):
        clean[i] = re.sub(r", 'uncertain'.*?'full_name'", '', clean[i])
    for i in range(len(clean)):
        clean[i] = clean[i].replace(":", " or")
    return clean
composerliste = manage_double_composer(composerliste)

def get_genre(d):
    genre_list = []
    genre_pattern = re.compile("'genres':\s*(.*?)\s*, 'folio_start'")
    genre_matches = genre_pattern.findall(d)
    for match in genre_matches:
        genre_list.append(match)
    return genre_list
genreliste = get_genre(d)

def get_folio_start(d):
    folio_start = []
    folio_start_pattern = re.compile("'folio_start':\s*(.*?)\s*, '")
    folio_start_matches = folio_start_pattern.findall(d)
    for match in folio_start_matches:
        folio_start.append(match)
    for i in range(len(folio_start)):
        if 'v' not in folio_start[i] and 'r' not in folio_start[i]:
            folio_start[i] += 'r'
    z = len(titleliste)
    k = len(folio_start) - z
    del folio_start[-k:-1]
    del folio_start[-1]
    print(folio_start)
    return folio_start
foliostart = get_folio_start(d)

def cleanfoliostart(foliostart):
    for i in range(len(foliostart)):
        foliostart[i] = foliostart[i].replace('"', '')
        foliostart[i] = foliostart[i].replace("'", "")
        if foliostart[i] == '[D]v':
            index = foliostart.index('[D]v')
            foliostart[index] = foliostart[index].replace('[D]v', '0v')
        if foliostart[i] == '[0]v':
            index = foliostart.index('[0]v')
            foliostart[index] = foliostart[index].replace('[0]v', '0v')
        if foliostart[i] == '[0]r':
            index = foliostart.index('[0]r')
            foliostart[index] = foliostart[index].replace('[0]r', '0r')
    return foliostart
foliostart = cleanfoliostart(foliostart)

def getfolioend(d):
    folioend = []
    folioendpattern = re.compile("'folio_end':\s*(.*?)\s*, '")
    folioendmatches = folioendpattern.findall(d)
    for match in folioendmatches:
        folioend.append(match)
    for i in range(len(folioend)):
        if 'v' not in folioend[i] and 'r' not in folioend[i]:
            folioend[i] += 'r'
    z = len(titleliste)
    k = len(folioend) - z
    del folioend[-k:-1]  # keep only correct folios
    del folioend[-1]
    return folioend
folioend = getfolioend(d)

def cleanfolioend(folioend):
    for i in range(len(folioend)):
        folioend[i] = folioend[i].replace('"', '')
        folioend[i] = folioend[i].replace("'", "")
    return folioend
folioend = cleanfolioend(folioend)

indices = []
for i in range(len(foliostart) - 1):
   if foliostart[i] == foliostart[i + 1]:
      indices.append(i)
for i in range(len(indices)):
      indices[i] += 1
indices.sort(reverse=True)
for i in indices:
   foliostart.pop(i)
   folioend.pop(i)
   composerliste.pop(i)
   titleliste.pop(i)
   genreliste.pop(i)
folioend.insert(0, "V")  # aligns folioend and foliostart
matching_indices = []
for i, (item1, item2) in enumerate(zip(foliostart, folioend)):
   if item1 == item2:
      matching_indices.append(i)
folioend.pop(0)
matching_indices.sort(reverse=True)
for i in matching_indices:
   foliostart.pop(i)
   folioend.pop(i)
   composerliste.pop(i)
   titleliste.pop(i)
   genreliste.pop(i)

def interpolationandcoef(foliostart):
    fol1 = [item[-1] for item in foliostart]
    num1 = [item[:-1] for item in foliostart]
    num1 = list(map(int, num1))
    num1.sort()
    fol2 = [item[-1] for item in folioend]
    num2 = [item[:-1] for item in folioend]
    num2 = list(map(int, num2))
    num2.sort()
    viewnumber = []
    for element1, element2 in zip(num1, num2):
        if element2 - element1 == 0:
            viewnumber.append("0")
        if element2 - element1 == 1:
            viewnumber.append("1")
        if element2 - element1 == 2:
            viewnumber.append("2")
        if element2 - element1 == 3:
            viewnumber.append("3")
        if element2 - element1 == 4:
            viewnumber.append("4")

    invfoliation = []
    for i in range(len(viewnumber)):
        invfoliation.append(fol1[i] + fol2[i] + viewnumber[i])
    for i in range(len(invfoliation)):
        invfoliation[i] = invfoliation[i].replace('vv0', '1').replace('rr0', '1').replace('vr1', '2').replace('rv1',
                                                                                                              '4').replace(
            'vv1', '3').replace('rr2', '5').replace('rr1', '3').replace('vr2', '4').replace('rv2', '6').replace('rv0',
                                                                                                               '2').replace(
            'vv2', '5').replace('rv3', '8').replace('vr3', '6').replace('rr3', '7').replace('vr4', '8').replace('vv3',
                                                                                                               '7')

    listeinter = num1
    del listeinter[0]

    interpolation = []
    for element1, element2 in zip(listeinter, num2):
        interpolation.append(element1 - element2)

    listeinter2 = fol1
    del listeinter2[0]

    invinterpolation = []
    for i in range(len(interpolation)):
        invinterpolation.append(listeinter2[i] + fol2[i])

    for i in range(len(invinterpolation)):
        if invinterpolation[i] == "vv":
            interpolation[i] = interpolation[i] * 2 - 1
        if invinterpolation[i] == "rr":
            interpolation[i] = interpolation[i] * 2 - 1
        if invinterpolation[i] == "vr":
            interpolation[i] = interpolation[i] * 2
        if invinterpolation[i] == "rv":
            interpolation[i] = interpolation[i] * 2 - 2

    coeflist = []
    for i in range(len(interpolation)):
        coeflist.append(invfoliation[i])
        coeflist.append(interpolation[i])
    coeflist.append(invfoliation[-1])
    for index, value in enumerate(coeflist):
        if value == -1:
            coeflist[index] = 0
    return coeflist
coeflist = interpolationandcoef(foliostart)

def nonliste():
    noneliste = []
    a = "None"
    for i in range(len(composerliste)):
        noneliste.append(a)
    return noneliste
noneliste = nonliste()

finalcoef = list(map(int, coeflist))

def composercoef(composerliste):
    composer = []
    completecomposer = []
    for i in range(len(composerliste)):
        completecomposer.append(composerliste[i])
        completecomposer.append(noneliste[i])
    for element1, element2 in zip(completecomposer, finalcoef):
        for i in range(element2):
            composer.append(element1)
    return composer
composer = composercoef(composerliste)

def titlecoef(titleliste):
    completetitle = []
    titre = []
    for i in range(len(titleliste)):
        completetitle.append(titleliste[i])
        completetitle.append(noneliste[i])
    for element1, element2 in zip(completetitle, finalcoef):
        for i in range(element2):
            titre.append(element1)
    return titre
titre = titlecoef(titleliste)

def genrecoef():
    completegenre = []
    genre = []
    for i in range(len(genreliste)):
        completegenre.append(genreliste[i])
        completegenre.append(noneliste[i])
    for element1, element2 in zip(completegenre, finalcoef):
        for i in range(element2):
            genre.append(element1)
    return genre
genre = genrecoef()


def add_none(composer):
    for i in range(y):
        composer.insert(0, 'None')
    return composer
composer = add_none(composer)

def add_none2(titre):
    for i in range(y):
        titre.insert(0, 'None')
    return titre
titre = add_none2(titre)

def add_nonegenre(genre):
    for i in range(y): #insert number of void folios
        genre.insert(0, 'None')
    for i in range(len(genre)):
        genre[i] = genre[i].replace('[','').replace(']', '')
    return genre
genre = add_nonegenre(genre)

def foliostartcoef():
    completefolio = []
    firstfolio = []
    for i in range(len(composerliste)):
        completefolio.append(foliostart[i])
        completefolio.append(noneliste[i])
    for element1, element2 in zip(completefolio, finalcoef):
        for i in range(element2):
            firstfolio.append(element1)
    return firstfolio
firstfolio = foliostartcoef()

def add_nonefirstfolio(firstfolio):
    for i in range(y):
        firstfolio.insert(0, 'None')
    return firstfolio
firstfolio = add_nonefirstfolio(firstfolio)

def folioendcoef():
    lastfolio = []
    completefolioend = []
    for i in range(len(composerliste)):
        completefolioend.append(folioend[i])
        completefolioend.append(noneliste[i])
    for element1, element2 in zip(completefolioend, finalcoef):
        for i in range(element2):
            lastfolio.append(element1)
    return lastfolio
lastfolio = folioendcoef()

def add_nonelastfolio(lastfolio):
    for i in range(y):
        lastfolio.insert(0, 'None')
    return lastfolio
lastfolio = add_nonelastfolio(lastfolio)

def sequence(titre, genre, firstfolio, lastfolio, composer, mf):
    num_items = len(titre)
    seq = mf.sequence()
    for x in range(num_items):
        cvs = seq.canvas(ident="f%s" % x, label="Canvas %s" % x)
        cvs.set_hw(1000, 1000)
        anno = cvs.annotation()
        metadata = {
            "Work title": titre[x] if titre[x] is not None else "",
            "Folio start": firstfolio[x] if firstfolio[x] is not None else "",
            "Folio end": lastfolio[x] if lastfolio[x] is not None else "",
            "Composer": composer[x] if composer[x] is not None else ""
        }
        if len(genre) == num_items:
            metadata["Genre"] = genre[x] if genre and genre[x] is not None else ""
        cvs.set_metadata(metadata)
        img = factory.image("f%s" % x, iiif=True)
        chc = anno.choice(img, [img])
    manifest_string = mf.toString(compact=False)  # converts manifest to string
    with open("monfichier.txt", "w") as fichier:  # writes string manifest into a txt
        fichier.write(manifest_string)
    return manifest_string

# Call the sequence function with the required parameters
sequence(titre, genre, firstfolio, lastfolio, composer, mf)
