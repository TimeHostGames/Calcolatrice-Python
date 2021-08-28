import time

numeri = input("Quanti numeri devi calcolare? Scegli tra 2, 3 o 4")

if numeri == "2":
    numero1 = int(input("Inserisci primo numero"))
    numero2 = int(input("Inserisci secondo numero"))
    risultato = int(numero1/numero2)
    print(risultato)
    time.sleep(2)
    exec(open("Calcolatrice.py").read())

if numeri == "3":
    numero1 = int(input("Inserisci primo numero"))
    numero2 = int(input("Inserisci secondo numero"))
    numero3 = int(input("Inserisci terzo numero"))
    risultato = int(numero1/numero2/numero3)
    print(risultato)
    time.sleep(2)
    exec(open("Calcolatrice.py").read())

if numeri == "4":
    numero1 = int(input("Inserisci primo numero"))
    numero2 = int(input("Inserisci secondo numero"))
    numero3 = int(input("Inserisci terzo numero"))
    numero4 = int(input("Inserisci quarto numero"))
    risultato = int(numero1/numero2/numero3/numero4)
    print(risultato)
    time.sleep(2)
    exec(open("Calcolatrice.py").read())

if (numeri < "2", numeri > "4"):
    print("Devi selezionare un numero compreso tra 2 e 4")
    time.sleep(2)
    exec(open("Divisione.py").read())