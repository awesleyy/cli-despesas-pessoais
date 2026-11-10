# Requisitos do Marco 3: refatorar para POO

Projeto: CLI de finanças pessoais
Branch: `feature/marco-3-poo` (a partir da `develop`)
Conceitos: classes, objetos, `__init__`, `self`, métodos, `__str__`, encapsulamento por convenção, responsabilidade única
Status do marco: **concluído**

## Objetivo

Reorganizar o código em classes **sem mudar o comportamento**. O programa funciona exatamente como no fim do Marco 2: mesmas mensagens, mesmos resultados. Isso é refatorar.

## Estrutura final

```
src/financas/
├── __init__.py
├── transacao.py    (classe Transacao)
├── carteira.py     (classe Carteira)
└── main.py         (menu e interação com o usuário)
```

O módulo `transacoes.py` (funções soltas) foi removido.

## Regras gerais

| ID | Regra |
|----|-------|
| RG-01 | **Comportamento preservado:** nenhuma mensagem, resultado ou fluxo do menu muda. O roteiro de verificação dá o mesmo resultado antes e depois. **Única mudança intencional:** categoria vazia ou só com espaços passa a ser recusada (limitação registrada no Marco 2). |
| RG-02 | A validação mora no **construtor** de `Transacao` e **levanta** `ValueError` com as mesmas mensagens do Marco 2. Uma transação inválida não chega a existir. |
| RG-03 | A `Carteira` é dona da lista de transações. A lista é **interna** (nome com `_` no início, por convenção) e só é manipulada por métodos da própria classe. |
| RG-04 | O `main.py` não acessa a lista interna e não passa lista de um lado para o outro. Ele cria uma `Carteira` e chama métodos. |
| RG-05 | Quem **trata** as exceções e fala com o usuário continua sendo o `main.py` (`try/except`). As classes levantam, não imprimem. A única exceção é o método que lista, que já imprimia no Marco 2. |
| RG-06 | Cada classe tem **uma responsabilidade só**: `Transacao` representa uma transação; `Carteira` gerencia o conjunto. |
| RG-07 | Conventional Commits. Um commit por requisito, **exceto** onde a mudança é atômica: RF-26 e RF-27 formam um commit só, pois o menu inteiro passa a receber a `Carteira` de uma vez e commits intermediários deixariam opções quebradas. |

## Requisitos funcionais

### Classe `Transacao` (em `transacao.py`)

| ID | Requisito | Aceite | Status |
|----|-----------|--------|--------|
| RF-18 | Construtor com `valor`, `categoria`, `data` e `tipo`, guardando os quatro como atributos e **validando** valor, data e tipo (mesmas regras e mensagens dos RF-07 a RF-09) e também a **categoria**: vazia ou só com espaços (qualquer quantidade) é recusada | dados inválidos levantam `ValueError` (mensagens do Marco 2 para valor, data e tipo; mensagem nova para categoria); dados válidos criam o objeto com os quatro atributos preenchidos | concluído |
| RF-19 | Representação em texto do objeto (`__str__`) com **data, tipo, categoria e valor com 2 casas** | `str(transacao)` devolve uma linha de texto, sem posição e sem `print`, igual ao formato do Marco 2 | concluído |

### Classe `Carteira` (em `carteira.py`)

| ID | Requisito | Aceite | Status |
|----|-----------|--------|--------|
| RF-20 | Construtor sem parâmetros que inicia a carteira vazia, com a lista interna (RG-03) | uma `Carteira()` recém-criada não tem transações; duas carteiras são independentes | concluído |
| RF-21 | Método para **adicionar** uma `Transacao` (recebe o objeto, não os campos soltos) | a carteira passa a ter 1 transação a mais, no final, e é o **mesmo objeto** que foi passado; qualquer outro tipo levanta `TypeError` | concluído |
| RF-22 | Método para **listar**: imprime uma transação por linha com **posição (a partir de 0)** e o texto do RF-19; carteira vazia imprime o mesmo aviso do Marco 2 | saída idêntica à do Marco 2; reaproveita o `__str__` | concluído |
| RF-23 | Método para **remover** por posição, com a validação do RF-10 e **devolvendo** a transação removida | posição negativa, inexistente ou não inteira levanta `ValueError` com a mesma mensagem; os demais itens mantêm a ordem | concluído |
| RF-24 | Métodos para **total de despesas** e **saldo**, que **devolvem** o número (sem imprimir) | mesmos resultados do Marco 2; carteira vazia devolve `0` | concluído |
| RF-25 | Método para **filtrar por categoria**, devolvendo uma **nova `Carteira`** com as transações encontradas, **sem alterar** a original | categoria inexistente devolve carteira vazia; o resultado é exibido reaproveitando o método de listar, sem duplicar formatação | concluído |

### Integração (em `main.py`)

| ID | Requisito | Aceite | Status |
|----|-----------|--------|--------|
| RF-26 | O `main()` cria **uma** `Carteira`; as funções das opções recebem a carteira (e não mais a lista) e chamam seus métodos, conforme o mapa de migração abaixo | o menu funciona como antes, em todas as 6 opções; nenhuma referência ao módulo antigo no `main.py` | concluído |
| RF-27 | Na opção de adicionar, o `main` **cria** a `Transacao` e depois a adiciona à carteira; os dois passos ficam sob o tratamento de `ValueError` | valor, data ou tipo inválidos mostram a mesma mensagem de antes e a carteira não muda | concluído |
| RF-28 | Remover o módulo `transacoes.py` depois de tudo migrado | nenhum `import` do módulo antigo no projeto; o menu roda normalmente | concluído |

