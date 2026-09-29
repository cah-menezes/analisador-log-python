# Analisador de logs > melhorar descrição

import csv
import datetime

# Variáveis fixas
ARQUIVO_LOG= "auth.log"
ARQUIVO_COLABORADORES = "colaboradores.csv"

# Funções
def carregar_logs():
    logs = []
    with open(ARQUIVO_LOG, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            logs.append(linha.strip())
    return logs

def carregar_colaboradores():
    colaboradores = {}
    with open(ARQUIVO_COLABORADORES, "r", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            colaboradores[linha["usuario"]] = linha
    return colaboradores

def analisar(logs, colaboradores):
    analisados = []
    for linha in logs:
        partes = linha.split(" | ")
        usuario = partes[1]
        ficha = colaboradores[usuario]
        if ficha ["status"] == "desligado":
            analisados.append(f"🚨 ALERTA: {usuario} está desligado mas acessou o sistema!")
    return analisados

# Programa principal
if __name__ == "__main__":
    colaboradores = carregar_colaboradores()
    logs = carregar_logs()
    alertas = analisar(logs, colaboradores)
    print(alertas)