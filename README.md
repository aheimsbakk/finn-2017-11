# Finn.no jobbannonse 2017-11

## [Annonse](https://www.digi.no/storylabs/karriere-og-utdanning/annonse-hva-sier-ditt-utvikler-instinkt-at-du-skal-gjore-her/408527)

## Oppgave

Her er en liten programmeringsnøtt. Du må gjerne legge ved en løsning om du søker hos oss (men det er ikke noe krav).

Anagram
Fila eventyr.txt er en ordliste som inneholder ett ord pr linje. Oppgaven består i å lage et program som leser en fil og som finner alle ord i filen som har ett eller flere anagrammer i lista, og som lister opp disse sammen med det opprinnelige ordet. Merk deg at ikke alle ordene har anagrammer. Du skal kun finne ettordsanagrammer.
Et anagram er et ord eller et uttrykk som er satt sammen ved å stokke om
bokstavene i et annet ord eller uttrykk (http://no.wikipedia.org/wiki/Anagram)
Hver linje i resultatet skal inneholde de ordene som er anagrammer av
hverandre. For eksempel slik
akte, teak, kate
aldri, arild
aller, ralle
alt, tal
andre, rande, denar, ander
....

Vi har mest peiling på følgende språk:
- Java
- JavaScript
- Ruby
- Scala
- Objective-C
- Python
Men overrask oss gjerne med et annet :-)

Hint
En måte å finne ut om to ord er anagrammer, er å sortere bokstavene i ordet og så sammenlikne den sorterte versjonen.
F. eks:
•	akte -> aekt
•	teak -> aekt
Disse ordene er anagrammer av hverandre

## Løsning

Finne anagram i fil med et ord på hver linje.

    $ ./anagram.py -h
    Usage: anagram.py [-h] FILE

    Print all permutations of anagrams in FILE.

    Options:
    --version   show program's version number and exit
    -h, --help  show this help message and exit

## Resultat

    $ ./anagram.py eventyr.txt 
    bar -> bra
    bra -> bar
    truet -> turte
    turte -> truet
    bry -> byr
    byr -> bry
    rå -> år
    år -> rå
    lysnet -> lysten
    lysten -> lysnet
    dem -> med
    med -> dem
    den -> ned
    ned -> den
    ens -> sen
    sen -> ens
    kisten -> skinte
    skinte -> kisten
    engang -> gangen
    gangen -> engang
    søsteren -> søstrene
    søstrene -> søsteren
    denne -> enden
    enden -> denne
    lovt -> tolv
    tolv -> lovt
    stuen -> suten
    suten -> stuen
    niste -> stien
    stien -> niste
    glinset -> glinste
    glinste -> glinset
    ordet -> torde
    torde -> ordet
    ristet -> sitter
    sitter -> ristet
    krok -> rokk
    rokk -> krok
    hellestein -> steinhelle
    steinhelle -> hellestein
    dra -> rad
    rad -> dra
    mor -> rom
    rom -> mor
    kristent -> kristnet
    kristnet -> kristent
    etter -> rette
    rette -> etter
    ende -> nede
    nede -> ende
    at -> ta
    ta -> at
    dro -> ord, rod
    ord -> dro, rod
    rod -> dro, ord
    løst -> støl
    støl -> løst
    navn -> vann
    vann -> navn
