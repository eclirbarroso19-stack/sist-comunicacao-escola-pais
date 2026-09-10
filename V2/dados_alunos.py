# V2 - sist-comunicacao-escola-pais / Fase 1
alunos = []

# Gera 30 alunos com lógica - igual sua sala de Jutaí
for i in range(1, 31):
    aluno = {
        "id": i,
        "nome": f"Aluno {i}",
        "turma": "3A",
        "faltas": i % 5,  # 0 a 4 faltas só pra teste
        "status": "OK" if (i % 5) < 3 else "Alerta"
    }
    alunos.append(aluno)

# Desafio da Fase 1: conta quantos estão em Alerta
alertas = 0
for aluno in alunos:
    if aluno["status"] == "Alerta":
        alertas += 1
        print(f"ALERTA: {aluno['nome']} - {aluno['faltas']} faltas")

print(f"\nTotal: {len(alunos)} alunos | {alertas} precisam de mensagem para os pais")
