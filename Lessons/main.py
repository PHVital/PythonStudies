nome = "Pedro Henrique Vital"
email = "joaofalso@gmail.com"

posicao = email.find("@")

separador = nome.find(" ")
nome.replace()

print(f"Usuario {nome[:separador]} cadastrado com sucesso com o provedor de email {email}")
print(f"Enviamos um link de confirmação para o email {email[0]}***{email[posicao:]}")