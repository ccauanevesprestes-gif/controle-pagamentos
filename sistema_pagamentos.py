
from datetime import datetime
import os

arquivo = "pagamento.json"


def carregar():
    if os.path.exists(arquivo):
        with open(arquivo, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def salvar(dados):
    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)


def conferir_liberacao(lista):
    print("\n--- conferir liberação ---")

    for item in lista:
        if item["status"] == "recebido":
            print(item)

    print("verificação concluída.")


def solicitar_autorizacao(lista):
    print("\n--- solicitar autorização ---")

    for item in lista:
        if item["status"] == "recebido":
            resposta = input(f"Aprovar pagamento de R${item['valor']}? (s/n): ")

            if resposta.lower() == "s":
                item["status"] = "aprovado"
            else:
                item["status"] = "negado"

    salvar(lista)
    print("processo atualizado")


def efetuar_pagamento(lista):
    print("\n--- efetuar pagamento ---")

    for item in lista:
        if item["status"] == "aprovado":
            item["status"] = "pago"
            item["data_pagamento"] = str(datetime.now())

    salvar(lista)
    print("pagamentos efetuados.")


def enviar_contabilidade(lista):
    print("\n--- contabilidade ---")

    with open("relatorio_pagamentos.txt", "w", encoding="utf-8") as f:
        for item in lista:
            f.write(str(item) + "\n")

    print("relatorio enviado para contabilidade")


def menu():
    lista = carregar()

    while True:
        print("""
=====================
SISTEMA DE PAGAMENTOS
=====================
1 - receber documentos
2 - conferir liberação
3 - solicitar autorização
4 - efetuar pagamento
5 - contabilidade
6 - sair
""")

        opcao = input("escolha: ")

        if opcao == "2":
            conferir_liberacao(lista)

        elif opcao == "3":
            solicitar_autorizacao(lista)

        elif opcao == "4":
            efetuar_pagamento(lista)

        elif opcao == "5":
            enviar_contabilidade(lista)

        elif opcao == "6":
            print("Encerrando...")
            break

        else:
            print("Opção inválida")


menu()