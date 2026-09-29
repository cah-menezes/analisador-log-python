# 🔍 Analisador de Log de Auditoria

Script em Python que lê registros de acesso e cruza com a base de colaboradores para identificar comportamentos suspeitos automaticamente.

## 🚨 O que ele detecta

* **Usuário desligado** acessando o sistema
* **Usuário sem MFA** ativo
* **Login fora do horário comercial** (antes das 8h ou depois das 18h)

## 🛠️ Tecnologias Utilizadas

* Python 3 (`csv`, `datetime`)
* Git & GitHub

## 📂 Arquivos

* `analisador.py` → script principal
* `auth.log` → registros de acesso simulados
* `colaboradores.csv` → base de colaboradores com status e MFA

## 🏁 Como Executar

1. Clone o repositório:

```bash
git clone https://github.com/cah-menezes/analisador-log-python.git
cd analisador-log-python
```

2. Execute o analisador:

```bash
python3 analisador.py
```

## 🗺️ Próximos Passos

* Exportar o relatório para arquivo `.txt` ou `.csv`
* Interface gráfica com tkinter
* Detectar padrões de IP suspeito