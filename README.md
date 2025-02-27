# WhatStock 📊📦

WhatStock é um sistema de gerenciamento de estoque desenvolvido em **Django** que envia alertas via **WhatsApp** quando os produtos atingem um nível crítico de estoque.

## 🚀 Funcionalidades

- Cadastro de produtos com detalhes como nome, categoria, estoque, preço, validade e mais.
- Monitoramento do estoque em tempo real.
- Envio de alertas automáticos via **WhatsApp** quando o estoque está abaixo do limite mínimo.
- Sistema de autenticação personalizado para acesso seguro.

## 🛠️ Pré-requisitos

Antes de começar, certifique-se de ter instalado:

- Python 3.11 ou superior
- Django 5.1.5
- Git
- MySQL ou MariaDB

## 📥 Instalação

1. Clone o repositório:

```bash
git clone git@github.com:Adricampelo/projeto-django.git
cd projeto-django
```

2. Crie e ative um ambiente virtual:

```bash
python -m venv env
source env/bin/activate  # No Windows: .\env\Scripts\activate
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

## 🗄️ Configuração do Banco de Dados

1. Crie um banco de dados no MySQL chamado `whatstock`:

```sql
CREATE DATABASE whatstock;
```

2. Ajuste as credenciais do banco no arquivo `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'whatstock',
        'USER': 'seu_usuario',
        'PASSWORD': 'sua_senha',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

3. Execute as migrações para criar as tabelas:

```bash
python manage.py makemigrations
python manage.py migrate
```

4. Insira um usuário administrador:

```sql
INSERT INTO whatstock.usuarios_usuario
(id, nome, email, password, contato, endereco, cpf, is_active, is_staff, is_superuser, last_login)
VALUES(11, 'ADMIN', 'admin@admin.com', 'pbkdf2_sha256$870000$3XAZ3dDq807fHy9rSKBHSu$5cm/4264cyB1/uQKun0YGvVqvdLXWMGjw6OSBG4rkuM=', '999999999', 'Rua Do Filipinho', '61119235367', 1, 0, 0, '2025-02-27 02:19:12.816845');
```

## ▶️ Executando o Projeto

1. Inicie o servidor de desenvolvimento:

```bash
python manage.py runserver
```

2. Acesse no navegador:

```
http://127.0.0.1:8000
```

## 📊 Gráfico de Estoque Crítico

O sistema gera gráficos interativos para visualização do estoque utilizando o Google Charts.

## 📢  Bot do WhatsApp

- Monitoramento do Estoque: Consulta o banco de dados e envia alertas no WhatsApp se houver produtos com estoque abaixo do mínimo..

Para instalar as bibliotecas necessárias para executar o código, você deve usar o **pip** (gerenciador de pacotes do Python).  

### ✅ **Passos para instalar as bibliotecas:**

1. **Certifique-se de ter o Python instalado**  
   Para verificar se o Python está instalado, execute no terminal ou prompt de comando:  
   ```bash
   python --version
   ```
   Ou, em algumas máquinas:  
   ```bash
   python3 --version
   ```

2. **Instale o Selenium e o MySQL Connector**  
   Execute os comandos abaixo no terminal:

   ```bash
   pip install selenium mysql-connector-python
   ```

   Se estiver usando **Linux** ou **macOS** e precisar do **pip3**, use:  
   ```bash
   sudo apt-get update
   sudo apt-get install python3-pip
   pip3 install selenium mysql-connector-python
   ```

3. **Verifique a instalação**  
   Para garantir que tudo foi instalado corretamente, execute:  
   ```bash
   python -m pip show selenium mysql-connector-python
   ```



4. **Teste o código:**  
   Execute o script:  
   ```bash
   python bot.py
   

