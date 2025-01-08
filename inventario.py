import json
import locale
import re

# Configurações de localização para valores monetários
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

# Nome do arquivo que armazena os dados do inventário
ARQUIVO_DADOS = "inventario.json"

# Inicializa o inventário carregando os dados do arquivo ou criando uma lista vazia
def inicializar_dados():
    global inventario
    try:
        with open(ARQUIVO_DADOS, "r") as arquivo:
            inventario = json.load(arquivo)
    except FileNotFoundError:
        inventario = []
    except json.JSONDecodeError:
        print("Erro ao carregar os dados. O arquivo JSON está corrompido.")
        inventario = []

# Salva os dados do inventário no arquivo JSON
def salvar_dados():
    try:
        with open(ARQUIVO_DADOS, "w") as arquivo:
            json.dump(inventario, arquivo, indent=4, ensure_ascii=False)
    except IOError:
        print("Erro ao salvar os dados no arquivo.")

# Gera um ID único para novos produtos
def gerar_id():
    return max(produto['id'] for produto in inventario) + 1 if inventario else 1

# Valida o formato do preço no padrão brasileiro
def validar_preco(preco_str):
    pattern = r'^\d{1,3}(\.\d{3})*,\d{2}$'  # Exemplo: 1.000,00
    return bool(re.match(pattern, preco_str))

# Adiciona um novo produto ao inventário
def adicionar_produto():
    nome = input("Digite o nome do produto: ").strip()
    if not nome:
        print("O nome do produto não pode estar vazio.")
        return

    categoria = input("Digite a categoria do produto: ").strip()
    if not categoria:
        print("A categoria do produto não pode estar vazia.")
        return

    try:
        quantidade = int(input("Digite a quantidade em estoque: ").strip())
        preco_str = input("Digite o preço do produto: ").strip()
        if not validar_preco(preco_str):
            print("Formato de preço inválido. Use o formato 1.000,00.")
            return

        preco = float(preco_str.replace('.', '').replace(',', '.'))
    except ValueError:
        print("Entrada inválida. A quantidade deve ser um número inteiro e o preço válido.")
        return

    produto = {
        "id": gerar_id(),
        "nome": nome,
        "categoria": categoria,
        "quantidade": quantidade,
        "preco": preco
    }
    inventario.append(produto)
    salvar_dados()
    print("Produto adicionado com sucesso!")

# Lista produtos com opções de filtro e ordenação
def listar_produtos():
    if not inventario:
        print("Nenhum produto encontrado.")
        return

    print("Opções de filtro e ordenação:")
    print("1. Sem filtro/ordenação")
    print("2. Filtrar por categoria")
    print("3. Ordenar por nome")
    print("4. Ordenar por quantidade")
    print("5. Ordenar por preço")

    try:
        opcao = int(input("Escolha uma opção: "))
    except ValueError:
        print("Opção inválida.")
        return

    produtos_filtrados = inventario
    if opcao == 2:
        categoria = input("Digite a categoria para filtrar: ").strip()
        produtos_filtrados = [p for p in inventario if p['categoria'].lower() == categoria.lower()]
    elif opcao == 3:
        produtos_filtrados = sorted(inventario, key=lambda p: p['nome'].lower())
    elif opcao == 4:
        produtos_filtrados = sorted(inventario, key=lambda p: p['quantidade'], reverse=True)
    elif opcao == 5:
        produtos_filtrados = sorted(inventario, key=lambda p: p['preco'], reverse=True)

    if not produtos_filtrados:
        print("Nenhum produto encontrado com os critérios selecionados.")
        return

    print(f"{'ID':<5}{'Nome':<20}{'Categoria':<15}{'Quantidade':<15}{'Preço':<15}")
    print("-" * 70)
    for produto in produtos_filtrados:
        preco_formatado = locale.currency(produto['preco'], grouping=True).replace('R$', '').strip()
        print(f"{produto['id']:<5}{produto['nome']:<20}{produto['categoria']:<15}{produto['quantidade']:<15}{preco_formatado:<15}")

# Atualiza informações de um produto existente
def atualizar_produto():
    try:
        id_produto = int(input("Digite o ID do produto que deseja atualizar: "))
        produto = next((p for p in inventario if p['id'] == id_produto), None)
        if not produto:
            print("Produto não encontrado.")
            return

        print("Deixe o campo vazio para manter o valor atual.")
        novo_nome = input(f"Nome ({produto['nome']}): ").strip()
        nova_categoria = input(f"Categoria ({produto['categoria']}): ").strip()
        nova_quantidade = input(f"Quantidade ({produto['quantidade']}): ").strip()
        novo_preco = input(f"Preço ({locale.currency(produto['preco'], grouping=True).replace('R$', '').strip()}): ").strip()

        if novo_nome:
            produto['nome'] = novo_nome
        if nova_categoria:
            produto['categoria'] = nova_categoria
        if nova_quantidade:
            produto['quantidade'] = int(nova_quantidade)
        if novo_preco:
            if validar_preco(novo_preco):
                produto['preco'] = float(novo_preco.replace('.', '').replace(',', '.'))
            else:
                print("Formato de preço inválido. Use o formato 1.000,00.")
                return

        salvar_dados()
        print("Produto atualizado com sucesso!")
    except ValueError:
        print("ID ou valor inválido.")

# Remove um produto do inventário
def excluir_produto():
    try:
        id_produto = int(input("Digite o ID do produto que deseja excluir: "))
        produto = next((p for p in inventario if p['id'] == id_produto), None)
        if not produto:
            print("Produto não encontrado.")
            return

        confirmar = input(f"Tem certeza de que deseja excluir {produto['nome']}? (sim/não): ").strip().lower()
        if confirmar == "sim":
            inventario.remove(produto)
            salvar_dados()
            print("Produto excluído com sucesso!")
        else:
            print("Operação cancelada.")
    except ValueError:
        print("ID inválido.")

# Busca produtos pelo nome ou categoria
def buscar_produto():
    termo = input("Digite o nome ou categoria do produto que deseja buscar: ").strip().lower()
    resultados = [p for p in inventario if termo in p['nome'].lower() or termo in p['categoria'].lower()]

    if not resultados:
        print("Nenhum produto encontrado.")
        return

    print(f"{'ID':<5}{'Nome':<20}{'Categoria':<15}{'Quantidade':<15}{'Preço':<15}")
    print("-" * 70)
    for produto in resultados:
        preco_formatado = locale.currency(produto['preco'], grouping=True).replace('R$', '').strip()
        print(f"{produto['id']:<5}{produto['nome']:<20}{produto['categoria']:<15}{produto['quantidade']:<15}{preco_formatado:<15}")

# Exibe o menu principal
def menu_principal():
    inicializar_dados()
    while True:
        print("\nGerenciamento de Inventário")
        print("1. Adicionar Produto")
        print("2. Listar Produtos")
        print("3. Atualizar Produto")
        print("4. Excluir Produto")
        print("5. Buscar Produto")
        print("6. Sair")

        escolha = input("Escolha uma opção: ").strip()
        if escolha == "1":
            adicionar_produto()
        elif escolha == "2":
            listar_produtos()
        elif escolha == "3":
            atualizar_produto()
        elif escolha == "4":
            excluir_produto()
        elif escolha == "5":
            buscar_produto()
        elif escolha == "6":
            print("Encerrando aplicação. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu_principal()
