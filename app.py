import os

player = {
    "nome": "Python",
    "x": 0, 
    "y": 0
}

def andar (direcao):
    if direcao == "d":
        player["x"] += 1
    if direcao == "a":
        player["x"] -= 1
    if direcao == "w":
        player["y"] -= 1
    if direcao == "s":
        player["y"] += 1

while True:
    os.system("cls")

    print("___________________________")
    for y in range(5):
        print("\n")
        for x in range (10): 
            if player["x"] == x and player["y"] == y:
                print("🤺", end="")
            else:
                print("🟨", end="")
    print("_______________________")

    direcao = input("Próxima direção (a,w,s,d): ")
    andar(direcao)
    if direcao == "sair":
        break