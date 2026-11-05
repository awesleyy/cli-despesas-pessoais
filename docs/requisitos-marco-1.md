# Requisitos do Marco 1: CRUD em memória

Projeto: CLI de finanças pessoais
Branch: `feature/marco-1-crud-memoria`

## Convenções do projeto

- **Branches (GitFlow):** `feature/`, `bugfix/`, `release/`, `hotfix/`. Nunca commitar direto em `main` ou `develop`. Merge via Pull Request.
- **Commits (Conventional Commits):** `tipo(escopo): descrição no imperativo, minúscula, sem ponto final`. Tipos: `feat`, `fix`, `docs`, `refactor`, `test`, `chore`, `ci`, `style`.
- **Um commit por função**, logo depois de escrevê-la e testá-la.

## Regras gerais

| ID | Regra |
|----|-------|
| RG-01 | Cada transação é um **dicionário** com 4 chaves: `valor` (número maior que zero), `categoria` (texto), `data` (texto `AAAA-MM-DD`, com hífens) e `tipo` (`"receita"` ou `"despesa"`, em minúsculas). |
| RG-02 | As transações ficam em uma **lista**. Nenhuma função usa variável global: a lista entra sempre como **primeiro parâmetro**. |
| RG-03 | Cada função tem **uma responsabilidade só**. Funções que calculam ou filtram não imprimem, apenas **devolvem**. Quem imprime é a `listar` e o código de teste no final do arquivo. |
| RG-04 | Validação de entrada (valor negativo, tipo inválido, data inválida, posição inexistente) **fica fora deste marco**. Entra no Marco 2. |

## Requisitos funcionais

### RF-01: Adicionar transação
- **Recebe:** lista, `valor`, `categoria`, `data`, `tipo`.
- **Faz:** monta o dicionário e o coloca no **final** da lista.
- **Devolve:** nada (a lista original é alterada).
- **Aceite:** a lista ganha 1 item, e o último é a transação adicionada.
- **Status:** concluído (`adicionar_transacao`).

### RF-02: Listar transações
- **Recebe:** lista.
- **Faz:** imprime uma transação por linha: **posição, data, tipo, categoria, valor** (2 casas decimais).
- **Lista vazia:** imprime um aviso e encerra, sem erro.
- **Devolve:** nada.
- **Aceite:** a posição começa em **0** e é a mesma usada pelo RF-03.
- **Status:** concluído (`listar_transacoes`).

### RF-03: Remover transação
- **Recebe:** lista, **posição**.
- **Faz:** remove a transação dessa posição.
- **Devolve:** a transação removida.
- **Aceite:** a lista fica com 1 item a menos, e os demais mantêm a ordem.
- **Status:** concluído (`remover_transacao`).

### RF-04: Total de despesas
- **Recebe:** lista.
- **Faz:** soma o `valor` apenas de `tipo == "despesa"`.
- **Devolve:** o total (número).
- **Sem despesas / lista vazia:** devolve `0`.
- **Aceite:** receitas **não** entram na soma.
- **Status:** concluído (`calcular_total_despesas`).

### RF-05: Saldo
- **Recebe:** lista.
- **Faz:** total de receitas **menos** total de despesas.
- **Devolve:** o saldo (pode ser negativo).
- **Lista vazia:** devolve `0`.
- **Aceite:** 1 receita de 1000 e 1 despesa de 300 resultam em saldo 700.
- **Status:** pendente.

### RF-06: Filtrar por categoria
- **Recebe:** lista, nome da categoria.
- **Faz:** seleciona as transações cuja `categoria` é igual à informada (comparação exata, sensível a maiúsculas).
- **Devolve:** uma **nova lista** com as encontradas, **sempre** (inclusive quando vazia). A lista original **não** é alterada.
- **Nenhuma encontrada:** devolve lista vazia `[]`.
- **Aceite:** `len` da lista original é o mesmo antes e depois do filtro.
- **Status:** em revisão (`filtrar_categoria`).

## Definição de pronto do marco

- [ ] Os 6 requisitos implementados em `main.py`.
- [ ] Pelo menos 5 transações de teste (receitas e despesas, 2 ou mais categorias), com uma chamada por função e `print` dos resultados.
- [ ] Um commit por função, em Conventional Commits.
- [ ] Tudo na branch `feature/marco-1-crud-memoria`, com Pull Request para `develop`.

## Ordem de implementação

RF-01, RF-02, RF-03, RF-04, RF-06, RF-05.