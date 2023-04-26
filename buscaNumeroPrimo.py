

def acha_numero_primo(numeroInicial,numeroFinal):
    index = numeroInicial
    totalPrimo = 0
    while index < numeroFinal:
        i = 2
        while i < index:
            if i == index - 1:
                print(f"o numero {index} eh primo")
                totalPrimo += 1
            if index % i == 0:
                break
            else:
                i += 1
        index += 1
    print(f"o total de numeros primos encontrados foi de {totalPrimo},"
          f" sendo eles %{100 * totalPrimo/(numeroFinal - numeroInicial)}")

acha_numero_primo(0,1000)