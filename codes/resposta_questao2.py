def fibonacci_sequence(n):
    fib_sequence = [0, 1]
    while fib_sequence[-1] < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

def is_in_sequence(n, sequence):
    return n in sequence

# Definir número
while(True):
    try:
        num = int(input('Escolha um número para verificar se ele existe na sequência de Fibonacci: '))
        break
    except:
        print('\nDigite um número inteiro\n')

# Inicia a sequência até o número
sequence = fibonacci_sequence(num)

# Verifica se o número está na sequência
if is_in_sequence(num, sequence):
    print(f"O número {num} pertence à sequência de Fibonacci.")
else:
    print(f"O número {num} não pertence à sequência de Fibonacci.")
