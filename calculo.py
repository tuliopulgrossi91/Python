# TULIO PULGROSSI - 29/08/18
import random

# CRIANDO VARIAVEIS
contador, acertos, erros, aleatorio = 0, 0, 0, 0

# CRIANDO LISTAS
operacao, dificuldade = ['0 - Somar', '1 - Subtrair', '2 - Multiplicar', '3 - Dividir'], ['0 - Facil', '1 - Medio', '2 - Dificil']

# JOGO DAS OPERAÇÕES - RESPONDER 10 QUESTÕES COM NUMEROS ALEATORIOS E AO FINAL EXIBE QUANTOS ACERTOS E ERROS O JOGADOR TEVE.

print('\nOperações disponiveis: \n')

for o in operacao:  # PERCORRER LISTA DE OPERAÇÕES
    print(o, '\n')

escolha1 = int(input('Escolha operação: '))  # RECEBER VALOR ESCOLHIDO (0, 1, 2, 3)

if escolha1 == 0 or escolha1 == 1 or escolha1 == 2 or escolha1 == 3:
    print('\nAgora escolha a dificuldade: \n')
else:
    escolha1 = int(input('Escolha operação: '))  # RECEBER VALOR ESCOLHIDO (0, 1, 2, 3)

for d in dificuldade:  # PERCORRER LISTA DE DIFICULDADE
    print(d, '\n')

escolha2 = int(input('Escolha dificuldade: '))  # RECEBENDO VALOR ESCOLHIDO (0, 1, 2)

