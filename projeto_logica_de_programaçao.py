''' 
       PROJETO GERAÇAO FUTURO JOVENS TALENTOS 
           ADA & RENAULT 

NOME = Alessandro brasil 

'''



# Dicionário inicial de estudantes
escola1 = {
    "12345": {
        "nome": "Maria Luiza",
        "matricula": "12345",
        "idade": "15",
        "serie": "8ºB",
        "boletim": {
            "matematica": 6.8,
            "portugues": 8.9,
            "geografia": 7.8,
            "ciencia": 9.0,
            "educacao_fisica": 10
        }
    },
    "12346": {
        "nome": "Pedro Henrique",
        "matricula": "12346",
        "idade": "17",
        "serie": "7ºB",
        "boletim": {
            "matematica": 3.8,
            "portugues": 9.9,
            "geografia": 8.8,
            "ciencia": 9.3,
            "educacao_fisica": 10
        }
    },
    "12347": {
        "nome": "Luiz Carlos",
        "matricula": "12347",
        "idade": "14",
        "serie": "6ºA",
        "boletim": {
            "matematica": 5.5,
            "portugues": 6.9,
            "geografia": 9.8,
            "ciencia": 8.1,
            "educacao_fisica": 10
        }
    },
    "12348": {
        "nome": "Jose Fernandes",
        "matricula": "12348",
        "idade": "12",
        "serie": "5ºC",
        "boletim": {
            "matematica": 7.8,
            "portugues": 4.9,
            "geografia": 8.8,
            "ciencia": 9.5,
            "educacao_fisica": 6.0
        }
    }
}

def media(boletim): # Define a função 'media', que recebe um dicionário 'boletim' contendo as notas de um aluno
    total = 0  # Inicializa a soma total das notas
    quantidade = 0  # Inicializa o contador de notas válidas

    for nota in boletim.values():  # Itera sobre as notas no boletim
        if nota is not None:  # Verifica se a nota não é None
            total += nota  # Adiciona a nota ao total
            quantidade += 1  # Incrementa a quantidade de notas válidas

    if quantidade > 0:  # Verifica se há notas para calcular a média
        media_final = total / quantidade  # Calcula a média
        status = "Aprovado" if media_final >= 6.0 else "Reprovado"  # Define o status baseado na média
        return media_final, status  # Retorna a média e o status
    else:
        return 0, "Sem notas"  # Retorna 0 e uma mensagem se não houver notas

def calcular_media_geral():  # Define a função 'calcular_media_geral', que irá calcular a média e status de todos os alunos cadastrados
    for matricula, dados in escola1.items():  # Itera sobre cada aluno na escola
        boletim = dados["boletim"]  # Acessa o boletim do aluno
        dados["media"], dados["status"] = media(boletim)  # Calcula a média e status do aluno

def coletar_dados(): # Define a função 'coletar_dados', que é responsável por capturar as informações dos alunos e armazená-las
    while True:  # Inicia um loop para coletar dados dos alunos
        matricula = input("Digite a matrícula do aluno (ou 'sair' para encerrar): ")  # Solicita a matrícula
        if matricula.lower() == 'sair':  # Verifica se o usuário deseja sair
            break  # Sai do loop
        if matricula in escola1:  # Verifica se a matrícula já está cadastrada
            print("Matrícula já cadastrada. Tente novamente.")  # Informa que a matrícula existe
            continue  # Volta ao início do loop

        adicionar_aluno(matricula)  # Chama a função para adicionar um novo aluno

