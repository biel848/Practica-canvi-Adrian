# convertidor_monedes.py

def convertidor():
    print("Benvingut al Convertidor de Monedes!")
    
    # Demanar a l'usuari la quantitat i les monedes
    quantitat = float(input("Introdueix la quantitat de diners que vols convertir: "))
    moneda_base = input("Introdueix la moneda original (ex: EUR, USD): ").upper()
    moneda_desti = input("Introdueix la moneda de destí (ex: USD, JPY): ").upper()

    # Tipus de canvi fixos (exemple)
    tipus_de_canvi = {
        "EUR": {"USD": 1.05, "GBP": 0.85, "JPY": 140.0},  # 1 EUR = 1.05 USD, 0.85 GBP, 140 JPY
        "USD": {"EUR": 0.95, "GBP": 0.80, "JPY": 130.0},  # 1 USD = 0.95 EUR, 0.80 GBP, 130 JPY
        "GBP": {"EUR": 1.18, "USD": 1.25, "JPY": 160.0},  # 1 GBP = 1.18 EUR, 1.25 USD, 160 JPY
        "JPY": {"EUR": 0.0071, "USD": 0.0077, "GBP": 0.0062}  # 1 JPY = 0.0071 EUR, 0.0077 USD, 0.0062 GBP
    }

    # Verificar si les monedes existeixen al diccionari
    if moneda_base in tipus_de_canvi and moneda_desti in tipus_de_canvi[moneda_base]:
        # Obtenir el tipus de canvi
        canvi = tipus_de_canvi[moneda_base][moneda_desti]
        # Calcular el resultat
        resultat = quantitat * canvi
        print(f"{quantitat} {moneda_base} equival a {resultat:.2f} {moneda_desti}.")
    else:
        print("Error: Les monedes introduïdes no estan suportades.")

# Executar el convertidor
convertidor()