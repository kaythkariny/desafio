# Gerenciamento de Inventário

Este é um sistema simples de gerenciamento de inventário para produtos. Ele permite adicionar, listar, atualizar, excluir e buscar produtos, além de salvar automaticamente os dados em um arquivo JSON para persistência.

## Funcionalidades

1. **Adicionar Produto**: Adicione produtos ao inventário fornecendo nome, categoria, quantidade e preço no formato brasileiro.
2. **Listar Produtos**: Liste todos os produtos com opções de filtro por categoria ou ordenação por nome, quantidade ou preço.
3. **Atualizar Produto**: Atualize os detalhes de um produto existente no inventário.
4. **Excluir Produto**: Remova um produto do inventário.
5. **Buscar Produto**: Busque produtos por nome ou categoria.
6. **Persistência de Dados**: Os dados são salvos automaticamente em um arquivo JSON (`inventario.json`) para garantir que nenhuma informação seja perdida ao encerrar o programa.

## Pré-requisitos

- Python 3.6 ou superior.
- Biblioteca `locale` (inclusa no Python).

## Como Usar

1. Clone este repositório ou copie o código para o seu ambiente local.
2. Certifique-se de que o arquivo `inventario.json` existe no mesmo diretório do script. Caso contrário, ele será criado automaticamente.
3. Execute o arquivo principal:

```bash
python inventario.py
```

4. Navegue pelo menu principal para gerenciar o inventário:
    - `1`: Adicionar Produto.
    - `2`: Listar Produtos.
    - `3`: Atualizar Produto.
    - `4`: Excluir Produto.
    - `5`: Buscar Produto.
    - `6`: Sair.

## Estrutura do Arquivo JSON

O arquivo `inventario.json` armazena os dados no seguinte formato:

```json
[
    {
        "id": 1,
        "nome": "Produto A",
        "categoria": "Categoria X",
        "quantidade": 10,
        "preco": 25.50
    },
    {
        "id": 2,
        "nome": "Produto B",
        "categoria": "Categoria Y",
        "quantidade": 5,
        "preco": 100.00
    }
]
```

- `id`: Identificador único do produto.
- `nome`: Nome do produto.
- `categoria`: Categoria à qual o produto pertence.
- `quantidade`: Quantidade em estoque.
- `preco`: Preço do produto em reais.

## Observações

- O formato de preço deve seguir o padrão brasileiro (exemplo: `1.000,00`).
- Caso o arquivo `inventario.json` esteja ausente ou corrompido, o programa criará um novo arquivo vazio ou exibirá um aviso.
- Utilize as opções do menu para interagir com o sistema de forma intuitiva.

---
**Autora**: Kayth Kariny  
**Licença**: MIT

