def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total

print(add(1, 2, 3, 4))

# com o argumento arbitrário *args, eu posso modificar a quantidade de argumentos sem prejudicar a função