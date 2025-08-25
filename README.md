# 📖 My Personal Blog

Este é um projeto de um blog pessoal onde você pode criar, editar e excluir posts, salvar posts para ler mais tarde e comentar em posts de outros usuários.

## Funcionalidades

* ✍️ **Posts**: Crie, edite e exclua seus próprios posts.
* 💬 **Comentários**: Interaja com outros usuários comentando nos posts.
* 💾 **Posts Salvos**: Salve posts interessantes para ler depois.
  
## 🚀 Tecnologias

* **Django**: Framework web usado para o backend.
* **PostgreSQL**: Banco de dados relacional para armazenar os dados.
* **Docker**: Usado para configurar o ambiente de desenvolvimento de forma fácil e consistente.

---

## ⚙️ Como começar

Siga as instruções abaixo para configurar e rodar o projeto localmente.

### Pré-requisitos

Certifique-se de que você tem o **Python** e o **Docker** instalados em sua máquina.

### 🛠️ Configuração do Projeto

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/seu-usuario/seu-repositorio.git)
    cd seu-repositorio
    ```

2.  **Configuração do banco de dados:**

    Você tem duas opções para configurar o banco de dados PostgreSQL.

    **Opção 1: Usando Docker Compose (Recomendado)**

    Este método é o mais simples e já configura o banco de dados para você.

    ```bash
    docker-compose up -d --build
    ```

    Isso vai iniciar o servidor do banco de dados em um contêiner. O banco de dados estará pronto para uso.

    **Opção 2: Usando um PostgreSQL local**

    Se você preferir usar uma instalação local do PostgreSQL, certifique-se de que está rodando e configure as variáveis de ambiente do banco de dados no arquivo `.env` (você pode criar um a partir de um arquivo de exemplo se houver).

3.  **Instalar dependências:**

    Todas as dependências do projeto estão listadas no arquivo `requirements.txt`. Instale-as usando pip:

    ```bash
    pip install -r requirements.txt
    ```

4.  **Rodar migrações:**

    Aplique as migrações do banco de dados para criar as tabelas necessárias:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5.  **Criar um superusuário (opcional):**

    Crie uma conta de administrador para acessar o painel do Django:

    ```bash
    python manage.py createsuperuser
    ```

6.  **Rodar o servidor:**

    Inicie o servidor de desenvolvimento do Django:

    ```bash
    python manage.py runserver
    ```

    O blog estará disponível em `http://127.0.0.1:8000`.

---

## Licença

Este projeto é de código aberto e está disponível sob a licença **MIT**.
