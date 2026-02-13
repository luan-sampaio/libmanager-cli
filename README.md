# 📚 Libmanager CLI

![Python](https://img.shields.io/badge/python-3.10+-blue)
![Status](https://img.shields.io/badge/status-completed-brightgreen)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-orange)

<div align="center">
  <img src="libmanager.gif" alt="Demonstração do Libmanager" width="600">
</div>
<br>

## 📖 Descrição

O **Libmanager** é uma aplicação de linha de comando (CLI) desenvolvida em Python para gerenciamento de uma biblioteca pessoal.

Este projeto reflete uma etapa importante no meu aprendizado da linguagem Python e no desenvolvimento da minha lógica de programação.


## ✨ Funcionalidades Atuais

- [x] **Cadastro automático do livro:** Cadastro do livro por meio do título (autor, ano e id são preenchidos automaticamente).
- [x] **Listar Livros:** Visualização de todos os itens cadastrados.
- [x] **Editar Livro:** Atualização de campos específicos.
- [x] **Excluir Livro:** Remoção do livro.
- [x] **Persistência de Dados:** Implementação da persistência em CSV.


## 🗂️ Estrutura do Projeto

A arquitetura foi pensada para separar a interface da lógica de negócios:

```text
libmanager/
│
├── data/                 # Diretório de persistência
│   └── books.csv         # Arquivo onde os dados são salvos
│
├── src/
│   ├── api_client.py     # Conexão com APIs externas 
│   ├── database.py       # Gerenciamento de dados no CSV
│   ├── functions_book.py # Lógica de negócios e controle 
│   ├── interface.py      # Menus e inputs do usuário 
│   └── main.py           # Ponto de entrada da aplicação
│
├── .gitignore            # Arquivos ignorados pelo Git
├── LICENSE               # Licença do projeto
├── README.md             # Documentação
└── requirements.txt      # Dependências do projeto 
```

## 🛠️ Tecnologias Utilizadas

O foco deste projeto é lógica pura, utilizando bibliotecas nativas do Python:

- Python 3

- Bibliotecas Padrão:
    - os: Utilizado para limpeza de tela.
    - requests: Utilizado para integração com a API da OpenLibrary.
    - csv: Utilizado para auxiliar nas operações de CRUD no CSV.
    - sys: Utilizado para encerrar o programa em cenários de Erro.
    - tabulate: Utilizado para expor a tabela de livros cadastrados.

## 🧠 Aprendizados

Durante o desenvolvimento deste projeto, tenho focado em:

- Sintaxe e Tipagem: Aprofundamento nos fundamentos da linguagem Python.

- Lógica de Programação.

- Modularização: Organização de código em módulos (src) para facilitar a manutenção.

## ⚙️ Como Executar

1. Clone o repositório:
``` bash
git clone https://github.com/luan-sampaio/libmanager-cli.git 
```
2. Entre na pasta do projeto:
``` bash
cd libmanager-cli
```
3. Crie e ative um ambiente virtual:
``` bash
# No Windows:
python -m venv venv
venv\Scripts\activate

# No Linux/Mac:
python3 -m venv venv
source venv/bin/activate
```
4. Instale as dependências do projeto:
``` bash
pip install -r requirements.txt
```
5. Execute o arquivo principal:
``` bash
python src/main.py 
```

## 🤝 Contribuindo

Sugestões e correções são muito bem-vindas, pois estou em fase de aprendizado!

1. Faça um Fork do projeto.
2. Crie uma Branch ```(git checkout -b feature/SuaFeature).```
3. Faça o Commit ```(git commit -m 'Add: nova funcionalidade').```
4. Faça o Push ```(git push origin feature/SuaFeature).```
5. Abra um Pull Request.

## 📄 Licença

Este projeto está sob a licença MIT.