def adicionar_aluno(matricula): # Define a função 'adicionar_aluno', que recebe a matrícula de um aluno e coleta suas informações para registrá-lo
    aluno = {}  # Cria um dicionário para armazenar os dados do aluno
    aluno["nome"] = input("Digite o nome do aluno: ").title()  # Solicita e formata o nome do aluno
    aluno["matricula"] = matricula  # Armazena a matrícula do aluno
    aluno["idade"] = input("Digite a idade do aluno: ")  # Solicita a idade do aluno
    aluno["serie"] = input("Digite a série do aluno: ")  # Solicita a série do aluno

    # Criando o dicionário boletim
    boletim = {
        "matematica": None,  # Inicializa a nota de matemática como None
        "portugues": None,  # Inicializa a nota de português como None
        "geografia": None,  # Inicializa a nota de geografia como None
        "ciencia": None,  # Inicializa a nota de ciências como None
        "educacao_fisica": None,  # Inicializa a nota de educação física como None
    }
    aluno["boletim"] = boletim  # Adiciona o boletim ao dicionário do aluno

    # Adicionando as notas
    adicionar_notas(boletim)  # Chama a função para adicionar notas ao boletim

    # Calculando a média e status
    resultado, status = media(boletim)  # Calcula a média e status com a função media

    # Adiciona os dados do aluno ao dicionário escola1
    aluno["media"] = resultado  # Armazena a média calculada
    aluno["status"] = status  # Armazena o status do aluno
    escola1[matricula] = aluno  # Adiciona o aluno ao dicionário escola1
    print(f"\nAluno {aluno['nome']} adicionado com sucesso!")  # Informa que o aluno foi adicionado

def adicionar_notas(boletim):  # Define a função 'adicionar_notas', que recebe um dicionário 'boletim' e permite ao usuário inserir as notas para cada matéria
    for materia in boletim.keys():  # Itera sobre as matérias do boletim
        while True:  # Inicia um loop para garantir entrada válida
            try:
                nota = float(input(f"Digite a nota para {materia.title()} (0 a 10): "))  # Solicita a nota
                if 0 <= nota <= 10:  # Verifica se a nota está no intervalo válido
                    boletim[materia] = nota  # Armazena a nota na matéria correspondente
                    break  # Sai do loop se a nota for válida
                else:
                    print("A nota deve ser entre 0 e 10. Tente novamente.")  # Informa intervalo inválido
            except ValueError:  # Captura erro se a entrada não for um número
                print("Entrada inválida. Digite um número.")  # Informa que a entrada foi inválida

def acessar_estudante(matricula): # Define a função 'acessar_estudante', que recebe a matrícula de um aluno e exibe suas informações detalhadas, como nome, idade e boletim
    estudante = escola1.get(matricula)  # Busca o aluno pelo matrícula
    if estudante:  # Verifica se o aluno foi encontrado
        # Acessando os dados do estudante
        nome = estudante["nome"]  # Obtém o nome do aluno
        idade = estudante["idade"]  # Obtém a idade do aluno
        serie = estudante["serie"]  # Obtém a série do aluno
        boletim = estudante["boletim"]  # Obtém o boletim do aluno

        # Imprimindo os dados
        print(f"\nNome: {nome}")  # Imprime o nome do aluno
        print(f"Matrícula: {matricula}")  # Imprime a matrícula do aluno
        print(f"Idade: {idade}")  # Imprime a idade do aluno
        print(f"Série: {serie}")  # Imprime a série do aluno
        print("Boletim:")  # Cabeçalho para o boletim
        for materia, nota in boletim.items():  # Itera sobre as matérias e notas do boletim
            # Imprime a nota ou informa que não está disponível
            print(f"  {materia.title()}: {nota:.1f}" if nota is not None else f"  {materia.title()}: Não disponível")
        print(f"Média: {estudante['media']:.2f}")  # Imprime a média do aluno
        print(f"Status: Você está {estudante['status']}.")  # Imprime o status do aluno
    else:
        print("Matrícula não encontrada.")  # Informa que a matrícula não existe

