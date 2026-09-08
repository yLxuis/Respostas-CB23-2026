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

## 2. Relação entre Restaurante e Iguaria

A relação entre `Restaurante` e `Iguaria` pode ser modelada como uma agregação.

Um restaurante pode possuir várias iguarias em seu cardápio. Assim, a classe `Restaurante` poderia possuir uma lista:

`Iguarias: list[Iguaria]`

A multiplicidade seria `0..*`, indicando que um restaurante pode possuir nenhuma ou várias iguarias.

## 3. Tipos dos argumentos

### Argumento 1

O `argumento1` poderia ser uma lista de `Iguaria`: `list[Iguaria]`

Isso ocorre porque um pedido pode envolver uma ou várias iguarias.

### Argumento 2

O `argumento2` poderia ser uma instância de `Funcionário`: `funcionário`

Assim, o gerente poderia demitir qualquer funcionário, como um `Garçom` ou um `Chefe de cozinha`.

