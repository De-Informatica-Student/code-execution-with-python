# Het Uitvoeren van Code

Code programmeren is vaak vanzelfsprekend, maar is de uitvoer dat ook.
Bij het uitvoeren van programmacode komt namelijk best nog wel het één en ander kijken.
Er moeten worden bijgehouden op welke regel de code is,
welke variabelen er zijn, welke waarden deze variabelen hebben, etc.
Dit wordt allemaal voor ons geregeld, maar het is wel handig om te weten hoe dit werkt.

## Inhoudsopgave

1. [De Code](#de-code)
2. [De Program Counter](#de-program-counter)
3. [Stack Trace](#stack-trace)
4. [Geheugen](#geheugen)
5. [Herhalingen en Voorwaardes](#herhalingen-en-voorwaardes)
6. [Stack Frames](#stack-frames)

## De Code

De code die gebruikt gaat worden tijdens deze uitleg is geschreven in Python.
Python is een programmeertaal die erg makkelijk te lezen is, en redelijk makkelijk te debuggen.
De complete code met uitleg kun je terug vinden in de map `src`.
Een algemene beschrijven van de code:

```python
# Een functie die een array print
def array_print(array):
    for item in array:
        print(item, end=' ')

    print('')

# Wat variabelen
a = 5
b = 10
c = 15

# Wat berekeningen
x = a + b + c
y = a * b * c
z = a / b

# Een array
numbers = []

# Een loop die de array vult
for i in range(a):
    numbers.append(b * i)

# Print de array
array_print(numbers)
```

## De Program Counter

De program counter (of instruction pointer) is een register die bijhoudt op welke regel de code is.
Een register is een stukje geheugen van de processor om tijdelijk waarden in op te slaan.
Als de program counter op 1 staat dan is de code voor regel 1,
hij moet nog worden uitgevoerd.
Zodra de program counter naar 2 gaat, dan is regel 1 uitgevoerd.
Vanaf dit punt wordt program counter afgekort met PC.

De PC begint op ```1```, vind hier een stukje commentaar en negeert het.
Dan komt de PC in ons programma op ```2``` te staan, staat daar een functie definitie.
Deze wordt niet uitgevoerd, maar de locatie van de functie wordt onthouden.
Daarna gaat de PC naar het einde van de functie, dit is regel 7.
De PC staat nu op ```7```. Dit is een lege regel, dus de PC gaat naar ```8```.

## Stack Trace

Een Stack Trace (of state strace) is een notatie om de staat van het programma te beschrijven.
Deze notatie wordt vaak gebruikt bij het debuggen van programma's.
Iedere stap die we zetten met de PC wordt opgeschreven in zijn eigen trace.

| PC | Functies                     |
|----|------------------------------|
| 1  |                              |
| 2  |                              |
| 7  | ```<func> array_print @ 2``` |

Na het uitvoeren van regel twee zie je dat de program counter op ```7``` staat.
Daarnaast is de functie definitie toegevoegd aan de stack trace.
Er wordt aangegeven dat het een functie is met ```<func>```,
deze heeft de naam ```array_print``` en staat op regel ```2```.

Vaak tijdens het uitschrijven van de stack trace wordt deze afgekort.
Alleen de regels die een wijziging veroorzaken in de stack worden opgeschreven.
Dit vanwege de duidelijkheid.
Het afkorten van onze tabel zou regel 1 verwijderen.
Regel 2 is waar de verandering plaatsvind, dus die willen we in de tabel houden.
Dit geld ook voor regel 7, hier zie je het resultaat van regel 2 terug.
Op die manier zien we de begin situatie en de eind situatie.
Voor de rest van de uitleg wordt de stack trace *niet* afgekort.

| PC | Functies                     |
|----|------------------------------|
| 2  |                              |
| 7  | ```<func> array_print @ 2``` |

## Geheugen

Fucties zijn niet het enige dat wordt bijgehouden, ook variabelen worden bijgehouden.
Onze code gaat nu drie variabele declareren, ```a```, ```b``` en ```c```.
Alle code krijgt direct een waarde toegewezen.
Dit kunnen we stap voor stap opschrijven in de stack trace.

| PC | Functies                     | a | b | c |
|----|------------------------------|---|---|---|
| 7  | ```<func> array_print @ 2``` |   |   |   |
| 8  | ```<func> array_print @ 2``` |   |   |   |
| 9  | ```<func> array_print @ 2``` |   |   |   |
| 10 | ```<func> array_print @ 2``` | 5 |   |   |
| 11 | ```<func> array_print @ 2``` | 5 | 10|   |
| 12 | ```<func> array_print @ 2``` | 5 | 10| 15|

Iedere variabele krijgt een andere kolom in de tabel.
Zo kunnen we zien welke waarde iedere variabele heeft op ieder moment.
De volgende drie regels code in het progamma zijn berekeningen.
Deze berekeningen gebruiken de variabelen ```a```, ```b``` en ```c```.
Iedere keer als er een berekening wordt uitgevoerd, wordt er een expressie geëvalueerd.
Deze expressie wordt niet opgeschreven in de stack trace.
We kunnen de expressies in ons hoofd uitvoeren met de opgeschreven waardes.

| PC | Functies                     | a | b | c | x | y | z |
|----|------------------------------|---|---|---|---|---|---|
| 12 | ```<func> array_print @ 2``` | 5 | 10| 15|   |   |   |
| 13 | ```<func> array_print @ 2``` | 5 | 10| 15|   |   |   |
| 14 | ```<func> array_print @ 2``` | 5 | 10| 15|   |   |   |
| 15 | ```<func> array_print @ 2``` | 5 | 10| 15| 30|   |   |
| 16 | ```<func> array_print @ 2``` | 5 | 10| 15| 30|750|   |
| 17 | ```<func> array_print @ 2``` | 5 | 10| 15| 30|750|0.5|

Als laatste gaan we een array definieren.
Deze werkt hetzelfde als de andere variabelen.
In het geheugen werkt die niet altijd hetzelfde,
maar dat is een onderwerp voor een andere keer.
Voor nu gaan we door met het definieren van de array.

| PC | Functies                     | a | b | c | x | y | z | numbers |
|----|------------------------------|---|---|---|---|---|---|---------|
| 17 | ```<func> array_print @ 2``` | 5 | 10| 15| 30|750|0.5|         |
| 18 | ```<func> array_print @ 2``` | 5 | 10| 15| 30|750|0.5|         |
| 19 | ```<func> array_print @ 2``` | 5 | 10| 15| 30|750|0.5|         |
| 20 | ```<func> array_print @ 2``` | 5 | 10| 15| 30|750|0.5| []      |

## Herhalingen en Voorwaardes

Nu weten we hoe variabelen werken in de stack trace,
maar hoe zit het met herhalingen en voorwaardes?
Loops hebben een begin en een eind.
In het geval van een for loop is het begin de declaratie van ```i```.
Het einde is de laatste regel van de loop, in dit geval regel ```23```.
Maar in plaats van de regel ```24```, gaat de PC naar het begin van de loop.

| PC | Functies                     | a | b | c | x | y | z | numbers             | i |
|----|------------------------------|---|---|---|---|---|---|---------------------|---|
| 20 | ```<func> array_print @ 2``` | 5 | 10| 15| 30|750|0.5| []                  |   |
| 21 | ```<func> array_print @ 2``` | 5 | 10| 15| 30|750|0.5| []                  |   |
| 22 | ```<func> array_print @ 2``` | 5 | 10| 15| 30|750|0.5| []                  |   |
| 23 | ```<func> array_print @ 2``` | 5 | 10| 15| 30|750|0.5| []                  | 0 |
| 22 | ```<func> array_print @ 2``` | 5 | 10| 15| 30|750|0.5| [0]                 | 0 |
| 23 | ```<func> array_print @ 2``` | 5 | 10| 15| 30|750|0.5| [0]                 | 1 |
| 22 | ```<func> array_print @ 2``` | 5 | 10| 15| 30|750|0.5| [0,100]             | 1 |
| 23 | ```<func> array_print @ 2``` | 5 | 10| 15| 30|750|0.5| [0,100]             | 2 |
| 22 | ```<func> array_print @ 2``` | 5 | 10| 15| 30|750|0.5| [0,100,200]         | 2 |
| 23 | ```<func> array_print @ 2``` | 5 | 10| 15| 30|750|0.5| [0,100,200]         | 3 |
| 22 | ```<func> array_print @ 2``` | 5 | 10| 15| 30|750|0.5| [0,100,200,300]     | 3 |
| 23 | ```<func> array_print @ 2``` | 5 | 10| 15| 30|750|0.5| [0,100,200,300]     | 4 |
| 22 | ```<func> array_print @ 2``` | 5 | 10| 15| 30|750|0.5| [0,100,200,300,400] | 4 |
| 24 | ```<func> array_print @ 2``` | 5 | 10| 15| 30|750|0.5| [0,100,200,300,400] |   |

### Oefening Tussendoor

Het functioneren van loops is vaak beter te zien in een while loop.
Dit komt omdat de informatie die we nodig hebben om de loop uit te voeren expliciet is.
Probeer voor jezelf deze code eens uit te schrijven in een stack trace.

```python
i = 5
while i < 100:
    i = i * i
```

## Stack Frames

Op het moment dat een functie wordt aangeroepen, wordt er een stack frame aangemaakt.
Een stack frame is een stukje geheugen dat wordt gebruikt om de lokale variabelen van een functie op te slaan.
De tabel die wij tot nu toe hebben gebruikt één stack frame.
Meerdere stack frames samen zijn een call stack.

De bovenste stack frame is de stack frame van de functie die op dit moment wordt uitgevoerd.
De stack frame daaronder is de stack frame van de functie die de huidige functie heeft aangeroepen.
Bij het aanroepen van een functie, komt er een nieuwe stack bovenop de oude.

| PC | Functies                     | a | b | c | x | y | z | numbers             |     |
|----|------------------------------|---|---|---|---|---|---|---------------------|-----|
| 24 | ```<func> array_print @ 2``` | 5 | 10| 15| 30|750|0.5| [0,100,200,300,400] |     |
| 25 | ```<func> array_print @ 2``` | 5 | 10| 15| 30|750|0.5| [0,100,200,300,400] |     |
| 26 | ```<func> array_print @ 2``` | 5 | 10| 15| 30|750|0.5| [0,100,200,300,400] |     |
| 26 | ```<func> array_print @ 2``` | 5 | 10| 15| 30|750|0.5| [0,100,200,300,400] | ... |

| PC | Functies                     |
|----|------------------------------|
| 2  | ```<func> array_print @ 2``` |

De nieuwe stack frame wordt aangegeven met een extra tabel.
In deze tabel kunnen we vervolgens de lokale variabelen van de functie opslaan.
Met de ... in de eerste tabel geef ik aan dat er gewacht wordt op antwoord van de functie.
Die functie kunnen we nu in de tweede tabel uitvoeren.
Dit werkt op exact dezelfde manier als tot nu toe.
Eerst wordt de parameter klaargezet, en dan de rest van de functie uitgevoerd.

| PC | Functies                     | array               | item |
|----|------------------------------|---------------------|------|
| 2  | ```<func> array_print @ 2``` |                     |      |
| 3  | ```<func> array_print @ 2``` | [0,100,200,300,400] |      |
| 4  | ```<func> array_print @ 2``` | [0,100,200,300,400] | 0    |
| 3  | ```<func> array_print @ 2``` | [0,100,200,300,400] | 0    |
| 4  | ```<func> array_print @ 2``` | [0,100,200,300,400] | 100  |
| 3  | ```<func> array_print @ 2``` | [0,100,200,300,400] | 100  |
| 4  | ```<func> array_print @ 2``` | [0,100,200,300,400] | 200  |
| 3  | ```<func> array_print @ 2``` | [0,100,200,300,400] | 200  |
| 4  | ```<func> array_print @ 2``` | [0,100,200,300,400] | 300  |
| 3  | ```<func> array_print @ 2``` | [0,100,200,300,400] | 300  |
| 4  | ```<func> array_print @ 2``` | [0,100,200,300,400] | 400  |
| 3  | ```<func> array_print @ 2``` | [0,100,200,300,400] | 400  |
| 5  | ```<func> array_print @ 2``` | [0,100,200,300,400] |      |
| 6  | ```<func> array_print @ 2``` | [0,100,200,300,400] |      |

En vanaf dit punt kunnen we de eerste stack trace weer verder uitwerken.

| PC | Functies                     | a | b | c | x | y | z | numbers             | i |     |
|----|------------------------------|---|---|---|---|---|---|---------------------|---|-----|
| 1  |                              |   |   |   |   |   |   |                     |   |     |
| 2  |                              |   |   |   |   |   |   |                     |   |     |
| 7  | ```<func> array_print @ 2``` |   |   |   |   |   |   |                     |   |     |
| 8  | ```<func> array_print @ 2``` |   |   |   |   |   |   |                     |   |     |
| 9  | ```<func> array_print @ 2``` |   |   |   |   |   |   |                     |   |     |
| 10 | ```<func> array_print @ 2``` | 5 |   |   |   |   |   |                     |   |     |
| 11 | ```<func> array_print @ 2``` | 5 | 10|   |   |   |   |                     |   |     |
| 12 | ```<func> array_print @ 2``` | 5 | 10| 15|   |   |   |                     |   |     |
| 13 | ```<func> array_print @ 2``` | 5 | 10| 15|   |   |   |                     |   |     |
| 14 | ```<func> array_print @ 2``` | 5 | 10| 15|   |   |   |                     |   |     |
| 15 | ```<func> array_print @ 2``` | 5 | 10| 15| 30|   |   |                     |   |     |
| 16 | ```<func> array_print @ 2``` | 5 | 10| 15| 30|750|   |                     |   |     |
| 17 | ```<func> array_print @ 2``` | 5 | 10| 15| 30|750|0.5|                     |   |     |
| 18 | ```<func> array_print @ 2``` | 5 | 10| 15| 30|750|0.5|                     |   |     |
| 19 | ```<func> array_print @ 2``` | 5 | 10| 15| 30|750|0.5|                     |   |     |
| 20 | ```<func> array_print @ 2``` | 5 | 10| 15| 30|750|0.5| []                  |   |     |
| 21 | ```<func> array_print @ 2``` | 5 | 10| 15| 30|750|0.5| []                  |   |     |
| 22 | ```<func> array_print @ 2``` | 5 | 10| 15| 30|750|0.5| []                  |   |     |
| 23 | ```<func> array_print @ 2``` | 5 | 10| 15| 30|750|0.5| []                  | 0 |     |
| 22 | ```<func> array_print @ 2``` | 5 | 10| 15| 30|750|0.5| [0]                 | 0 |     |
| 23 | ```<func> array_print @ 2``` | 5 | 10| 15| 30|750|0.5| [0]                 | 1 |     |
| 22 | ```<func> array_print @ 2``` | 5 | 10| 15| 30|750|0.5| [0,100]             | 1 |     |
| 23 | ```<func> array_print @ 2``` | 5 | 10| 15| 30|750|0.5| [0,100]             | 2 |     |
| 22 | ```<func> array_print @ 2``` | 5 | 10| 15| 30|750|0.5| [0,100,200]         | 2 |     |
| 23 | ```<func> array_print @ 2``` | 5 | 10| 15| 30|750|0.5| [0,100,200]         | 3 |     |
| 22 | ```<func> array_print @ 2``` | 5 | 10| 15| 30|750|0.5| [0,100,200,300]     | 3 |     |
| 23 | ```<func> array_print @ 2``` | 5 | 10| 15| 30|750|0.5| [0,100,200,300]     | 4 |     |
| 22 | ```<func> array_print @ 2``` | 5 | 10| 15| 30|750|0.5| [0,100,200,300,400] | 4 |     |
| 24 | ```<func> array_print @ 2``` | 5 | 10| 15| 30|750|0.5| [0,100,200,300,400] |   |     |
| 25 | ```<func> array_print @ 2``` | 5 | 10| 15| 30|750|0.5| [0,100,200,300,400] |   |     |
| 26 | ```<func> array_print @ 2``` | 5 | 10| 15| 30|750|0.5| [0,100,200,300,400] |   |     |
| 26 | ```<func> array_print @ 2``` | 5 | 10| 15| 30|750|0.5| [0,100,200,300,400] |   | ... |
| 27 | ```<func> array_print @ 2``` | 5 | 10| 15| 30|750|0.5| [0,100,200,300,400] |   |     |
