#

matricula1 = 2026001
nome = "Ana Silva"
telefone = "9999-8888"

aluno = {
    "matricula" : 2026001,
    "nome": "Ana silva",
    "telefone": "9999-8888"
}

print(aluno)

contato = {
    "@camila": "Camila",
    "@paola": "Paola",
    "@sheron": "Sheron",
    "@bruna": "Bruna",
    "@joao": "joão"
}

print(contato)
print(type(contato))

#acesso direito ao dicionario
print(contato("@camila"))

#acesso seguro com get()
print(contato.get("@paola"))
print(contato.get("@inexistente"))
print(contato.get("@inexistente"))
print(contato.get("@inexistente", "Não encontrado"))

print("Original: ", contato) #acessando a liata original

#add novo elemento
contato["@giovanna"] = "Giovanna"
print("Após add: ", contato)

#atualiza elementos existente
contato["@paola"] = "paola Oliveira"
print("Após add: ", contato)

contato.update(
    {
        "@bruna": "Bruna Marquezine",
"@camila": "Camila Q."
    }
)

print("Após atualização: ", contato)

#pop: Remova e retorne
removido = contato.pop("@sheron")
print(f"Removido: {removido}")
print("Após o pop:", contato)

#del remove sem retornar
del contato["@paola"]
print("Após o del: ", contato)

#clear esvazia tudo
copia = dict(contato)
contato.clear()
print("Após clear: ", contato)
print("Cópia", copia)

print("Número de contato: ", len(contato))

contato.pop("@camila")
print("Após remover um:")

#verificar existência
if "@joao" in contato:
    print("Existe")

if "@inexistente" in contato:
    print("Existe")
else:
    print("Não existe")
#Dicionario vacio
vazio = {}

#Diconario com tipos mistos

dados = {
    "nome": "João",
    "idade": 25,
    "altura": 1.70,
    "ativo": True
}

print

("Vazio: ", vazio)
print("Vazio:", dados)