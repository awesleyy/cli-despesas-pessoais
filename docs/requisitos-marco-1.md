# Requisitos do Marco 1: CRUD em memória

Projeto: CLI de finanças pessoais
Branch: `feature/marco-1-crud-memoria` (mergeada em `develop`, PR #1)
Status do marco: **concluído**

## Convenções do projeto

- **Branches (GitFlow):** `feature/`, `bugfix/`, `chore/`, `release/`, `hotfix/`. Nunca commitar direto em `main` ou `develop`. Merge via Pull Request.
- **Commits (Conventional Commits):** `tipo(escopo): descrição no imperativo, minúscula, sem ponto final`. Tipos: `feat`, `fix`, `docs`, `refactor`, `test`, `chore`, `ci`, `style`. Escopo opcional (passa a valer a partir do Marco 3).
- **Um commit por assunto**, logo depois de escrevê-lo e verificá-lo.

## Regras gerais

| ID | Regra |
|----|-------|
| RG-01 | Cada transação é um **dicionário** com 4 chaves: `valor` (número maior que zero), `categoria` (texto), `data` (texto `AAAA-MM-DD`, com hífens) e `tipo` (`"receita"` ou `"despesa"`, em minúsculas). |
| RG-02 | As transações ficam em uma **lista**. Nenhuma função usa variável global: a lista entra sempre como **primeiro parâmetro**. |
| RG-03 | Cada função tem **uma responsabilidade só**. Funções que calculam ou filtram não imprimem, apenas **devolvem**. Só `listar_transacoes` imprime. |
| RG-04 | Validação de entrada (valor negativo, tipo inválido, data inválida, posição inexistente) **fica fora deste marco**. Entra no Marco 2. |

## Requisitos funcionais

Todas as funções estão em `src/financas/transacoes.py`.

| ID | Função | Recebe | Devolve | Aceite | Status |
|----|--------|--------|---------|--------|--------|
| RF-01 | `adicionar_transacao` | lista, valor, categoria, data, tipo | nada (altera a lista) | a lista ganha 1 item no final | concluído |
| RF-02 | `listar_transacoes` | lista | nada (imprime) | uma linha por transação: posição (a partir de 0), data, tipo, categoria, valor com 2 casas; lista vazia imprime aviso e encerra | concluído |
| RF-03 | `remover_transacao` | lista, posição | a transação removida | a lista fica com 1 item a menos, ordem mantida | concluído |
| RF-04 | `calcular_total_despesas` | lista | total das despesas | receitas não entram; sem despesas ou lista vazia devolve `0` | concluído |
| RF-05 | `calcular_saldo` | lista | receitas menos despesas | 1000 de receita e 300 de despesa resultam em 700; pode ser negativo; lista vazia devolve `0` | concluído |
| RF-06 | `filtrar_categoria` | lista, categoria | **nova lista** com as encontradas | sempre devolve lista (vazia se nada achar); a original não é alterada | concluído |

## Definição de pronto do marco

- [x] Os 6 requisitos implementados.
- [x] Funções verificadas manualmente (casos de borda: lista vazia, só receitas, saldo negativo, categoria inexistente). **Testes automatizados entram no Marco 5.**
- [x] Um commit por função, em Conventional Commits.
- [x] Branch `feature/marco-1-crud-memoria` mergeada em `develop` via PR.
- [x] Estrutura reorganizada em `src/financas/`, `tests/` e `docs/` (branch `chore/estrutura-do-projeto`).
- [x] `python -m financas.main`, rodado de dentro de `src`, executa sem erro.

## Casos para virar testes no Marco 5

- Saldo com 1000 de receita e 300 de despesa: 700
- Saldo com despesas maiores que receitas: negativo
- Saldo e total de despesas com lista vazia: 0
- Total de despesas só com receitas: 0
- Filtro com categoria inexistente: `[]`
- `len` da lista original igual antes e depois do filtro
- Remover devolve a transação e mantém a ordem dos demais

## Pendências para o Marco 2

- Validar `valor`, `tipo`, `data` e posição (RG-04).
- Menu interativo no `main.py`.
- Tratamento de erros com `try/except`.