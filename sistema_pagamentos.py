import json
from datetime import datetime
import os

arquivo = "pagamento.json"



def carregar():
    if os.path.exists(arquivo):
        with open(arquivo, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []


def salvar(dados):
    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)



def receber_documentos(lista):
    print("\n--- receber documentos ---")

    fornecedor = input("Fornecedor: ")
    valor = float(input("Valor: "))

    lista.append({
        "fornecedor": fornecedor,
        "valor": valor,
        "status": "recebido"
    })

    salvar(lista)
    print("documento registrado com sucesso")



def conferir_liberacao(lista):
    print("\n--- conferir liberação ---")

    encontrou = False

    for item in lista:
        if item["status"] == "recebido":
            print(item)
            encontrou = True

    if not encontrou:
        print("Nenhum pagamento recebido.")



def solicitar_autorizacao(lista):
    print("\n--- solicitar autorização ---")

    for item in lista:
        if item["status"] == "recebido":
            resposta = input(f"Aprovar pagamento de R$ {item['valor']}? (s/n): ")

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

    if not lista:
        print("Nenhum dado para relatório.")
        return

    with open("relatorio_pagamentos.txt", "w", encoding="utf-8") as f:
        f.write("RELATÓRIO DE PAGAMENTOS\n")
        f.write("=" * 40 + "\n\n")

        total = 0

        for item in lista:
            f.write(f"Fornecedor: {item.get('fornecedor', 'N/A')}\n")
            f.write(f"Valor: R$ {item.get('valor', 0)}\n")
            f.write(f"Status: {item.get('status', 'N/A')}\n")

            if item.get("status") == "pago":
                total += item.get("valor", 0)

            if "data_pagamento" in item:
                f.write(f"Data pagamento: {item['data_pagamento']}\n")

            f.write("-" * 40 + "\n")

        f.write(f"\nTOTAL PAGO: R$ {total}\n")

    print("relatório enviado para contabilidade")


def menu():
    while True:
        lista = carregar()

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

        if opcao == "1":
            receber_documentos(lista)

        elif opcao == "2":
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