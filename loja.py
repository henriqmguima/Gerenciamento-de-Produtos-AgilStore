import json
import os

# Nome do arquivo do "banco de dados"
arquivo_inventario = 'inventario.json'

# Função para carregar o inventário do arquivo JSON


def carregar_inventario():
    if os.path.exists(arquivo_inventario):
        with open(arquivo_inventario, 'r') as file:
            return json.load(file)
    else:
        return []

# Função para salvar o inventário no arquivo JSON


def salvar_inventario():
    with open(arquivo_inventario, 'w') as file:
        json.dump(inventario, file, indent=4)


# Lista de inventário
inventario = carregar_inventario()
contador_id = max([produto['id'] for produto in inventario], default=0) + 1


def validar_entrada(valor, tipo):
    """Função para validar se a entrada do usuário é válida"""
    while True:
        try:
            if tipo == 'str':
                if not valor.strip():
                    raise ValueError("Valor não pode ser vazio.")
                return valor.strip()
            elif tipo == 'int':
                valor_int = int(valor)
                if valor_int < 0:
                    raise ValueError("Valor não pode ser negativo.")
                return valor_int
            elif tipo == 'float':
                valor_float = float(valor)
                if valor_float < 0:
                    raise ValueError("Valor não pode ser negativo.")
                return valor_float
        except ValueError as e:
            print(e)
            valor = input(f"Digite novamente ({tipo}): ")


def adicionar_produto():
    global contador_id
    nome = input("Digite o nome do produto: ")
    nome = validar_entrada(nome, 'str')

    categoria = input("Digite a categoria do produto: ")
    categoria = validar_entrada(categoria, 'str')

    quantidade = input("Digite a quantidade em estoque: ")
    quantidade = validar_entrada(quantidade, 'int')

    preco = input("Digite o preço do produto: ")
    preco = validar_entrada(preco, 'float')

    # Criar um dicionário para o produto com ID baseado no contador
    produto = {
        "id": contador_id,
        "nome": nome,
        "categoria": categoria,
        "quantidade": quantidade,
        "preco": preco
    }

    # Adicionar o produto ao inventário
    inventario.append(produto)

    # Incrementar o contador para o próximo ID
    contador_id += 1
    salvar_inventario()  # Salvar o inventário atualizado no arquivo
    print(f"Produto {nome} adicionado com sucesso!")


def listar_produtos():
    if inventario:
        # Exibir os produtos como uma tabela
        print("\n--- Inventário Atual ---")
        print(f"{'ID':<5} {'Nome':<20} {'Categoria':<15} {
              'Quantidade':<10} {'Preço':<10}")
        print("-" * 60)
        for produto in inventario:
            print(f"{produto['id']:<5} {produto['nome']:<20} {produto['categoria']:<15} {
                  produto['quantidade']:<10} {produto['preco']:<10.2f}")
    else:
        print("O inventário está vazio.")


def atualizar_produto():
    id_produto = int(input("Digite o ID do produto que deseja atualizar: "))

    # Procurar o produto no inventário
    produto = next((p for p in inventario if p['id'] == id_produto), None)

    if produto:
        print(f"\nProduto encontrado: {produto['nome']}")
        print("Quais campos você deseja atualizar? (Digite 'nome', 'categoria', 'quantidade' ou 'preco')")

        # Solicitar atualização dos campos
        campo = input(
            "Digite o nome do campo que deseja atualizar (ou 'sair' para cancelar): ").lower()

        if campo == 'sair':
            print("Atualização cancelada.")
            return

        if campo == 'nome':
            novo_nome = input("Digite o novo nome do produto: ")
            produto['nome'] = validar_entrada(novo_nome, 'str')
        elif campo == 'categoria':
            nova_categoria = input("Digite a nova categoria do produto: ")
            produto['categoria'] = validar_entrada(nova_categoria, 'str')
        elif campo == 'quantidade':
            nova_quantidade = input("Digite a nova quantidade em estoque: ")
            produto['quantidade'] = validar_entrada(nova_quantidade, 'int')
        elif campo == 'preco':
            novo_preco = input("Digite o novo preço do produto: ")
            produto['preco'] = validar_entrada(novo_preco, 'float')
        else:
            print("Campo inválido! Tente novamente.")
            return

        salvar_inventario()  # Salvar as alterações no arquivo
        print(f"Produto {produto['nome']} atualizado com sucesso!")
    else:
        print("Produto não encontrado com esse ID.")


def excluir_produto():
    id_produto = int(input("Digite o ID do produto que deseja excluir: "))

    # Procurar o produto no inventário
    produto = next((p for p in inventario if p['id'] == id_produto), None)

    if produto:
        print(f"\nProduto encontrado: {produto['nome']}")
        confirmacao = input(f"Tem certeza que deseja excluir o produto '{
                            produto['nome']}'? (s/n): ").lower()

        if confirmacao == 's':
            inventario.remove(produto)  # Remover o produto do inventário
            salvar_inventario()  # Salvar o inventário atualizado no arquivo
            print(f"Produto '{produto['nome']}' excluído com sucesso!")
        else:
            print("Exclusão cancelada.")
    else:
        print("Produto não encontrado com esse ID.")


def buscar_produto():
    opcao_busca = input(
        "Deseja buscar por ID ou Nome (digite 'id' ou 'nome')? ").lower()

    if opcao_busca == 'id':
        id_produto = int(input("Digite o ID do produto que deseja buscar: "))

        # Procurar o produto pelo ID
        produto = next((p for p in inventario if p['id'] == id_produto), None)

        if produto:
            print("\n--- Detalhes do Produto ---")
            print(f"ID: {produto['id']}")
            print(f"Nome: {produto['nome']}")
            print(f"Categoria: {produto['categoria']}")
            print(f"Quantidade em Estoque: {produto['quantidade']}")
            print(f"Preço: R${produto['preco']:.2f}")
        else:
            print("Produto não encontrado com esse ID.")

    elif opcao_busca == 'nome':
        nome_produto = input(
            "Digite o nome (ou parte do nome) do produto que deseja buscar: ").lower()

        # Procurar o produto pelo nome (parcial)
        produtos_encontrados = [
            p for p in inventario if nome_produto in p['nome'].lower()]

        if produtos_encontrados:
            print("\n--- Produtos Encontrados ---")
            for produto in produtos_encontrados:
                print(f"ID: {produto['id']} | Nome: {produto['nome']} | Categoria: {
                      produto['categoria']} | Quantidade: {produto['quantidade']} | Preço: R${produto['preco']:.2f}")
        else:
            print("Nenhum produto encontrado com esse nome.")


def menu():
    while True:
        print("\n--- Menu ---")
        print("1. Adicionar Produto")
        print("2. Listar Produtos")
        print("3. Atualizar Produto")
        print("4. Excluir Produto")
        print("5. Buscar Produto")
        print("6. Fechar Sistema")

        opcao = input("Escolha uma opção (1, 2, 3, 4, 5 ou 6): ")

        if opcao == "1":
            adicionar_produto()
        elif opcao == "2":
            listar_produtos()
        elif opcao == "3":
            atualizar_produto()
        elif opcao == "4":
            excluir_produto()
        elif opcao == "5":
            buscar_produto()
        elif opcao == "6":
            print("Sistema fechado.")
            break
        else:
            print("Opção inválida. Tente novamente.")


# Rodar o menu
menu()
