
import random

tal = input("Skriv ett tal: ")

while tal.isdigit() == False:
    print("Du får bara skriva siffror!")
    tal = input("Försök igen: ")

print("Tack!")

ord = input("Skriv ett ord: ")
print(ord[:10])

ord = input("Skriv ett ord: ")

if len(ord) > 10:
    ord = ord[:10] + "..."

print(ord)

namn = input("Skriv ditt namn: ")

if namn.isalpha():
    print(namn.upper())
else:
    print("Du får bara skriva bokstäver!")

hemligt_tal = random.randint(1, 13)

print("Gissa ett tal mellan 1 och 13. Skriv q för att avsluta.")

gissning = input("Din gissning: ")

while gissning.lower() != "q":

    if gissning.isdigit():
        tal = int(gissning)

        if tal == hemligt_tal:
            print("Rätt!")
            hemligt_tal = random.randint(1, 13)

        elif tal < hemligt_tal:
            print("För lågt!")

        else:
            print("För högt!")

    else:
        print("Skriv ett tal eller q.")

    gissning = input("Gissa igen: ")

print("Spelet avslutades!")