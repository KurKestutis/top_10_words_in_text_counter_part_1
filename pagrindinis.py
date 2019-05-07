from paste5 import *

langas = Tk()
langas.title("Dažniausiai tekste panaudotų žodžių skaičiuoklė (Top - 10) KK X 4.0")
langas.iconbitmap(r'top_X4.ico')
# duomenys = ""
x = []

def sudet_du_listus(a,b):
    print(a+b)



# Pasiimti duomenis iš bokso
def pasiimti():
    # global duomenys
    duomenys = boksas.get("1.0", "end-1c")
    print("Štai kas paiimta iš bokso: " + str(duomenys))
    global x
    x = duomenys.split()
    y=['a', 'b', 'c']
    sudet_du_listus(x, y)

    print(x)
    return x

"""-----------Laukai/Mygtukai/Užrašai----------"""
uzrasas1 = Label(langas, text="Įveskite tekstą:")
boksas = Text(langas, height=20, width=70)
mygtukas_pateikti = Button(langas, text="          Pateikti          ", command=lambda: pasiimti())
#command=lambda: pasiimti() >>> just means do this when i press the button


# mygtukas_pateikti.bind("<Button-1>", pasiimti)
# mygtukas_pateikti=Button(langas, command=lambda: pasiimti())
# mygtukas1.bind("<Button-1>", spausdinti) PRISIMINIMUI
# laukas1.bind("<Return>", spausdinti)

parasteWN = Label(langas, text="   ")
parasteEN = Label(langas, text="   ")
parasteWS = Label(langas, text="   ")
parasteEN = Label(langas, text="   ")
perskyrimas = Label(langas, text="   ")

"""-------------------PARAŠTĖS--------------------"""
parasteWN.grid(row=0, column=0)
parasteEN.grid(row=0, column=7)
parasteWS.grid(row=32, column=0)
parasteEN.grid(row=32, column=7)
perskyrimas.grid(row=15, column=0)

"""-------------FUNKCIJŲ PALEIDIMAS---------------"""
boksas.grid(row=2, column=1, columnspan=6, sticky=W)

uzrasas1.grid(row=1, column=1, sticky=W)
mygtukas_pateikti.grid(row=16, column=6, sticky=E)

"""--------------------POPUO MENU----------------"""

boksas.bind('<Button-3>', rClicker, add='')

'''-------------SCCROLLBAR--------------'''


print(str(x) + " va sitas yra x'sas")

# def ikso_funkcija():
#     x

langas.mainloop()
