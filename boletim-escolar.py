print("""
      -----------------------------------------
                    BOLETIM ESCOLAR          
          ESCOLA ESTADUAL PROFESSOR OLIVEIRA 
      -----------------------------------------
""")

import datetime
aluno = str(input("Nome do Aluno(a): "))
turma = str(input("Turma: "))

data = datetime.date.today()
data_formatada = print("Data de Emissão: {}".format(data.strftime("%d/%m/%Y")))
ano = int(input("Ano letivo: "))

print("\n-----LANÇAMENTO DE NOTAS BIMESTRAIS-----\n")

bimestre = int(input("Informe o número do bimestre para inserir as notas: "))

# Lingua Portuguesa
print("\nLíngua Portuguesa\n")
n1 = float(input("Atividades no caderno: "))
n2 = float(input("Trabalho individual: "))
n3 = float(input("Trabalho em grupo: "))
n4 = float(input("Prova: "))

nota = n1 + n2 + n3 + n4
print("\nSua nota é: {:.1f}".format(nota))

if nota >= 6:
    print("Situação: APROVADO")
else:
    print("Situação: Está em RECUPERAÇÃO")

# Matemática
print("\nMatemática\n")
n1 = float(input("Atividades no caderno: "))
n2 = float(input("Trabalho individual: "))
n3 = float(input("Trabalho em grupo: "))
n4 = float(input("Prova: "))

nota = n1 + n2 + n3 + n4
print("\nSua nota é: {:.1f}".format(nota))

if nota >= 6:
    print("Situação: APROVADO")
else:
    print("Situação: Está em RECUPERAÇÃO")

# Ciências
print("\nCiências\n")
n1 = float(input("Atividades no caderno: "))
n2 = float(input("Trabalho individual: "))
n3 = float(input("Trabalho em grupo: "))
n4 = float(input("Prova: "))

nota = n1 + n2 + n3 + n4
print("\nSua nota é: {:.1f}".format(nota))

if nota >= 6:
    print("Situação: APROVADO")
else:
    print("Situação: Está em RECUPERAÇÃO")

# História
print("\nHistória\n")
n1 = float(input("Atividades no caderno: "))
n2 = float(input("Trabalho individual: "))
n3 = float(input("Trabalho em grupo: "))
n4 = float(input("Prova: "))

nota = n1 + n2 + n3 + n4
print("\nSua nota é: {:.1f}".format(nota))

if nota >= 6:
    print("Situação: APROVADO")
else:
    print("Situação: Está em RECUPERAÇÃO")

# Geografia
print("\nGeografia\n")
n1 = float(input("Atividades no caderno: "))
n2 = float(input("Trabalho individual: "))
n3 = float(input("Trabalho em grupo: "))
n4 = float(input("Prova: "))

nota = n1 + n2 + n3 + n4
print("\nSua nota é: {:.1f}".format(nota))

if nota >= 6:
    print("Situação: APROVADO")
else:
    print("Situação: Está em RECUPERAÇÃO")

# Inglês
print("\nInglês\n")
n1 = float(input("Atividades no caderno: "))
n2 = float(input("Trabalho individual: "))
n3 = float(input("Trabalho em grupo: "))
n4 = float(input("Prova: "))

nota = n1 + n2 + n3 + n4
print("\nSua nota é: {:.1f}".format(nota))

if nota >= 6:
    print("Situação: APROVADO")
else:
    print("Situação: Está em RECUPERAÇÃO")

# Ed. Física
print("\nEducação Física\n")
n1 = float(input("Atividades no caderno: "))
n2 = float(input("Trabalho individual: "))
n3 = float(input("Trabalho em grupo: "))
n4 = float(input("Prova: "))

nota = n1 + n2 + n3 + n4
print("\nSua nota é: {:.1f}".format(nota))

if nota >= 6:
    print("Situação: APROVADO")
else:
    print("Situação: Está em RECUPERAÇÃO")

# Artes
print("\nArtes\n")
n1 = float(input("Atividades no caderno: "))
n2 = float(input("Trabalho individual: "))
n3 = float(input("Trabalho em grupo: "))
n4 = float(input("Prova: "))

nota = n1 + n2 + n3 + n4
print("\nSua nota é: {:.1f}".format(nota))

if nota >= 6:
    print("Situação: APROVADO")
else:
    print("Situação: Está em RECUPERAÇÃO")
