import random

def main():
    michelangelo = {
      "name": "Michelangelo", 
      "defense": 10, 
      "attack": 10,
      "weapons": [
        {
          "name": "Nunchakus",
          "attack": 10,
          "defense": 3
        },
        {
          "name": "Shield",
          "attack": 1,
          "defense": 10
        }
      ]
    }
    donatello = {
      "name": "Donatello", 
      "defense": 5, 
      "attack": 15,
      "weapons": [
        {
          "name": "Wooden Stick",
          "attack": 10,
          "defense": 5
        },
        {
          "name": "Shield",
          "attack": 1,
          "defense": 10
        }
      ]
    }
    rafael = {
      "name": "Rafael", 
      "defense": 15, 
      "attack": 5,
      "weapons": [
        {
          "name": "Sai",
          "attack": 10,
          "defense": 2
        },
        {
          "name": "Shield",
          "attack": 1,
          "defense": 10
        }
      ]
    }
    leonardo = {
      "name": "Leonardo", 
      "defense": 7, 
      "attack": 12,
      "weapons": [
        {
          "name": "Katanas",
          "attack": 10,
          "defense": 7
        },
        {
          "name": "Shield",
          "attack": 1,
          "defense": 10
        }
      ]
    }
    
    turtles = [michelangelo, donatello, rafael, leonardo]
    choice = int(input("Escolha uma das tartarugas ninjas\n1 - Michelangelo,\n2 - Donatello,\n3 - Rafael,\n4 - Leonardo\n"))
    chosenTurtle = turtles.pop(choice - 1)
    choice = int(input("Escolha uma arma (1,2)"))
    chosenWeapon = chosenTurtle["weapons"][choice - 1]
    enemyTurtle = random.choice(turtles)
    enemyWeapon = random.choice(enemyTurtle["weapons"])
    print("Seu ataque é ", chosenTurtle["attack"], "(+", chosenWeapon["attack"], ")", sep="")
    print("Sua defesa é ", chosenTurtle["defense"], "(+", chosenWeapon["defense"], ")", sep="")

    print("O ataque do seu inimigo é ", enemyTurtle["attack"], "(+", enemyWeapon["attack"], ")", sep="")
    print("A defesa do seu inimigo é ", enemyTurtle["defense"], "(+", enemyWeapon["defense"], ")", sep="")

    yourRoundOutcome = chosenTurtle["attack"] + chosenWeapon["attack"] - enemyTurtle["defense"] - enemyWeapon["defense"]
    enemyRoundOutcome = enemyTurtle["attack"] + enemyWeapon["attack"] - chosenTurtle["defense"] - chosenWeapon["defense"]

    if (yourRoundOutcome > enemyRoundOutcome) :
      print("Você ganhou")
    elif(enemyRoundOutcome > yourRoundOutcome) :
      print("Você perdeu")
    else:
      print("Empate")

main()
    