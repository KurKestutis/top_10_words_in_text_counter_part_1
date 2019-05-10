pateikta = ("vienas, du, du, trys, trys, trys, keturi, keturi, keturi, keturi, "
            "penki, penki, penki, penki, penki, šeši, šeši, šeši, šeši, šeši, "
            "šeši, septyni, septyni, septyni, septyni, septyni, septyni, "
            "septyni, aštuoni, aštuoni, aštuoni, aštuoni, aštuoni, aštuoni, aštuoni, aštuoni,")

# konvertuoti viską į mažąsias raides ir panaikinti skirybos ženklus ir išplitinti į listą
pateikta = pateikta.lower()
for skiryba in [',' , ':' , '.' , '"' , '!' , '?' , '–' , '(' , ')' , '\n' , '\r']:
    pateikta = pateikta.replace(skiryba, '')
visi_zodziai = pateikta.split(" ")
print(visi_zodziai)

#suskaiciuoti
zodziu_skaicius = {}
for zodis in visi_zodziai:
    suskaiciuota_dabar = zodziu_skaicius.get(zodis, 0)
    suskaiciuota_dabar_update = suskaiciuota_dabar + 1
    zodziu_skaicius[zodis] = suskaiciuota_dabar_update
print(zodziu_skaicius)