if escolha2 == 0 or escolha2 == 1 or escolha2 == 2:

    while contador < 10:
        if escolha1 == 0 and escolha2 == 0:  # VERIFICANDO NIVEL SOMAR (FACIL)
            aleatorio = 11
            valor1 = random.randrange(0, aleatorio)
            valor2 = random.randrange(0, aleatorio)
            print('\n'+'Questão '+str(contador)+': '+str(valor1)+' + '+str(valor2))
            r = float(input('Resultado: '))

            if r == float(valor1 + valor2):
                acertos += 1
            else:
                erros += 1

            contador += 1

        elif escolha1 == 0 and escolha2 == 1:   # VERIFICANDO NIVEL SOMAR (MEDIO)
            aleatorio = 101
            valor1 = random.randrange(0, aleatorio)
            valor2 = random.randrange(0, aleatorio)
            print('\n'+'Questão '+str(contador)+': '+str(valor1)+' + '+str(valor2))
            r = float(input('Resultado: '))

            if r == float(valor1 + valor2):
                acertos += 1
            else:
                erros += 1

            contador += 1

        elif escolha1 == 0 and escolha2 == 2:   # VERIFICANDO NIVEL SOMAR (DIFICIL)
            aleatorio = 1001
            valor1 = random.randrange(0, aleatorio)
            valor2 = random.randrange(0, aleatorio)
            print('\n' + 'Questão '+str(contador)+': '+str(valor1)+' + '+str(valor2))
            r = float(input('Resultado: '))

            if r == float(valor1 + valor2):
                acertos += 1
            else:
                erros += 1

            contador += 1

        elif escolha1 == 1 and escolha2 == 0:  # VERIFICANDO NIVEL SUBTRAIR (FACIL)
            aleatorio = 11
            valor1 = random.randrange(0, aleatorio)
            valor2 = random.randrange(0, aleatorio)
            print('\n'+'Questão '+str(contador)+': '+str(valor1)+' - '+str(valor2))
            r = float(input('Resultado: '))

            if r == float(valor1 - valor2):
                acertos += 1
            else:
                erros += 1

            contador += 1

        elif escolha1 == 1 and escolha2 == 1:   # VERIFICANDO NIVEL SUBTRAIR (MEDIO)
            aleatorio = 101
            valor1 = random.randrange(0, aleatorio)
            valor2 = random.randrange(0, aleatorio)
            print('\n'+'Questão'+str(contador)+': '+str(valor1)+' - '+str(valor2))
            r = float(input('Resultado: '))

            if r == float(valor1 - valor2):
                acertos += 1
            else:
                erros += 1

            contador += 1

        elif escolha1 == 1 and escolha2 == 2:   # VERIFICANDO NIVEL SUBTRAIR (DIFICIL)
            aleatorio = 1001
            valor1 = random.randrange(0, aleatorio)
            valor2 = random.randrange(0, aleatorio)
            print('\n'+'Questão '+str(contador)+': '+str(valor1)+' - '+str(valor2))
            r = float(input('Resultado: '))

            if r == float(valor1 - valor2):
                acertos += 1
            else:
                erros += 1

            contador += 1

        elif escolha1 == 2 and escolha2 == 0:   # VERIFICANDO NIVEL MULTIPLICAR (FACIL)
            aleatorio = 11
            valor1 = random.randrange(0, aleatorio)
            valor2 = random.randrange(0, aleatorio)
            print('\n'+'Questão '+str(contador)+': '+str(valor1)+' x '+str(valor2))
            r = float(input('Resultado: '))

            if r == float(valor1 * valor2):
                acertos += 1
            else:
                erros += 1

            contador += 1

        elif escolha1 == 2 and escolha2 == 1:   # VERIFICANDO NIVEL MULTIPLICAR (MEDIO)
            aleatorio = 101
            valor1 = random.randrange(0, aleatorio)
            valor2 = random.randrange(0, aleatorio)
            print('\n'+'Questão '+str(contador)+': '+str(valor1)+' x '+str(valor2))
            r = float(input('Resultado: '))

            if r == float(valor1 * valor2):
                acertos += 1
            else:
                erros += 1

            contador += 1

        elif escolha1 == 2 and escolha2 == 2:   # VERIFICANDO NIVEL MULTIPLICAR (DIFICIL)
            aleatorio = 1001
            valor1 = random.randrange(0, aleatorio)
            valor2 = random.randrange(0, aleatorio)
            print('\n' +'Questão '+str(contador)+': '+str(valor1)+' x '+str(valor2))
            r = float(input('Resultado: '))

            if r == float(valor1 * valor2):
                acertos += 1
            else:
                erros += 1

            contador += 1

        elif escolha1 == 3 and escolha2 == 0:   # VERIFICANDO NIVEL DIVIDIR (FACIL)
            aleatorio = 11
            valor1 = random.randrange(0, aleatorio)
            valor2 = random.randrange(0, aleatorio)
            print('\n'+'Questão '+str(contador)+': '+str(valor1)+' / '+str(valor2))
            r = float(input('Resultado: '))

            if r == float(valor1 / valor2):
                acertos += 1
            else:
                erros += 1

            contador += 1

        elif escolha1 == 3 and escolha2 == 1:   # VERIFICANDO NIVEL DIVIDIR (MEDIO)
            aleatorio = 101
            valor1 = random.randrange(0, aleatorio)
            valor2 = random.randrange(0, aleatorio)
            print('\n'+'Questão '+str(contador)+': '+str(valor1)+' / '+str(valor2))
            r = float(input('Resultado: '))

            if r == float(valor1 / valor2):
                acertos += 1
            else:
                erros += 1

            contador += 1

        elif escolha1 == 3 and escolha2 == 2:   # VERIFICANDO NIVEL DIVIDIR (DIFICIL)
            aleatorio = 1001
            valor1 = random.randrange(0, aleatorio)
            valor2 = random.randrange(0, aleatorio)
            print('\n'+'Questão '+str(contador)+': '+str(valor1)+' / '+str(valor2))
            r = float(input('Resultado: '))

            if r == float(valor1 / valor2):
                acertos += 1
            else:
                erros += 1

            contador += 1
    else:
        print('\n'+'Acertos: '+str(acertos)+'\n')
        print('Erros: '+str(erros)+'\n')