def alterar_dados(matricula):   # Define a função 'alterar_dados', que recebe a matrícula de um aluno e permite modificar suas informações, como nome, idade, série ou notas
    estudante = escola1.get(matricula)  # Busca o aluno pelo matrícula
    if estudante:  # Verifica se o aluno foi encontrado
        print("Escolha o que deseja alterar:")  # Informa opções de alteração
        print("1. Nome")  # Opção para alterar o nome
        print("2. Idade")  # Opção para alterar a idade
        print("3. Série")  # Opção para alterar a série
        print("4. Boletim")  # Opção para alterar o boletim
        opcao = input("Digite o número da opção: ")  # Solicita a escolha do usuário

        if opcao == "1":  # Se a opção for alterar o nome
            estudante["nome"] = input("Digite o novo nome: ").title()  # Solicita o novo nome
            print("Nome alterado com sucesso!")  # Informa que a alteração foi feita
        elif opcao == "2":  # Se a opção for alterar a idade
            estudante["idade"] = input("Digite a nova idade: ")  # Solicita a nova idade
            print("Idade alterada com sucesso!")  # Informa que a alteração foi feita
        elif opcao == "3":  # Se a opção for alterar a série
            estudante["serie"] = input("Digite a nova série: ")  # Solicita a nova série
            print("Série alterada com sucesso!")  # Informa que a alteração foi feita
        elif opcao == "4":  # Se a opção for alterar o boletim
            adicionar_notas(estudante["boletim"])  # Chama a função para alterar as notas
            estudante["media"], estudante["status"] = media(estudante["boletim"])  # Recalcula média e status
            print("Boletim alterado com sucesso!")  # Informa que a alteração foi feita
        else:
            print("Opção inválida.")  # Informa que a opção não é válida
    else:
        print("Matrícula não encontrada.")  # Informa que a matrícula não existe

def apagar_aluno(matricula): # Define a função 'apagar_aluno', que recebe a matrícula de um aluno e remove suas informações do sistema, caso exista
    if matricula in escola1:  # Verifica se a matrícula está cadastrada
        del escola1[matricula]  # Remove o aluno do dicionário
        print(f"Aluno com matrícula {matricula} foi apagado com sucesso.")  # Informa que foi apagado
    else:
        print("Matrícula não encontrada.")  # Informa que a matrícula não existe

def contar_alunos(): # Define a função 'contar_alunos', que retorna o número total de alunos cadastrados no sistema
    return len(escola1)  # Retorna a quantidade de alunos cadastrados

# Coleta os dados dos alunos
coletar_dados()  # Chama a função para coletar dados

# Chame a função para calcular a média de todos os alunos após a coleta de dados
calcular_media_geral()  # Calcula a média geral dos alunos

# Acessa um estudante pelo ID
estudante_id = input("Digite a matrícula do estudante desejado para visualizar: ")  # Solicita a matrícula
acessar_estudante(estudante_id)  # Chama a função para acessar os dados do aluno

# Alterar os dados do estudante
estudante_id = input("Digite a matrícula do estudante que deseja alterar os dados: ")  # Solicita a matrícula
alterar_dados(estudante_id)  # Chama a função para alterar os dados do aluno

# Apagar dados de um estudante
estudante_id = input("Digite a matrícula do estudante que deseja apagar: ")  # Solicita a matrícula
apagar_aluno(estudante_id)  # Chama a função para apagar o aluno

# Contar o número de alunos
numero_de_alunos = contar_alunos()  # Armazena o número de alunos cadastrados

# Imprimir todos os dados da escola1 após as alterações
print("\nDados atualizados dos estudantes:")  # Cabeçalho para dados atualizados
for matricula, dados in escola1.items():  # Itera sobre todos os alunos na escola
    print(f"\nMatrícula: {matricula}")  # Imprime a matrícula do aluno
    print(f"Nome: {dados['nome']}")  # Imprime o nome do aluno
    print(f"Idade: {dados['idade']}")  # Imprime a idade do aluno
    print(f"Série: {dados['serie']}")  # Imprime a série do aluno
    print("Boletim:")  # Cabeçalho para o boletim
    for materia, nota in dados["boletim"].items():  # Itera sobre as matérias e notas do boletim
        # Imprime a nota ou informa que não está disponível
        print(f"  {materia.title()}: {nota:.1f}" if nota is not None else f"  {materia.title()}: Não disponível")
    
    # Verifica se as chaves 'media' e 'status' existem antes de acessá-las
    if 'media' in dados and 'status' in dados:  # Verifica se média e status estão disponíveis
        print(f"Média: {dados['media']:.2f}")  # Imprime a média do aluno
        print(f"Status: Você está {dados['status']}.")  # Imprime o status do aluno
    else:
        print("Média e Status não disponíveis para este aluno.")  # Informa que não estão disponíveis
        
print(f"\nNúmero total de alunos cadastrados: {numero_de_alunos}")  # Imprime o total de alunos