# Maak een functie aan die een array print
def array_print(array):
    # Loop door de array heen
    for item in array:
        # Print de waarde, zonder naar de volgende regel te gaan
        print(item, end=' ')

    # Ga naar de volgende regel nadat de loop klaar is
    print('')

# Maak wat variabelen aan
a = 5
b = 10
c = 15

# Doe wat met de variabele
x = a + b + c
y = a * b * c
z = a / b

# Maak een array aan
numbers = []

# Voer een loop uit, zovaak als de waarde 'a'
for i in range(a):
    # Voeg de waarde 'b' * 'i' toe aan de array
    numbers.append(b * i)

    # Print de waarde
    print('[', i, '] ', numbers[i] * 10)