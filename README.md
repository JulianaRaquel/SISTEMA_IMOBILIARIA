# Sistema de Agendamentos para Imobiliária

### **Objetivo**: desenvolver um sistema de exposição de imóveis para venda e aluguel.

## Tecnologias Utilizadas:
* ###  Python
* ### Django
* ### Git
* ### PostgreSQL
* ### Docker

## Funcionalidades do Projeto

#### 1. Sistema de cadastro de usuário com username e-mail e senha (http://127.0.0.1:8000/cadastro/)
#### 2. Sistema de login de usuário com username e senha (http://127.0.0.1:8000/login/)
#### 3. Página de Home que lista todos os imóveis disponíveis sendo possível filtrar por preço mínimo, preço máximo, cidade e tipo do imóvel. (http://127.0.0.1:8000/home/)
#### 4. Página que exibe os detalhes de cada imóvel em específico (http://127.0.0.1:8000/imovel/1)
#### 5. Botão para agendar visita no qual o usuário vai informar o dia e o horário em que fará a visita.
#### 6. Página que lista os agendamentos eitos pelo usuário na qual inclui também um botão para cancelar o agendamento.

## Instruções para instalação

#### _Versão do Python requerida:_ 3.9.13

### Faça o clone do projeto:
```commandline
git clone git@github.com:JulianaRaquel/SISTEMA_IMOBILIARIA.git
```
### Crie o ambiente virtual (venv):
```commandline
python3 -m venv venv
```
### Ative o ambiente virtual no linux:
```commandline
source venv/bin/activate
```
### Ative o ambiente virtual no windows:
```commandline
venv\Scripts\Activate
```
### Instale as dependências do projeto:
```commandline
pip install -r requirements.txt
```
### Copie as variáveis de ambiente:
```commandline
cp .env.example .env
```
### Aplique as migrações:
```commandline
python3 manage.py migrate
```
### Rode o servidor:
```commandline
python3 manage.py runserver
```