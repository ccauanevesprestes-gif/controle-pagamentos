
Sistema de Pagamentos

 Descrição

Este projeto é um sistema simples de pagamentos desenvolvido em Python. Ele simula o fluxo de um processo de pagamento dentro de uma empresa, desde a conferência dos documentos até a geração de um relatório para a contabilidade.

Os dados dos pagamentos são armazenados em um arquivo JSON, permitindo que as informações permaneçam salvas mesmo após o programa ser encerrado.

 Funcionalidades

O sistema oferece as seguintes opções:

 Conferir pagamentos recebidos
 Solicitar autorização para realizar os pagamentos
 Efetuar os pagamentos aprovados
 Gerar um relatório para a contabilidade
 Armazenar todas as informações em um arquivo `pagamento.json

 Estrutura do projeto

```
.
├── pagamento.json              # Armazena os dados dos pagamentos
├── relatorio_pagamentos.txt    # Relatório gerado para a contabilidade
└── sistema_pagamentos.py       # Código principal
```

Como executar

1. Certifique-se de ter o Python 3 instalado.
2. Coloque o arquivo `pagamento.json` na mesma pasta do programa.
3. Execute o arquivo pelo terminal:

bash
python sistema_pagamentos.py


Funcionamento

Ao iniciar o programa, será exibido um menu com as seguintes opções:

1 - Receber documentos
2 - Conferir liberação
3 - Solicitar autorização
4 - Efetuar pagamento
5 - Contabilidade
6 - Sair



As demais opções funcionam da seguinte forma:

Conferir liberação:exibe todos os pagamentos que possuem o status recebido
  Solicitar autorização: solicita ao usuário a aprovação ou negação de cada pagamento recebido.
  Efetuar pagamento: altera o status dos pagamentos aprovados para pago e registra a data e hora do pagamento.
  Contabilidade: gera um arquivo chamado relatorio_pagamentos.txt` contendo todas as informações dos pagamentos.

Estrutura dos dados

Cada pagamento é armazenado em formato JSON, semelhante ao exemplo abaixo:

json

    fornecedor: "Empresa ABC
    valor: 1500
    status: recebido



Após a aprovação e pagamento, um novo campo é adicionado:

json

    fornecedor: Empresa ABC
    valor: 1500
    status: pago
    data_pagamento: 2026-06-26 14:35:20.123456


 Bibliotecas utilizadas

O projeto utiliza apenas bibliotecas padrão do Python:

json para leitura e gravação dos dados.
os para verificar se o arquivo JSON existe.
datetime para registrar a data e a hora do pagamento.

 Observações

Este projeto foi desenvolvido com fins de estudo para praticar conceitos como

Manipulação de arquivos JSON.
 Organização do código em funções.
 Estruturas de repetição e decisão.
 Persistência de dados.
Criação de menus interativos no terminal.

Como melhoria futura, pode ser implementada a opção de receber documentos, além de funcionalidades como cadastro de pagamentos, exclusão, edição e busca por fornecedor ou status.
