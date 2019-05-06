from paste5 import *

langas = Tk()
langas.title("Dažniausiai tekste panaudotų žodžių skaičiuoklė (Top - 10) KK X 4.0")
langas.iconbitmap(r'top_X4.ico')

# def Pasiimti duomenis iš bokso
def pasiimti(event):
    print(boksas.get())
    duomenys = boksas.get()
    print("Štai kas paiimta iš bokso: " + str(duomenys))

"""-----------Laukai/Mygtukai/Užrašai----------"""

# boksas = Text(langas, height=20, width=70)
boksas = Entry(langas)


uzrasas1 = Label(langas, text="Įveskite tekstą:")
mygtukas_pateikti = Button(langas, text="          Pateikti          ")
mygtukas_pateikti.bind("<Button-1>", pasiimti)
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


'''-------------SCCROLLBAR EXAMPLES--------------'''


# scroll = Scrollbar(boksas)
# scroll.grid()
# scroll.grid(row=3, column=1, columnspan=6, sticky=E)
# row=2, column=1, columnspan=6, sticky=W

# scroll.config(command=)



langas.mainloop()
