# Requisitos do Marco 4: persistência com SQLite

Projeto: CLI de finanças pessoais
Branch: `feature/marco-4-sqlite` (a partir da `develop`)
Conceitos: valor padrão de parâmetro, SQL básico (`CREATE TABLE`, `INSERT`, `SELECT`, `DELETE`, `WHERE`), módulo `sqlite3`, chave primária, parâmetros `?`, `commit`, tupla, escopo de variável
Status do marco: **concluído**

## Objetivo

Guardar as transações em um arquivo SQLite: fechar e reabrir o programa **não** apaga os dados. Cada transação passa a ser identificada pelo **`id`** gerado pelo banco, e não mais pela posição na lista.

## Estrutura final

```
src/financas/
├── __init__.py
├── transacao.py       (classe Transacao, agora com id)
├── carteira.py        (classe Carteira, remoção por id)
├── repositorio.py     (classe RepositorioTransacoes, único lugar com SQL)
└── main.py            (menu e interação com o usuário)
```

O arquivo do banco (`financas.db`) é criado na pasta de onde o programa é executado e não vai para o Git.

## Regras gerais

| ID | Regra |
|----|-------|
| RG-01 | **Todo o SQL mora em `repositorio.py`.** `Transacao`, `Carteira` e `main.py` não importam `sqlite3` nem escrevem SQL. |
| RG-02 | **Todo valor vindo do usuário entra no comando por `?`**, com os valores em uma tupla. Nunca montar SQL juntando texto (f-string, `+`, `%`). |
| RG-03 | O repositório recebe o **caminho do banco no construtor**. Isso permite usar `":memory:"` (banco temporário) nos testes do Marco 5. |
| RG-04 | Depois de cada alteração no banco (`CREATE`, `INSERT`, `DELETE`), chamar `commit()` na hora. |
| RG-05 | O repositório e a `Carteira` **levantam** exceções e não imprimem; quem trata e fala com o usuário continua sendo o `main.py`. |
| RG-06 | **Banco primeiro, memória depois**: nas operações que mudam os dois, o repositório é chamado antes da `Carteira`, para que um erro nunca deixe os dois fora de sincronia. |
| RG-07 | **Comportamento preservado**, exceto duas mudanças intencionais: a listagem mostra o **`id`** no lugar da posição, e a remoção pede o **`id`**. |
| RG-08 | Conventional Commits. Um commit por requisito, **exceto** RF-38 e RF-39, que formam um commit só: o menu inteiro passa a depender do repositório, e um commit intermediário deixaria uma opção quebrada. |

## Requisitos funcionais

### Classe `Transacao` e `Carteira` com id (sem banco)

| ID | Requisito | Aceite | Status |
|----|-----------|--------|--------|
| RF-29 | `Transacao` ganha o parâmetro **`id`**, opcional (padrão `None`) e **último** do construtor, guardado em `self.id`. Aceita `None` ou inteiro; qualquer outra coisa levanta `ValueError("Id inválido, informe um id existente.")`. As demais validações não mudam | sem id, `id` é `None`; com `7`, `id == 7`; com `"x"`, `1.5` ou `[]`, `ValueError`; validações antigas intactas | concluído |
| RF-30 | `__str__` passa a começar pelo id (`<id>: data, tipo, categoria, valor`), e `Carteira.listar_transacoes` imprime só o objeto, sem posição. Aviso de carteira vazia igual ao do Marco 3 | carteira com ids 3, 8 e 9 lista `3: ...`, `8: ...`, `9: ...`; o filtro por categoria mostra os **ids reais** | concluído |
| RF-31 | `Carteira.remover_transacao(id_transacao)` remove por **id** e **devolve** a transação removida. Id que não é inteiro (nem `bool`) ou que não existe levanta `ValueError("Id inválido, informe um id existente.")`. O id **não é** o índice da lista | com ids 1, 2 e 3, remover o `2` devolve essa transação e sobram 1 e 3; `99`, `0`, `-1`, `"a"`, `1.5`, `None`, `True` e remover o mesmo id duas vezes levantam `ValueError` e a lista não muda | concluído |

### Classe `RepositorioTransacoes` (em `repositorio.py`)

