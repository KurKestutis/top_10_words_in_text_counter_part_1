pateikta = ("vienas, du, du, trys, trys, trys, keturi, keturi, keturi, keturi, "
            "penki, penki, penki, penki, penki, šeši, šeši, šeši, šeši, šeši, "
            "šeši, septyni, septyni, septyni, septyni, septyni, septyni, "
            "septyni, aštuoni, aštuoni, aštuoni, aštuoni, aštuoni, aštuoni, aštuoni, aštuoni, devyni, devyni, devyni, devyni, devyni, devyni, devyni, devyni, devyni, "
            "dešimt, dešimt, dešimt, dešimt, dešimt, dešimt, dešimt, dešimt, dešimt, dešimt, ")

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


"""-----------SORTINIMAS---------------"""
import collections
zodis = collections.namedtuple('zodis', 'score name')
d = zodziu_skaicius
# d = {'vienas': 1, 'du': 2, 'trys': 3, 'keturi': 4, 'penki': 5, 'šeši': 6, 'septyni': 7, 'aštuoni': 8}
worst = sorted(zodis(v,k) for (k,v) in d.items())
best = sorted([zodis(v,k) for (k,v) in d.items()], reverse=True)
print(best[0])
print(best[0].name)
print(best[0].score)




