import Forca
import Adivinhacao


print("~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.")
print("~.~. Escolha o seu JOGO!!! .~.~.~.~.~.")
print("~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.")




print("(1) - Adivinhação) (2) - Forca")

jogo = int(input("Qual Jogo?"))

if(jogo == 1):
    print("Jogar Adivinhação")
    Adivinhacao.jogar()

elif(jogo == 2):

    print("Jogar Forca")
    Forca.jogar()