"""
Programmieraufgabe (Rabatte & Zusatzkosten beim Online-Einkauf)

	1. Der Warenwert (in €) ist gegeben.

	2. Vom Warenwert werden folgende Rabatte und Zuschläge berechnet:
	Mengenrabatt: 10 %
	Sonderrabatt: 5 %
	Versandkosten: 4,90 € (fester Betrag)
	Verpackungskosten: 2 %

	3. Auf den neuen Betrag nach Abzügen und Zuschlägen kommt zusätzlich die Mehrwertsteuer von 19 % drauf.

	Ausgabe:

	Das Programm soll am Ende übersichtlich ausgeben:
	- den eingegebenen Warenwert,
	- den abgezogenen Mengenrabatt,
	- den abgezogenen Sonderrabatt,
	- die hinzugerechneten Versandkosten,
	- die hinzugerechneten Verpackungskosten,
	- die berechnete Mehrwertsteuer,
	- den Endpreis nach allen Abzügen und Zuschlägen.
	
"""

######################################################################
# Rabatte und Zusatzkosten bei einem Online-Einkauf
######################################################################

# Eingabe
warenwert = float(input("Bitte den Warenwert in Euro eingeben: "))

# Rabatte berechnen
mengenrabatt = warenwert * 10 / 100
sonderrabatt = warenwert * 5 / 100

# Rabatte vom Warenwert abziehen
betrag_nach_rabatten = warenwert - mengenrabatt - sonderrabatt

# Zusatzkosten berechnen
versandkosten = 4.90
verpackungskosten = betrag_nach_rabatten * 2 / 100

# Nettobetrag nach Rabatten und Zusatzkosten
nettobetrag = betrag_nach_rabatten + versandkosten + verpackungskosten

# Mehrwertsteuer berechnen
mehrwertsteuer = nettobetrag * 19 / 100

# Endpreis berechnen
endpreis = nettobetrag + mehrwertsteuer

# Ausgabe
print("\n--- Online-Einkauf ---")
print(f"Warenwert:             {warenwert:10.2f} Euro")
print(f"Mengenrabatt:         -{mengenrabatt:10.2f} Euro")
print(f"Sonderrabatt:         -{sonderrabatt:10.2f} Euro")
print(f"Versandkosten:        +{versandkosten:10.2f} Euro")
print(f"Verpackungskosten:    +{verpackungskosten:10.2f} Euro")
print(f"Mehrwertsteuer:       +{mehrwertsteuer:10.2f} Euro")
print("--------------------------------")
print(f"Endpreis:              {endpreis:10.2f} Euro")