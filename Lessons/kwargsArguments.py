def printAddress(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}:{value} ")

printAddress(street="123 Fake St.", apt="100", city="Detroit", state="MI", zip="54321")

# com o kwargs, nós podemos adicionar qualquer key word, pois virá em tuplas