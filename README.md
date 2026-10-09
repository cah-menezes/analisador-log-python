# 🔍 Analisador e Exportador de Log de Auditoria

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Segurança da Informação](https://img.shields.io/badge/Segurança_da_Informação-GRC-E74C3C?style=flat)

Scripts em Python que automatizam a revisão de registros de acesso: cruzam logs de autenticação com a base de colaboradores para identificar comportamentos suspeitos e exportam o resultado como evidência de auditoria — sem precisar revisar linha por linha manualmente.

---

## 🚨 O que o analisador detecta

- **Usuário desligado** acessando o sistema
- **Usuário sem MFA** ativo
- **Login fora do horário comercial** (antes das 8h ou depois das 18h)

## 📤 O que o exportador faz

Recebe os alertas gerados pelo analisador e salva automaticamente um arquivo `.txt` na pasta `relatorios/`, com data e hora no nome — pronto para uso como evidência de auditoria.

```
relatorios/relatorio_2024-09-15_23-47-00.txt
```

Cada execução gera um arquivo novo, sem sobrescrever os anteriores.

---

## 📂 Arquivos

- `analisador.py` — lógica de análise: lê o log, cruza com a base e gera os alertas
- `exportador.py` — salva os alertas em `.txt` com timestamp
- `auth.log` — registros de acesso simulados
- `colaboradores.csv` — base de colaboradores com status e MFA

## 🚀 Como executar

**Só a análise no terminal:**
```bash
git clone https://github.com/cah-menezes/analisador-log-python.git
cd analisador-log-python
python3 analisador.py
```

**Com exportação do relatório:**
```bash
python3 exportador.py
```

O relatório será salvo automaticamente em `relatorios/`. Se a pasta não existir, o script cria sozinho.

---

*Projeto desenvolvido como parte de uma trilha de automação aplicada à segurança da informação e GRC.*