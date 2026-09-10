# sistema-comunicacao-escola-pais
Sistema para controle de presença de pais e encaminhamento para Conselho Tutelar - V1 em Google Sheets
# Sistema. Comunicação Escola-Pais via WhatsApp

Projeto desenvolvido para resolver um problema real da educação municipal de Jutaí-AM: pais que não comparecem às convocações da escola.

> Desenvolvido por Eclir - Estudante de ADS em Manaus, focado em soluções de baixo custo para o interior do Amazonas.

### O Problema
Secretarias de educação perdem horas ligando e ainda não têm relatório para encaminhar ao Conselho Tutelar. Tudo fica em caderno ou planilha solta.

### A Solução (V1)
Sistema em Google Sheets com 3 abas integradas que funciona como um banco de dados simples:

**Aba 1 - Série/turma:** Cadastro de alunos com listas suspensas e formatação condicional por cor.
- Status Pai/Mãe: Ausente / Presente
- Status Encaminhamento: Aguardando pai, Em Apoio Pedagógico, Encaminhado Cons. Tutelar, Resolvido
- Órgão: Apoio, Conselho, Escola, CREAS

**Aba 2 - Comunicados Prontos:** Biblioteca de 5 mensagens padrão para WhatsApp, separadas por nível de criticidade.

**Aba 3 - Dashboard:** Painel automático que conta com `CONT.SE` e `CONT.VALORES`, gerando relatório para o Secretário.

### Tecnologias e Conceitos Aplicados
- Google Sheets (Validação de Dados, Formatação Condicional, Cores Alternadas)
- Lógica de Programação: `CONT.SE` = `if` em Python, cada linha = um `dicionário`
- Pensamento de Produto: V1 entregável, focada em resolver a dor principal

### Próximos Passos (V2)
- Migrar para Python com dicionários e salvar em .csv
- Gerador de PDF automático dos comunicados
- Bot simples de WhatsApp

### Prints do Sistema
[<img width="1896" height="811" alt="image" src="https://github.com/user-attachments/assets/e5768fa6-1a56-4fd0-a850-24d89761c62c" />
]
[<img width="1917" height="632" alt="image" src="https://github.com/user-attachments/assets/1908da30-cd82-4f7d-b2c8-4ffea5cbd63a" />
]
[<img width="1910" height="822" alt="image" src="https://github.com/user-attachments/assets/712487d2-8a92-4668-8d50-2b6ddc029c50" />
]