| ID | Requisito | Aceite | Status |
|----|-----------|--------|--------|
| RF-32 | Construtor `RepositorioTransacoes(caminho_banco)`: abre a conexão (atributo interno `_conexao`) e cria a tabela `transacoes` se não existir, com as colunas `id` (chave primária, `AUTOINCREMENT`), `valor` (`REAL`, maior que zero), `categoria`, `data` e `tipo` (`TEXT`), todas `NOT NULL`, nessa ordem | criar com um caminho novo gera o arquivo e a tabela; criar de novo com o mesmo caminho não dá erro nem apaga dados; `":memory:"` funciona sem criar arquivo | concluído |
| RF-33 | `salvar_transacao_banco(transacao)`: insere `valor`, `categoria`, `data` e `tipo` (o id é gerado pelo banco) e **atribui o id gerado** a `transacao.id`. Não devolve nada. Antes de tocar no banco: se não for `Transacao`, `TypeError("Esperando um objeto Transacao")`; se já tiver id, `ValueError("Transação já salva.")` | o id deixa de ser `None`; duas transações recebem ids diferentes; `Pao d'agua` e `x') --` são gravados como texto comum; salvar o mesmo objeto duas vezes não duplica a linha | concluído |
| RF-34 | `carregar_transacoes_banco()`: devolve uma **lista de objetos `Transacao`**, com o id preenchido, em ordem crescente de id | banco vazio devolve `[]`; salvar 3, remover o id 2 e carregar devolve 2 objetos (ids 1 e 3), com `valor` numérico e os demais campos iguais aos salvos | concluído |
| RF-35 | `remover_transacao_banco(id_transacao)`: remove a linha com aquele id. Id que não é inteiro (nem `bool`) ou que não existe no banco levanta `ValueError("Id inválido, informe um id existente.")`. Não devolve nada | id existente remove a linha; `99`, `0`, `-1`, `"a"`, `1.5`, `None`, `True` e remover o mesmo id duas vezes levantam `ValueError` e nada muda; um id removido nunca é reaproveitado | concluído |
| RF-36 | `fechar_banco()`: fecha a conexão | depois de fechar, reabrir o mesmo arquivo traz os dados salvos | concluído |

### Integração (em `main.py`)

| ID | Requisito | Aceite | Status |
|----|-----------|--------|--------|
| RF-37 | O caminho do banco é a constante `CAMINHO_BANCO = "financas.db"`. No início de `main()`, criar o repositório, carregar as transações salvas e colocá-las na `Carteira` com `adicionar_transacao`. O repositório é criado **uma vez** e passado como argumento às funções que o usam | adicionar transações, sair e reabrir mostra as mesmas, com os mesmos ids | concluído |
| RF-38 | `opcao_adicionar(carteira, repositorio)`: depois de criar a `Transacao` (sem id), chama `salvar_transacao_banco` e só então `adicionar_transacao` da carteira, todos sob o mesmo `try/except ValueError`. O usuário **não informa** o id | dado válido aparece na listagem com id e continua lá ao reabrir; dado inválido mostra a mesma mensagem de antes, sem gravar no banco nem entrar na carteira | concluído |
| RF-39 | `opcao_remover(carteira, repositorio)`: pede o **id** (`"Informe o id da transação: "`); se a conversão para `int` falhar, `"Digite um número inteiro."` e volta ao menu; senão chama `remover_transacao_banco` e depois `remover_transacao` da carteira, e a confirmação só aparece se nenhuma falhou | a transação some da tela e continua removida ao reabrir; `abc`, vazio e `1.5` mostram a mensagem de conversão; `0`, `-1`, `999` e id já removido mostram `"Id inválido, informe um id existente."`, sem mudar nada | concluído |
| RF-40 | Ao escolher `0`, chamar `fechar_banco()` antes de encerrar | o programa encerra sem erro e os dados ficam salvos; opções inválidas antes do `0` não fecham o banco | concluído |
| RF-41 | `.gitignore` com as regras `*.db` e `*.db-journal` (o modelo padrão de Python só cobre `db.sqlite3`, regra de Django) | `git check-ignore -v src/financas.db` aponta a nova regra; `git status` não lista nenhum `.db` | concluído |

## Mapa de integração do `main.py`

| Momento | O que acontece |
|---------|----------------|
| Início | criar o repositório com `CAMINHO_BANCO` → `carregar_transacoes_banco()` → cada `Transacao` entra na `Carteira` |
| 1 adicionar | criar `Transacao` → `salvar_transacao_banco` (ganha id) → `Carteira.adicionar_transacao` |
| 2 listar, 4 total, 5 saldo, 6 filtrar | só a `Carteira` (em memória), sem tocar no banco |
| 3 remover | `remover_transacao_banco(id)` → `Carteira.remover_transacao(id)` |
| 0 sair | `fechar_banco()` |

## Roteiro de verificação (manual)

Executado no fim do marco, fechando e reabrindo o programa. **Todos os itens passaram.**

