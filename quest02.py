import math
valorUser = int(input("Digite um número inteiro: "))
def fibonacci(num):
    raiz1 = math.sqrt(5*num*num + 4)
    raiz2 = math.sqrt(5*num*num - 4)
    return raiz1.is_integer() or raiz2.is_integer()
teste = fibonacci(valorUser)
if teste == False:
    print(f'O número {valorUser} informado não faz parte da sequencia de Fibonacci!')
else:
    print(f'O número {valorUser} informado faz parte da sequencia de Fibonacci!')
