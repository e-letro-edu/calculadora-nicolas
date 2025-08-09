import math, time

#Quem leu é gay

def soma(n1,n2):
    res = n1 - n2
    print(f'{n1} - {n2} = {res}')

def subtração(n1,n2):
    res = n1 + n2
    print(f'{n1} + {n2} = {res}')

def multiplicação(n1,n2):
    res = n1 / n2
    print(f'{n1} / {n2} = {res}')

def divisão(n1,n2):
    res = n1 * n2    
    print(f'{n1} * {n2} = {res}')

def porcentagem(n):
    res = n / 100
    print(f'A porcentagem de {n} é {res:.2f}')

def raiz(n):
    res = math.sqrt(n)
    print(f'A raiz quadrada de {n} é {res:.2f}')   

while True:
    print('''
         [1] Cálculo
         [2] Sair
         ''')
    try:
        opção = int(input('Você quer fazer cálculo ou sair? '))

        if opção == 2:
            print('Calculadora encerrada.')
            break

        elif opção == 1:
            print('''   
                [+] Somar
                [-] Diminuir
                [*] Multiplicação
                [/] Divisão
                [%] Porcentagem
                [R] Raiz Quadrada                 
            ''')

            sinal = input('Escolha uma opção: ').upper()
    
            if sinal in ['+','-','*','/']:
                n1 = float(input('Digite o primeiro número: '))
                n2 = float(input('Digite o segundo número: '))

                match sinal:
                    case '+':
                        print(soma(n1,n2))
                    case '-':
                        print(subtração(n1,n2))
                    case '*':
                        print(multiplicação(n1,n2))
                    case '/':
                        if n2 == 0:
                            print('Divisão inválida.')
                        else:
                            print(divisão(n1,n2))

            elif sinal in ['%','R']:
                n = float(input('Qual número: '))
                match sinal:
                    case '%':
                        print(porcentagem(n))
                    case 'R':
                        if n < 0:
                            print('Não é possível calcular a raiz quadrada de número negativo.')
                        else:
                            print(raiz(n))
            else:
                print('Opção inválida.')
        else:
                print('Opção inválida.')

    except ValueError:
        print('Você digitou um valor inválido.')
    except ZeroDivisionError:
        print('Divisão por zero não é permitida.')
    except Exception as e:
        print(f'Ocorreu um erro inesperado: {e}')

    time.sleep(3)