## Mapa de migração do `main.py` (RF-26 e RF-27)

Mudou só **quem é chamado**: mensagens, fluxo e tratamento de erro continuam como no Marco 2.

| Opção | Antes (Marco 2, módulo `transacoes`) | Agora (Marco 3) |
|-------|--------------------------------------|-----------------|
| 1 adicionar | `adicionar_transacao(lista, valor, categoria, data, tipo)` | criar um objeto `Transacao` com os 4 campos e passá-lo ao método de adicionar da `Carteira` |
| 2 listar | `listar_transacoes(lista)` | método de listar da `Carteira`, sem argumentos |
| 3 remover | `remover_transacao(lista, posicao)` | método de remover da `Carteira`, só com a posição |
| 4 total de despesas | `calcular_total_despesas(lista)` | método da `Carteira`, sem argumentos |
| 5 saldo | `calcular_saldo(lista)` | método da `Carteira`, sem argumentos |
| 6 filtrar | `filtrar_categoria(lista, categoria)` e depois `listar_transacoes` | método de filtrar da `Carteira` (devolve outra `Carteira`) e depois o método de listar **dessa carteira filtrada** |

## Roteiro de verificação (manual)

Rodado no fim do marco comparando a saída do programa do Marco 2 com a do Marco 3: **31 cenários, todos idênticos**.

- Adicionar uma transação válida e listar.
- Valor `abc`, vazio, `0`, `-5`, `nan` e `inf`: mensagem de erro e nada entra.
- Tipo `gasto` e `Despesa`; data `2026-13-40`, `05/11/2026` e vazia: mensagem de erro e nada entra.
- Remover com posição `abc`, vazia, `-1`, `99`, `1.5` e uma posição válida; remover do meio mantendo a ordem.
- Listar com a carteira vazia.
- Total de despesas e saldo (vazio, positivo, zero, negativo e só receitas).
- Filtrar por categoria existente, inexistente, vazia, com maiúscula, em carteira vazia, e conferir que o filtro não altera a carteira.
- Opção de menu `abc`, `9`, vazio e `-1`.
- **(novo no Marco 3)** Categoria vazia, com um espaço e com vários espaços: mensagem de erro e nada entra. Fora da comparação, pois o Marco 2 aceitava.

## Decisões de projeto

- **Duas classes, uma responsabilidade cada.** `Transacao` sabe se validar e se mostrar; `Carteira` sabe gerenciar o conjunto. O menu continua como funções, pois não tem estado a guardar.
- **Objeto válido ou inexistente.** A validação no construtor garante que toda `Transacao` em circulação nasceu correta, sem depender de alguém lembrar de chamar uma função.
- **Lista interna com `_`.** O Python não impede o acesso; o `_` é uma convenção que comunica "use os métodos".
- **A `Carteira` verifica o tipo ao adicionar** e levanta `TypeError`. Esse é um erro de programação, não de entrada do usuário, e por isso o `main` **não** o captura: um `ValueError` tratado esconderia o bug atrás de uma mensagem amigável.
- **O filtro devolve uma nova `Carteira`.** Assim o resultado reaproveita o método de listar e também sabe calcular total e saldo da categoria. Os objetos `Transacao` são os mesmos da original (não há cópia); só a lista é nova.
- **Estado do resultado é local.** O filtro cria a carteira nova em uma variável local, sem deixar atributo na classe nem no objeto.
- **Chamada pelo objeto** (`carteira.metodo()`), e não pela classe com o objeto passado à mão.
- **Migração do `main.py` em um commit só**, pelo caráter atômico da mudança (RG-07).

## Limitações conhecidas (melhorias futuras)

- Os atributos da `Transacao` são públicos e podem ser **alterados depois da criação** (por exemplo `transacao.valor = -5`), contornando a validação do construtor. A solução é o encapsulamento com propriedades (`@property`).
- A categoria é guardada **com os espaços das pontas** (`" a "`), o que pode gerar categorias "diferentes" no filtro. Normalizar ao guardar é uma melhoria possível.
- `data` aceita `2026-1-5` (o `strptime` tolera mês e dia sem zero).
- `valor` aceita `True`, e a posição também (`bool` é subtipo de `int` em Python).
- Dados em memória: somem ao fechar o programa (Marco 4).
- Na lista filtrada, a numeração recomeça em 0 e não corresponde à posição na carteira original, que é a usada para remover.
- Erros de validação ainda usam `ValueError` genérico; classes de erro próprias seriam uma melhoria.

## Definição de pronto

- [x] Classes `Transacao` e `Carteira` implementadas conforme RF-18 a RF-25.
- [x] `main.py` usando apenas a `Carteira` (RF-26 e RF-27).
- [x] `transacoes.py` removido (RF-28).
- [x] Roteiro de verificação com saída igual à do Marco 2 (31 cenários), exceto a mudança intencional da categoria.
- [x] Commits em Conventional Commits.

## Próximo marco

**Marco 4:** persistência com SQLite. O conceito exigido é SQL básico e o módulo `sqlite3`. A persistência é uma responsabilidade nova: a `Carteira` não deve saber de banco de dados, então nasce uma terceira classe para isso.