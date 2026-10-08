# 🔍 Analisador de Log de Auditoria

Script em Python que automatiza a revisão de registros de acesso, cruzando logs de autenticação com a base de colaboradores para identificar comportamentos suspeitos e gerar relatório de evidência — sem precisar revisar linha por linha manualmente.

> Projeto desenvolvido como parte de uma trilha de automação aplicada à segurança da informação e GRC.

## 🚨 O que ele detecta

- **Usuário desligado** acessando o sistema
- **Usuário sem MFA** ativo
- **Login fora do horário comercial** (antes das 8h ou depois das 18h)

## 📄 Saída

Gera automaticamente um arquivo `.txt` com o relatório de inconsistências encontradas, pronto para ser usado como evidência de auditoria.

## 🛠️ Tecnologias

- Python 3 (`csv`, `datetime`, `os`)
- Git & GitHub

## 📂 Arquivos

- `analisador.py` → script principal de análise e exportação
- `auth.log` → registros de acesso simulados
- `colaboradores.csv` → base de colaboradores com status e MFA

## 🏁 Como executar

1. Clone o repositório:
```bash
git clone https://github.com/cah-menezes/analisador-log-python.git
cd analisador-log-python
```

2. Execute o analisador:
```bash
python3 analisador.py
```

O relatório será gerado automaticamente na pasta `relatorios/`.

## 💡 Possíveis evoluções

- Detecção de padrões de IP suspeito
- Exportação em `.csv` para análise em planilha
- Integração com base de dados real via SQL