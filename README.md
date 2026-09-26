# Sistema de Controle de Estacionamento

Projeto desenvolvido em Python para simular o controle básico de um estacionamento pelo terminal.

O sistema permite registrar a entrada de veículos, armazenar a placa e o tempo de permanência, listar e buscar veículos estacionados, registrar saídas, calcular o valor a pagar e gerar um relatório da operação.

## Funcionalidades

- Registrar entrada de veículos
- Impedir o cadastro duplicado de uma placa já estacionada
- Listar os veículos estacionados
- Buscar veículo pela placa
- Registrar a saída de veículos
- Calcular automaticamente o valor a pagar
- Exibir o total acumulado em caixa
- Exibir a quantidade de veículos estacionados
- Exibir a quantidade de veículos que já saíram
- Validar entradas numéricas com `try/except`

## Regras de cobrança

O valor é calculado de acordo com o tempo informado:

- Até 2 horas: R$ 8,00 por hora
- De 3 a 5 horas: R$ 6,00 por hora
- Acima de 5 horas: R$ 5,00 por hora

## Tecnologias utilizadas

- Python 3

## Conceitos utilizados

- Variáveis
- Listas
- Dicionários
- Funções
- Estruturas condicionais
- Laços de repetição
- Entrada e saída de dados
- Tratamento de exceções com `try/except`

## Como executar

1. Clone este repositório:

```bash
git clone https://github.com/natanaelliberato/controle-estacionamento.git
```

2. Acesse a pasta do projeto:

```bash
cd controle-estacionamento
```

3. Execute o programa:

```bash
python3 estacionamento.py
```

## Demonstração

O programa é executado diretamente pelo terminal através de um menu com opções para registrar entradas, listar e buscar veículos, registrar saídas, consultar o relatório e encerrar o sistema.
