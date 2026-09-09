# Aula 05 - Respostas

## 1. Relações de herança

As classes podem ser organizadas nas seguintes hierarquias:

- `Pessoa` é uma classe base para `Funcionário`,
- `Funcionário` é uma subclasse de `Pessoa`,
- `Garçom`, `Chefe de cozinha` e `Gerente` são subclasses de `Funcionário`.
- `Pizza` e `Bolo` são subclasses de `Iguaria`,
- `Pizzaria` é uma subclasse de `Restaurante`.

### Herança de Pessoa para Funcionário

A classe `Funcionário` herdaria os atributos `nome` e `idade` da classe `Pessoa`. Além disso, possuiria os atributos próprios `salario` e `carga_horaria`.

### Herança de Funcionário para seus funcionários

AS classes `Garçom`, `Chefe de cozinha` e `Gerente` herdariam de `Funcionário` os atributos `nome`, `idade`, `salario` e `carga_horaria`.

Além disso, cada um possuiria seu próprio método:

- `Garçom`: `anotar_pedido()`
- `Chefe de cozinha`: `preparar()`
- `Gerente`: `demitir()`

As classes `Pizza` e `Bolo` herdariam de `Iguaria` os atributos `nome` e `preço`.

Além disso, cada um possuiria seu próprio atributo:

- `Pizza`: `borda_recheada`
- `Bolo`: `formato`

`Pizzaria` herdaria de `Restaurante` seus atributos `nome`, `endereço` e `telefone`

Além de possuir seu próprio atributo:

- `Pizzaria`: `rodizio`.

## 2. Relação entre Restaurante e Iguaria

A relação entre `Restaurante` e `Iguaria` pode ser modelada como uma agregação.

Um restaurante pode possuir várias iguarias em seu cardápio. Assim, a classe `Restaurante` poderia possuir uma lista:

`Iguarias: list[Iguaria]`

A multiplicidade seria `0..*`, indicando que um restaurante pode possuir nenhuma ou várias iguarias.

A classe `Iguaria` não precisa necessariamente deixar de existir caso um restaurante seja removido, pois uma iguaria pode ser representada independentemente do restaurante. Por isso, a agregação é mais adequada do que uma composição forte.

## 3. Tipos dos argumentos

### Argumento 1

Para `argumento1`, seria adequado utilizar uma instância da classe `Pedido`. Um pedido pode conter uma ou várias iguarias, portanto a classe `Pedido` poderia possuir uma lista de iguarias.

Assim:
`anotar_pedido(pedido: Pedido)`

### Argumento 2

Para `argumento2`, seria adequado utilizar uma instância de `Iguaria`, pois o chefe de cozinha prepara uma comida específica. Como `Pizza` e `Bolo` são subclasses de `Iguaria`, o método também poderá receber objetos dessas classes.

Assim:
`preparar(iguaria: Iguaria)`

### Argumento 3

Para `argumento3`, seria adequado utilizar uma instância de `Funcionario`, pois o gerente demite funcionários. Dessa forma, o metódo poderá receber `Garçom`, `Chefe de cozinha` ou qualquer outra subclasse de `Funcionário`.

Assim:
`demitir(funcionario: Funcionario)`
