import random

class QA:
    def __init__(self, vprasanje, pravilen_odgovor, drugi_odgovori):
        self.vprasanje = vprasanje
        self.pravilen_odgovor = pravilen_odgovor
        self.drugi_odgovori = drugi_odgovori

qaList = [QA("Kdo postane Darth Vader?", "Anakin Skywalker", ["Luke Skywalker", "nihče"]),
QA("Kje živijo wookies?", "Na planetu Kashyyyk", ["Na planetu Tatooine", "na planetu Bracca"]),
QA("Koliko Star Wars filmov obstaja?", "9", ["6", "3"]),
QA("Koliko sedežev ima Jedi Council?", "12", ["15", "10"]),
QA("Kakšne barve je lightsaber od Mace Winduja?", "vijolične", ["modre", "zelene"]),
QA("Kako se imenuje ladja Bobe Fett?","Slave 1", ["Slave 2", "Slave 3"]),
QA("Na katerem planetu so izdelovali klone?", "Kamino", ["Mustafar", "Dantooine"]),
QA("Kateri dan je Wookie Life day??", "17. november", ["25. december", "1. januar"]),
QA("Kdo je zgradil C3PO?", "Anakin Skywalker", ["Obi-Wan Kenobi", "Luke Skywalker"]),
QA("Kako je bilo ime sinu od Leie Organa in Han Sola?", "Ben Solo", ["Luke Solo", "nista imela sina"])]

print("Navodila: Kot odgovor na vsako vprašanje vnesite številko. Vsako vprašanje ima kvečjemu en odgovor.")
print("May the Force be with you."'\n')

count = 0
random.shuffle(qaList)

for qaItem in qaList:
    print(qaItem.vprasanje)
    print("Možni odgovori so:"'\n')
    mozni = qaItem.drugi_odgovori + [qaItem.pravilen_odgovor]
    random.shuffle(mozni)
    count = 0

    while count < len(mozni):
        print(str(count+1) + ": " + mozni[count])
        count += 1
    print("Prosim vnesite število svojega odgovora:")
    odgovor = str(input())
    while not str(odgovor).isdigit():
        print("To ni število, prosim vnesite veljaven odgovor:"'\n')
        odgovor = input()
    odgovor = int(odgovor)
    while not (odgovor > 0 and odgovor <= len(mozni)):
        print("To število ni ustrezno nobenemu odgovoru. Prosim, vnesite veljavno število:"'\n')
        odgovor = int(input())
    
    if mozni[odgovor - 1] == qaItem.pravilen_odgovor:
        print("Pravilno ste odgovorilo na vprašanje!"'\n')
        count += 1
    else:
        print("Napačen odgovor."'\n')
        print("Pravilen odgovor je bil:" + qaItem.pravilen_odgovor)
        print("")

print("Pravilno ste dgovorili na " + str(count) + " od " + str(len(qaList)) + " vprašanj.")
