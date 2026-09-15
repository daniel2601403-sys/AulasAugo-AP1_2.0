titulo = "Quanto João gastou na livraria?"
texto_compra = "João comprou dois livros na Livraria, cada um por "
texto_desconto = " O desconto aplicado foi de: "
pergunta = "Quanto ele gastou no total?"
label_resposta = "O valor final da compra foi de: "

preco = 35.00
quantidade = 2
desconto = 10.00

valor_total = preco * quantidade
valor_final = valor_total - desconto

print(f"""
{titulo}
{texto_compra}R$ {preco:.2f}.{texto_desconto}R$ {desconto:.2f}
{pergunta}
{label_resposta}R$ {valor_final:.2f}
""")