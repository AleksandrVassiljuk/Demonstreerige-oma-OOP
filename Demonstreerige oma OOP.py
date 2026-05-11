class Ulesanne:
    def __init__(self, nimi):
        self.nimi = nimi


class ToDoList:
    def __init__(self):
        self.ulesanded = []

    def lisa(self, nimi):
        self.ulesanded.append(Ulesanne(nimi))
        print("Ülesanne lisatud")

    def kuva(self):
        if len(self.ulesanded) == 0:
            print("Ülesandeid pole")
        else:
            for i, u in enumerate(self.ulesanded, start=1):
                print(i, u.nimi)


todo = ToDoList()

while True:
    print("\n1 Lisa")
    print("2 Kuva")
    print("3 Välju")

    valik = input("Valik: ")

    if valik == "1":
        nimi = input("Sisesta ülesanne: ")
        todo.lisa(nimi)

    elif valik == "2":
        todo.kuva()

    elif valik == "3":
        print("Programm lõpetati")
        break

    else:
        print("Vale valik")