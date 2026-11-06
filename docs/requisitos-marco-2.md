# Requisitos do Marco 2: validação e menu interativo

Projeto: CLI de finanças pessoais
Branch: `feature/marco-2-validacao-menu` (a partir da `develop`)
Conceitos: exceções (`raise`, `try/except`), `input()`, laço `while`, organização de funções
Status do marco: **requisitos implementados** (falta o teste manual geral)

## Regras gerais

| ID | Regra |
|----|-------|
| RG-01 | A validação mora em `transacoes.py`: a função **levanta** uma exceção com mensagem clara. Ela **não imprime** e não decide o que fazer com o erro. Pode capturar um erro do Python apenas para **relançá-lo** com mensagem própria (caso da data). |
| RG-02 | Quem **trata** a exceção e fala com o usuário é o `main.py`. O programa **nunca** cai por entrada inválida. |
| RG-03 | Capture só o tipo de erro esperado (`except ValueError`, por exemplo). Nada de `except` sem tipo. O `try` envolve só o trecho que pode falhar, e cada ponto de falha distinto tem o seu `try/except`. |
| RG-04 | Os dados continuam em memória (SQLite entra no Marco 4). A lista de transações é criada no `main()` e **passada como parâmetro**, sem variável global. |
| RG-05 | Conventional Commits, um commit por requisito (ou por opção do menu, quando cada uma tem lógica própria). |

## Requisitos funcionais

### Validações (em `transacoes.py`)

| ID | Onde | Regra | Aceite | Status |
|----|------|-------|--------|--------|
| RF-07 | `adicionar_transacao` | `valor` é `int` ou `float` maior que zero | `0`, negativo e texto levantam `ValueError`; a lista não muda | concluído |
| RF-08 | `adicionar_transacao` | `tipo` é `"receita"` ou `"despesa"` | qualquer outro valor (inclusive `"Despesa"`) levanta `ValueError`; a lista não muda | concluído |
| RF-09 | `adicionar_transacao` | `data` é uma data real no formato `AAAA-MM-DD` | `2026-13-40` e `05/11/2026` levantam `ValueError`; a lista não muda | concluído |
| RF-10 | `remover_transacao` | posição é inteira e existe na lista | negativa, igual ou maior que o tamanho da lista e texto levantam `ValueError` | concluído |

### Menu (em `main.py`)

| ID | Requisito | Aceite | Status |
|----|-----------|--------|--------|
| RF-11 | Menu em laço com as opções: adicionar, listar, remover, total de despesas, saldo, filtrar por categoria e sair | o menu volta a aparecer depois de cada ação; `0` encerra | concluído |
| RF-12 | Opção inválida no menu (letra, número fora da lista, vazio) | mensagem de erro e volta ao menu, sem cair | concluído |
| RF-13 | `exibir_menu()`: função que **só imprime** o menu | o `main()` não tem nenhum `print` de opção do menu | concluído |
| RF-14 | Roteamento no `main()` com `if/elif/else`: o `main()` cria a lista, mostra o menu, lê a opção e **chama** a função da opção escolhida | `main()` só com laço e roteamento; opção inválida cai no `else`, sem checagem de intervalo separada | concluído |
| RF-15 | Uma função por opção (`opcao_adicionar`, `opcao_listar`, `opcao_remover`, `opcao_total_despesas`, `opcao_saldo`, `opcao_filtrar`), cada uma **recebendo a lista como parâmetro** | adicionar uma opção nova muda só o menu, uma função e um `elif` | concluído |
| RF-16 | Entradas do usuário tratadas: conversão do valor e da posição, e as exceções dos RF-07 a RF-10 | mensagem clara e volta ao menu; a transação inválida **não** é adicionada | concluído |
| RF-17 | Confirmação depois de cada operação bem-sucedida (adicionar e remover) | a mensagem aparece **só** se não houve exceção | concluído |

### Detalhamento do RF-16 por opção

| Opção | Pontos de falha | Tratamento |
|-------|-----------------|------------|
| 1 adicionar | conversão do `valor` (`float`); chamada a `adicionar_transacao` (valor, data e tipo) | dois `try/except` separados; `return` após falha da conversão; mensagem da própria exceção na chamada |
| 3 remover | conversão da posição (`int`); chamada a `remover_transacao` | dois `try/except` separados; `return` após falha da conversão; mensagem da própria exceção na chamada |
| 2, 4, 5, 6 | nenhum (sem conversão e sem exceção possível) | RF-16 não se aplica; apenas chamam a lógica e exibem o resultado |

## Decisões de projeto

- **Quem levanta e quem trata:** `transacoes.py` levanta `ValueError`; `main.py` captura e mostra. Assim a mesma lógica serve a uma API no futuro (Fase 2).
- **`try/except` na lógica só para traduzir:** o `strptime` levanta um `ValueError` técnico; a função captura e relança o seu, sem imprimir.
- **Confirmação dentro do `try`**, logo depois da chamada, para só rodar se ela não falhou.
- **Exibição do saldo negativo:** `-R$ 300.00`.
- **Filtro:** reaproveita `listar_transacoes` para exibir o resultado.

## Limitações conhecidas (melhorias futuras)

- `categoria` aceita texto vazio (nenhum requisito a valida). Se for tratar, a regra vai em `transacoes.py` com `raise ValueError`, e o `except` já existente no `main` cobre sem código novo.
- `data` aceita `2026-1-5` (o `strptime` tolera mês e dia sem zero).
- `valor` aceita `True`, porque `bool` é subtipo de `int` em Python.
- `data` igual a `None` levanta `TypeError` (o `strptime` só aceita texto). No menu isso não ocorre, pois o `input()` sempre devolve texto.
- Na lista filtrada, a numeração recomeça em 0 e **não** corresponde à posição na lista geral, que é a usada para remover.
- Dados em memória: somem ao fechar o programa (resolvido no Marco 4).

## Definição de pronto

- [x] Validações em `transacoes.py`, sem `print` dentro delas.
- [x] Menu estruturado conforme RF-13 a RF-15.
- [x] Entradas tratadas (RF-16) e confirmações (RF-17).
- [x] Commits em Conventional Commits.
- [x] Teste manual geral: digitar lixo (`abc`, vazio, negativos, espaços) em **cada** entrada, sem derrubar o programa.

## Casos para virar testes no Marco 5

- valor `0`, `-5`, `"abc"` na adicionar; `100` (inteiro) e `50.5` aceitos
- tipo `"Despesa"` (maiúscula) e `"gasto"`
- data `2026-13-40`, `05/11/2026` e vazia
- remover com posição `-1`, `99`, `"a"` e uma posição válida
- a lista **não muda** quando a validação falha
- opção do menu `abc`, `9`, vazia e `0`
- saldo positivo, zero, vazio e negativo
- filtro com categoria existente, inexistente e vazia

## Próximo marco

**Marco 3:** refatorar para POO (classes `Transacao` e `Carteira`), separando responsabilidades. O conceito exigido é classes, métodos e encapsulamento. Os casos desta lista viram o critério de aceite para garantir que nada quebra na refatoração.