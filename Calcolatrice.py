operazione = input("Scegli tra addizione, sottrazione, moltiplicazione e divisione")

if operazione == "addizione":
    exec(open("Addizione.py").read())

if operazione == "sottrazione":
    exec(open("Sottrazione.py").read())

if operazione == "moltiplicazione":
    exec(open("Moltiplicazione.py").read())

if operazione == "divisione":
    exec(open("Divisione.py").read())