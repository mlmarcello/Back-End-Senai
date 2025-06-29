def calcular_desconto(idade, situacao, conhecimento, comunidade):
    if idade < 18:
        return 0
    desconto_total = 0

    # Situação profissional
    if situacao.lower() == "estudante":
        desconto_total += 10
    elif situacao.lower() == "desempregado":
        desconto_total += 15
    # conhecimento
    if conhecimento.lower() == "sim":
        desconto_total += 5
    # comunidade
    if comunidade.lower() == "sim":
        desconto_total += 20
    return desconto_total


print(
    "Bem-vindo ao sistema de verificação de elegibilidade para desconto em cursos de TI!"
)
nome = input("Digite seu nome: ")
print(f"Oi {nome}, vamos calcular seu desconto!")
input_idade = input("Digite a idade do aluno:")
idade = int(input_idade)
input_situacao = input(
    "Qual a situação profissional do aluno?(estudante, desempregado, empregado):"
)
input_conhecimento = input("O aluno possui conhecimento prévio em TI?(sim, não):")
input_comunidade = input("O aluno faz parte de alguma comunidade de TI?(sim, não):")

print(
    resultado := calcular_desconto(
        idade, input_situacao, input_conhecimento, input_comunidade
    )
)
desconto_final = calcular_desconto(
    idade, input_situacao, input_conhecimento, input_comunidade
)
print(f"O desconto total é de {desconto_final}%")
if desconto_final > 0:
    print(
        f"{nome}, você é elegível para um desconto de {desconto_final}% no curso de TI! venha se inscrever no nosso curso!"
    )
else:
    print(f"{nome}, você não é elegível para desconto no curso de TI, mas pode se inscrever normalmente.")
