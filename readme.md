# 📚 Gestor de Tarefas - API REST com Django

## Objetivo do Projeto

Este é um projeto de estudo focado em desenvolver os fundamentos de:

- **Desenvolvimento de APIs RESTful** com Django REST Framework
- **Integração frontend-backend** 
- **Padrões de arquitetura web e boas práticas com Django**

## Conceitos Abordados

### Backend (Django)
- `Models` - Estrutura de dados do banco
- `Serializers` - Conversão de dados Python/JSON
- `Views` - Lógica de negócios e endpoints
- `URL routing` - Mapeamento de endpoints

### API REST
- Verbos HTTP (GET, POST, PATCH, DELETE)
- Status codes (200, 201, 400, 404)
- Estrutura de requests/responses
- CRUD completo

### Frontend
- Consumo de API com Fetch API
- Manipulação do DOM
- Tratamento de erros

## Endpoints da API REST

A aplicação oferece os seguintes endpoints para interação via API:

1. **Listar Todas as Tarefas**
   - **Método**: GET
   - **Endpoint**: `/api/`
   - **Descrição**: Retorna todas as tarefas cadastradas

2. **Detalhes de uma Tarefa**
   - **Método**: GET
   - **Endpoint**: `/api/<id>/`
   - **Descrição**: Recupera os detalhes de uma tarefa específica

3. **Criar Nova Tarefa**
   - **Método**: POST
   - **Endpoint**: `/api/create`
   - **Corpo da Requisição**:
     ```json
     {
         "Title": "Título da Tarefa",
         "Description": "Descrição opcional",
         "Date": "AAAA-MM-DD",
         "Completed": False
     }
     ```

4. **Atualizar Tarefa**
   - **Método**: PATCH
   - **Endpoint**: `/api/<id>/`
   - **Descrição**: Permite atualizar parcialmente uma tarefa
   - **Corpo da Requisição**: Campos a serem atualizados

5. **Excluir Tarefa**
   - **Método**: DELETE
   - **Endpoint**: `/api/delete/<id>`
   - **Descrição**: Remove uma tarefa específica

## Tecnologias Utilizadas

- **Backend**: Django, Django REST Framework
- **Frontend**: HTML, JavaScript, Tailwind CSS
- **Banco de Dados**: SQLite
- **Ícones**: Font Awesome
