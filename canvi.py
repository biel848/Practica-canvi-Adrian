# convertidor_monedes.py
import requests

def obtenir_tipus_de_canvi(base, desti):
    url = f"https://api.exchangerate-api.com/v4/latest/{base}"
    resposta = requests.get(url)
    dades = resposta.json()
    return dades['rates'].get(desti)

def convertidor():
    # Monedes i quantitat fixades
    moneda_base = "EUR"  # Euro
    moneda_desti = "USD"  # Dòlar americà
    quantitat = 100  # Quantitat fixa a convertir

    # Obtenir el tipus de canvi
    tipus_de_canvi = obtenir_tipus_de_canvi(moneda_base, moneda_desti)
    if tipus_de_canvi:
        resultat = quantitat * tipus_de_canvi
        print(f"{quantitat} {moneda_base} equival a {resultat:.2f} {moneda_desti}.")
    else:
        print("No s'ha pogut obtenir el tipus de canvi. Revisa els codis de moneda.")

# Executar el convertidor
convertidor()