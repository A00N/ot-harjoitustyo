# Ohjelmistotekniikan harjoitustyö

## Nonogram

Sovellus on perinteinen japanilainen ristikko, joka tunnetaan nimellä _nonogram_. Sovelluksen idea on tuottaa iloa ja kehittää päättelykykyä. Sovellus toimii myös **Ohjelmistotekniikan kurssin** harjoitustyönä.

## Pelaaminen
Mikäli nonogramit ovat käsitteenä vieras, suosittelen katsomään tämän videon:

https://www.youtube.com/watch?v=zisu0Qf4TAI


### Dokumentaatio

[Release 1](https://github.com/Zo4N/ot-harjoitustyo/releases/tag/viikko5)

[Kayttöohje](https://github.com/Zo4N/ot-harjoitustyo/blob/main/dokumentaatio/kayttoohje.md)

[Vaativuusmäärittely](./dokumentaatio/vaatimusmaarittely.md)

[Työaikakirjanpito](./dokumentaatio/tyoaikakirjanpito.md)

[Changelog](./dokumentaatio/changelog.md)

[Arkkitehtuuri](./dokumentaatio/arkkitehtuuri.md)

### Huomiot!

Vdi yhteydellä linuxissa kyseinen ohjelma _toimii_ **mutta** kuvasuhteet eivät tuntemattomaksi syyksi jäänestä viasta huolimatta toimi oikein.

Kuva miltä sovelluksen pitäisi näyttää (ja näyttää windowsilla, macilla sekä fuksiläppärillä)

[Kuva](./dokumentaatio/kuvat/toimivasovellus.PNG)

### Asennus ja käyttäminen

Aloita kloonaamalla repositorio, lisää alla olevat komennot terminaalissa

git clone https://github.com/Zo4N/ot-harjoitustyo

curl -sSL https://install.python-poetry.org/. | POETRY_HOME=$HOME/.local python3 

export PATH="$HOME/.local/bin:$PATH"

poetry update

poetry run invoke start
