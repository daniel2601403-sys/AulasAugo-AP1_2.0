idade_minima = 18

# Primeiro perguntamos apenas a idade
idade = int(input("Qual a sua idade? "))

# Validamos a idade ANTES de perguntar sobre o ingresso
if idade < idade_minima:
    print("Acesso negado! Você não possui a idade mínima para acessar o evento.")
else:
    # Só chega aqui (e só pergunta o ingresso) se a idade for suficiente
    ingresso = input("Você tem o ingresso? (s/n): ")
    tem_ingresso = ingresso == "s"

    if tem_ingresso:
        print("Acesso liberado! Divirta-se com o nosso evento!")
    else:
        print("Acesso negado! Você não possui o ingresso para entrar no evento.")