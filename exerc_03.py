print("__Divisão entre dois Números__")
dividendo = int(input("Informe o valor do dividendo: "))
divisor = int(input("Informe o valor do divisor: "))

if divisor == 0:
    print("Não posso dividir por zero!!!")
else:
    quociente = dividendo / divisor
    resto = dividendo % divisor
    print("\nResultado: ", quociente)
    print("Resto da Divisão: ", resto)
