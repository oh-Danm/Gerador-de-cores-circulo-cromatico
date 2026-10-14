# Programa simples de geração de cores de uma color wheel

## Sobre
Esse serve para a criação de paletas de cores com base na roda cromática da cor de entrada.

## Funcionamento
Para executar o programa basta compilá-lo com o python3 instalado com o comando:

```
python3 <nome-do-arquivo(adobe.py)>
```

*Nota: o código foi feito na versão 3.10.12 do Python, então verifique se sua versão do Python é compatível.*

### Execução
Ao executar, o programa irá pedir o valor de red, green e blue do padrão rgb.

```
R: <valor-red>
G: <valor-green>
B: <valor-blue>
```

Depois, o programa abrirá um "menu" para selecionar a paleta desejada:

```
Escolha o tipo de paleta de cores:
1-Complementar
2-Análogas
3-Triádicas
4-Split-complementares
5-Tetrádicas (retângulo)
6-Quadradas
```

E por fim, o programa irá retornar o código hex e os valores em rgb das cores da paleta e da cor original

###### Exemplo
```
Complementar: rgb(17, 16, 15)
Hex = #11100f
Original: rgb(15, 16, 17)
Hex = #0f1011
```