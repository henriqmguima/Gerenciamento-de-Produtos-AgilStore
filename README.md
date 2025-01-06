# Sistema de Inventário

Este é um sistema simples de gerenciamento de inventário para produtos, onde você pode adicionar, listar, atualizar, excluir e buscar produtos no estoque. Ele cria e utiliza um arquivo JSON para armazenar os dados de produtos.

## Tecnologias Utilizadas

- **Python 3.x**: A linguagem utilizada para o desenvolvimento do sistema.
- **JSON**: Formato utilizado para armazenamento dos dados no arquivo `inventario.json`.

## Funcionalidades

1. **Adicionar Produto**: Permite adicionar novos produtos ao inventário.
2. **Listar Produtos**: Exibe todos os produtos armazenados no inventário.
3. **Atualizar Produto**: Permite atualizar as informações de um produto existente.
4. **Excluir Produto**: Permite excluir um produto do inventário.
5. **Buscar Produto**: Permite buscar um produto pelo ID ou nome (parcial).

## Design da Solução
A aplicação foi projetada para ser simples e funcional, com foco na praticidade para um uso direto no terminal. As principais características incluem:

**Banco de Dados Simulado**: Utilizamos o formato JSON para persistir os dados do inventário.
**Sistema Baseado em Menu**: O menu apresenta as funcionalidades principais de forma clara e sequencial, permitindo uma navegação intuitiva para o usuário.
**Validação de Dados**: Foram incluídas validações para garantir que os dados inseridos sejam coerentes e completos, como a proibição de campos vazios, letras ou valores negativos para quantidade e preço.
**Separação de Funções**: Cada funcionalidade principal foi implementada como uma função independente facilitando a manutenção.

## Como Rodar

1. Clone este repositório ou baixe os arquivos.
2. Abra o terminal ou prompt de comando na pasta do projeto.
3. Execute o seguinte comando para rodar o sistema:

   ```bash
   python inventario.py
