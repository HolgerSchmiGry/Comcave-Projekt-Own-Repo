"""
Zinsen berechnen
Schreibe ein Programm, das ein Startkapital, einen Zinssatz und die Anzahl der Jahre speichert. 

Berechne das Endkapital nach Zinseszinsen.

"""

######################################################################
# Zinseszinsen berechnen
######################################################################

# Eingaben
startkapital = float(input("Bitte das Startkapital in Euro eingeben: "))
zinssatz = float(input("Bitte den Zinssatz in Prozent eingeben: "))
jahre = int(input("Bitte die Anzahl der Jahre eingeben: "))

# Endkapital mit Zinseszinsen berechnen
endkapital = startkapital * (1 + zinssatz / 100) ** jahre

# Ausgabe
print("\n--- Zinsberechnung ---")
print(f"Startkapital:    {startkapital:10.2f} Euro")
print(f"Zinssatz:        {zinssatz:10.2f} Prozent")
print(f"Laufzeit:        {jahre:10d} Jahre")
print("--------------------------------")
print(f"Endkapital:      {endkapital:10.2f} Euro")

# Die verwendete Formel lautet:
#
# Endkapital = Startkapital * (1 + Zinssatz / 100) ** Jahre
#
# Dabei bedeutet:
#
# Startkapital = das Geld, das am Anfang vorhanden ist
# Zinssatz = der Zinssatz in Prozent
# Jahre = die Anzahl der Jahre
# Endkapital = das Geld nach der angegebenen Laufzeit
#
# Beispiel:
#
# Startkapital = 1000 Euro
# Zinssatz = 5 Prozent
# Jahre = 3
#
# Endkapital = 1000 * (1 + 5 / 100) ** 3
# Endkapital = 1157.63 Euro
#
# Wichtig ist dabei:
#
# zinssatz / 100
#
# Dadurch wird aus 5 Prozent die Dezimalzahl 0.05.
#
# Mit ** jahre wird die Zahl potenziert.
# Dadurch werden auch die Zinsen aus den vorherigen Jahren wieder mitverzinst.
# Das nennt man Zinseszins.