- Abrir, adicionar 3 transações, sair e abrir de novo: aparecem com os ids 1, 2 e 3.
- Remover a de id do meio, sair e abrir: continua removida e as outras mantêm seus ids.
- Adicionar uma nova depois de remover (do meio e a última): o id novo **não reaproveita** o removido.
- Remover com `abc`, vazio e `1.5`: mensagem de conversão. Com `0`, `-1`, `999` e um id já removido: mensagem de id inválido. Nada muda.
- Categoria com apóstrofo (`Pao d'agua`), `x') --` e `a'; DROP TABLE transacoes; --`: gravadas como texto, sem quebrar e sem apagar a tabela.
- Dados inválidos (valor `abc`, `-5`, `0`, `nan`, `inf`; data `2026-13-40` e `05/11/2026`; tipo `gasto`; categoria vazia e só com espaços): mesmas mensagens do Marco 3 e nada gravado.
- Total de despesas, saldo e filtro com dados vindos do banco: valores batem; o filtro mostra os ids reais; categoria inexistente ou vazia mostra o aviso de lista vazia.
- Opção de menu `abc`, `9`, vazio e `-1`: mensagem de erro, sem cair.
- Apagar o arquivo `.db`: o programa recria um banco vazio, sem erro.
- `git status` não lista nenhum `.db`.

## Decisões de projeto

- **Terceira classe para o banco.** A `Carteira` gerencia o conjunto em memória; o `RepositorioTransacoes` cuida do disco. Trocar de banco no futuro mexe só nele.
- **Identificação por `id`.** A posição muda a cada remoção; o id é estável e é o que o banco usa. Com `AUTOINCREMENT`, um id apagado nunca é reaproveitado.
- **O banco gera o id.** A `Transacao` nasce com `id = None` e recebe o número em `salvar_transacao_banco`; a lida do banco já nasce com id.
- **O id fica no `__str__`**, por ser propriedade da própria transação, e não da posição na lista.
- **Mesma ordem no construtor e na tabela** (`valor, categoria, data, tipo`), para o `INSERT` e o `SELECT` não gerarem confusão. A conversão de cada linha lida passa cada posição ao parâmetro certo, pois o `id` é o primeiro da linha e o último do construtor.
- **Nomes dos métodos do repositório terminam em `_banco`**, para não repetir os da `Carteira` (`remover_transacao`).
- **`data` é guardada como texto `AAAA-MM-DD`**, pois o SQLite não tem tipo de data.
- **O repositório é passado como argumento** às funções do menu: uma variável criada dentro de `main()` não é visível dentro de outra função.
- **Erros do SQLite (`sqlite3.Error`) não são tratados**: só os erros de entrada do usuário.
- **README completo** fica para o fechamento da Fase 1.

## Limitações conhecidas (melhorias futuras)

- Os atributos da `Transacao` são públicos e podem ser alterados depois da criação (por exemplo `transacao.valor = -5`), contornando a validação. A solução é o encapsulamento com `@property`.
- O `id` da `Transacao` aceita `0`, negativos e `bool`; o `valor` também aceita `True`.
- O caminho do banco é **relativo à pasta de execução**: rodar o programa de outra pasta cria outro `financas.db` vazio.
- A memória (`Carteira`) e o banco são duas cópias dos dados: se o arquivo for alterado por fora com o programa aberto, a tela fica desatualizada. Duas execuções ao mesmo tempo também não são tratadas.
- Erros do SQLite (arquivo travado, disco cheio) não são tratados; mudar as colunas da tabela exige apagar ou migrar o `.db`.
- A categoria é guardada com os espaços das pontas (`" a "`); `data` aceita `2026-1-5`.
- Total, saldo e filtro são calculados em Python, e não em SQL (`SUM`, `WHERE`).
- Sem teste automatizado ainda (Marco 5).
- Erros de validação usam `ValueError` genérico; classes de erro próprias seriam uma melhoria.

## Definição de pronto

- [x] `Transacao` e `Carteira` trabalhando com `id` (RF-29 a RF-31).
- [x] `RepositorioTransacoes` implementado (RF-32 a RF-36), sem SQL fora dele.
- [x] Menu integrado ao repositório (RF-37 a RF-40).
- [x] `.gitignore` do banco (RF-41).
- [x] Roteiro de verificação executado.
- [x] Commits em Conventional Commits.

## Próximo marco

**Marco 5:** testes automatizados com `pytest` e a primeira pipeline de CI no GitHub Actions. Os casos dos Marcos 1 a 4 viram testes, e o `":memory:"` permite testar o repositório sem criar arquivo.