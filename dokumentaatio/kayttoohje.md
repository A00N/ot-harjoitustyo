### Käyttöohje
Lataa projektin viimeisin release. Tämä löytyy [https://github.com/Zo4N/ot-harjoitustyo/releases] tästä.


## Käynnistäminen

Ennen käyttämistä, tulee käyttäjän asentaa riippuvuuksia.

Kirjoita seuraavat komennot terminaaliisi

```bash
poetry install
```


Tämän jälkeen käynnistä ohjelma:

```
poetry run invoke start
```

Tämän jälkeen sinulle aukeaa päävalikko. Valikosta voit painaa nappia "Play", päästäksesi suoraan tasoon 1 tai voit painaa nappia "Levels" ja selata tasot läpi.

Ollessasi tasossa, hiiren vasen painike lisää ruudukkoon mustan ruudun ja oikea painike lisää harmaan. Musta ruutu tarkoittaa siihen kuuluvan merkin, ja harmaa sen olevan "tyhjä" ruutu,
Kun taso on suoritettu vihjeiden mukaan, ilmestyy ruutuun viesti "Läpäisty". Tämän jälkeen tasoa ei voi enää muokata.

Päävalikossa painamalla "Quit", peli sulkeutuu.
