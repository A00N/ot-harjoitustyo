# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovelluksen tarkoitus on tuottaa iloa käyttäjälle, sekä kehittää päättelykykyä japanilaisen ristikon muodossa. Sovellusta on mahdollista käyttää offline - tilassa. Sovellus 
sisältää eri vaikeusasteisia ristikoita, jolloin eritasoisille käyttäjille löytyy kaikille haastetta.

## Käyttäjät

Sovelluksessa on ainoastaan yksi käyttäjärooli eli _pelaaja_. 

## Käyttöliittymäluonnos
Sovellus koostuu seuraavista näkymistä:
- Päävalikko
- Tasonäkymä
- Taso(t)

![](./kuvat/paavalikko-tasot-taso.png)

##Perusversion toiminnot

# Päävalikossa 

- Pelaaja voi selata eri tasoja
- Pelaaja voi valita tasoista haluamansa tason ja pelata sitä
- Pelaaja näkee mitkä tasoita on suorittanut
- Pelaaja voi poistua pelistä

# Pelissä

- Pelaajalla on kolme elämää
- Pelaaja voi lisätä rasteja ruutuun, johon ei tule neliötä
- Pelaaja voi lisätä neliön ruutuun, johon uskoo sen kuuluvan
- Pelaajalle menettää elämän, mikäli laittaa neliön väärään ruutuun ja sen tilalle ilmestyy rasti
- Peliin tulee automaattisesti rasti, kun rivin tai sarakkeen neliöt tulevat täyteen.
- Pelaaja voi poistua päävalikkoon, vaikka tasoa ei olisi tehty


## Jatkokehitysideat

Perusversion jälkeen mahdollisia lisäyksiä:

- Pelissä voisi ansaita "kredittejä" suorittamalla tasoja, joilla voi ostaa vihjeitä, ulkoasuja tai mahdollisesti uusia tasoja.
- Peliin voisi lisätä kirjaston erilaisia kuvia, joista pelaaja voisi valita, josta peli sitten luo automaattisesti tason
- Peliin voisi lisätä kirjautumis- ja rekisteröitymistoimminnon, jotta käyttäjät voivat pitää kirjaa suoritetuista tasoistaan vaikka käyttäjillä oli käytössä sama laite
- Peliin voisi lisätä **highscore** toiminnon, jolloin pelaajat voisivat vertailla omia tuloksiaan
- Peliin voisi lisätä ajastimen, jolloin se mittaisi myös kauanko pelaajalla menee aikaa tason suorittamiseen.
