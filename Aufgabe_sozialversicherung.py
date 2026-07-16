######################################################################
# Ein Programm zur Berechnung der Sozialversicherung
#	
#	Gegeben sind folgende Werte
#	- Bruttolohn in Euro
#	- Arbeitslosenversicherung in %	
#	- Rentenversicherung in %	
#	- Krankenversicherung in %	
#	- Pflegeversicherung in %	
#	- (Version 2: Die Angabe der Anzahl der Kinder)
#
#	Als Ergebnis sollen folgende Werte angezeigt werden:
#	- Bruttolohn in Euro 
#	- Betrag der für die Arbeitslosenversicherung abgezogen wird	
#	- Betrag der für die Rentenversicherung abgezogen wird	
#	- Betrag der für die Krankenversicherung abgezogen wird	
#	- Betrag der für die Pflegeversicherung abgezogen wird	
#	- Das zu versteuernde Einkommen
#
#	Die Beitragsbemessungsgrenze soll ert mal nicht betrachtet werden 
#   Dies kann in einer weiteren Verion eingebaut werden 
#
#	Die Kirchensteuer soll nicht betrachtet werden.
#	Dies kann in einer weiteren Verion eingebaut werden 
#
######################################################################

######################################################################
# Berechnung der Sozialversicherung
######################################################################

# Eingaben
bruttolohn = float(input("Bitte den Bruttolohn in Euro eingeben: "))

arbeitslosenversicherung_prozent = float(
    input("Arbeitslosenversicherung in Prozent: ")
)

rentenversicherung_prozent = float(
    input("Rentenversicherung in Prozent: ")
)

krankenversicherung_prozent = float(
    input("Krankenversicherung in Prozent: ")
)

pflegeversicherung_prozent = float(
    input("Pflegeversicherung in Prozent: ")
)

# Berechnungen
arbeitslosenversicherung = (
    bruttolohn * arbeitslosenversicherung_prozent / 100
)

rentenversicherung = (
    bruttolohn * rentenversicherung_prozent / 100
)

krankenversicherung = (
    bruttolohn * krankenversicherung_prozent / 100
)

pflegeversicherung = (
    bruttolohn * pflegeversicherung_prozent / 100
)

# Alle Sozialversicherungsbeiträge zusammenrechnen
sozialversicherung_gesamt = (
    arbeitslosenversicherung
    + rentenversicherung
    + krankenversicherung
    + pflegeversicherung
)

# Vereinfachte Berechnung laut Aufgabenstellung
zu_versteuerndes_einkommen = bruttolohn - sozialversicherung_gesamt

# Ausgabe
print("\n--- Ergebnis der Berechnung ---")
print(f"Bruttolohn:                     {bruttolohn:10.2f} Euro")
print(f"Arbeitslosenversicherung:       {arbeitslosenversicherung:10.2f} Euro")
print(f"Rentenversicherung:             {rentenversicherung:10.2f} Euro")
print(f"Krankenversicherung:            {krankenversicherung:10.2f} Euro")
print(f"Pflegeversicherung:             {pflegeversicherung:10.2f} Euro")
print(f"Sozialversicherung insgesamt:   {sozialversicherung_gesamt:10.2f} Euro")
print(f"Zu versteuerndes Einkommen:     {zu_versteuerndes_einkommen:10.2f} Euro")