def verifica_se_numero_eh_primo(numero):
    divisor = 2
    if numero <= 1:
        return False
    if numero == 2:
        return True
    while divisor < numero:
        if divisor == numero - 1:
            return True
        if numero % divisor == 0:
            return False
        else:
            divisor += 1

def verifica_primos_fibonacci(numero_maximo):
    totalPrimoFibonacci = 0
    totalFibonacci = 0
    numeroUm = 1
    numeroDois = 1
    numeroTress = 1
    while numeroTress < numero_maximo:
    #while True:
        if verifica_se_numero_eh_primo(numeroTress):
            totalPrimoFibonacci += 1
            print(f"o numero {numeroTress} participa da sequencia fibonacci e eh"
                  f" primo ate agora achamos {totalPrimoFibonacci} numeros que pertencem a ambos os grupos\n"
                  f" numeros fibonacci percorridos {totalFibonacci}")
        totalFibonacci += 1
        numeroUm = numeroDois
        numeroDois = numeroTress
        numeroTress = numeroUm + numeroDois

verifica_primos_fibonacci(1000000000000)