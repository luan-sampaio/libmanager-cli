# 📚 Libmanager CLI

![Python Version](https://img.shields.io/badge/python-3.10%2B-blue?style=flat&logo=python)
![Status](https://img.shields.io/badge/status-em_desenvolvimento-yellow)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)

<div align="center">
  <img src="libmanager.gif" alt="Demonstração do Libmanager" width="600">
</div>
<br>

## 📖 Descrição

O **Libmanager** é uma aplicação de linha de comando (CLI) desenvolvida em Python para gerenciamento de uma biblioteca pessoal.

Este projeto reflete uma etapa importante no meu aprendizado da linguagem Python e no desenvolvimento da minha lógica de programação.


## ✨ Funcionalidades Atuais

- [x] **Adicionar Livro:** Cadastro com título, autor e ano (ID gerado automaticamente).
- [x] **Listar Livros:** Visualização de todos os itens cadastrados.
- [x] **Editar Livro:** Atualização de campos específicos.
- [x] **Excluir Livro:** Remoção de registros.
- [ ] **Persistência de Dados:** (Em andamento) Implementação de salvamento em JSON.
- [ ] **Cadastro automático do livro:** (Em andamento) Implementação de consumo de API.

## 🚀 Roadmap 

Como o projeto está em constante evolução, estas são as próximas melhorias planejadas:

1. Implementar persistência de dados.
2. Adicionar consumo de API para cadastro automático do livro por nome.
3. Melhorar a interface visual do terminal.

## 🗂️ Estrutura do Projeto

A arquitetura foi pensada para separar a interface da lógica de negócios:

```text
libmanager/
│
├── src/
│   ├── database.py       # Gerenciamento de dados
│   ├── functions_book.py # Lógica do CRUD
│   ├── interface.py      # Menus e inputs do usuário
│   └── main.py           # Ponto de entrada da aplicação
│
├── LICENSE               # Licença do projeto
└── README.md             # Documentação
```

## 🛠️ Tecnologias Utilizadas

O foco deste projeto é lógica pura, utilizando bibliotecas nativas do Python:

- Python 3

- Bibliotecas Padrão:
    - os: Utilizado para funcionalidades do sistema (ex: limpeza de tela).

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
cd libmanager 
```
3. Execute o arquivo principal:
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
