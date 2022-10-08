import random

def jogar():
    user = input("Qual sua escolha: 'r' para pedra, 'p' para papel, 't' para tesoura :")
    computer = random.choice(['r','p','t'])

    if user == computer:
        return 'It\'s a tie '

    if vencer(user,computer):
        return 'You won!!'
    
    return 'You lost!'

def vencer (jogador,oponente):
    if (jogador == 'r' and oponente == 't') or (jogador == 'p' and oponente == 'r') or (jogador == 't' and oponente == 'p'):
        return True

print(jogar())