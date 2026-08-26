import colorsys as cor

#conversor de rgb para hex
def hexadecimal(r, g, b):
    #inicialização de cada seção do hex como uma string vazia
    h = ""
    h1 = ""
    h2 = ""
    h3 = ""
    h += "#"

    #verificar se o valor de red é zero, se for, adicionar direto no hex, senão calcular o valor em hex
    if r==0:
        h1+="00"
    else:
        while r > 0:
            a = r%16
            r = r//16
            if a >= 10:
                h1 += chr((a-10)+ord("A"))
            else:
                h1 += str(a)

    #a mesma coisa para green
    if g==0:
        h2+="00"
    else:
        while g > 0:
                a = g%16
                g = g//16
                if a >= 10:
                    h2 += chr((a-10)+ord("A"))
                else:
                    h2 += str(a)

    #e para blue
    if b==0:
        h3+="00"
    else:
        while b > 0:
                a = b%16
                b = b//16
                if a >= 10:
                    h3 += chr((a-10)+ord("A"))
                else:
                    h3 += str(a)

    #inverter as strings de red, green e blue
    h1 = h1[::-1]
    h2 = h2[::-1]
    h3 = h3[::-1]
    #e adicionar no resultado
    h += h1 + h2 + h3
    return h     

#conversor de rgb para hsv
def hsv(r, g, b):
    r1 = r / 255.0 
    g1 = g / 255.0
    b1 = b / 255.0
    return cor.rgb_to_hsv(r1, g1, b1)

#conversor de hsv para rgb (ignore a incoerência)
def volta(h, s, v):
    r, g, b = cor.hsv_to_rgb(h, s, v)
    return (round(r*255), round(g*255), round(b*255))

#função para somar hue com o grau de rotação
def soma(h, grau):
    return (h + (grau/360))%1.0

#função para gerar cores complementares
def cor_comp(r, g, b):
    #converte os valores de rgb para hsv
    h,s,v = hsv(r,g,b)

    #soma o hue com 180 graus para gerar a cor complementar
    h_comp = soma(h, 180)

    #retorna o valor em rgb
    return volta(h_comp, s, v)

#função para gerar cores análogas
def cor_ana(r, g, b, offset):
    #converte os valores de rgb para hsv
    h,s,v = hsv(r,g,b)

    #soma e subtrai o hue com o valor do offset para gerar as cores análogas
    h_ana_menos = soma(h, -offset)
    h_ana_mais = soma(h, offset)

    #retorna os valores em rgb
    return volta(h_ana_menos, s, v), volta(h_ana_mais, s, v) 

#função para gerar cores triádicas
def cor_tri(r,g,b):
    #converte os valores de rgb para hsv
    h,s,v = hsv(r,g,b)

    #soma o hue com 120 e 240 graus para gerar as cores triádicas
    h_tri1 = soma(h, 120)
    h_tri2 = soma(h, 240)

    #retorna os valores em rgb
    return volta(h_tri1, s, v), volta(h_tri2, s, v)

#função para gerar cores split-complementares
def split_comp(r,g,b):
    #converte os valores de rgb para hsv
    h,s,v = hsv(r,g,b)

    #soma o hue com 150 e 210 graus para gerar as cores split-complementares
    h_comp1 = soma(h, 150)
    h_comp2 = soma(h, 210)

    #retorna os valores em rgb
    return volta(h_comp1, s, v), volta(h_comp2, s, v)

#função para gerar cores tetrádicas (retangulares)
def cor_tetra(r,g,b):
    #converte os valores de rgb para hsv
    h,s,v = hsv(r,g,b)

    #soma o hue com 60, 180 e 240 graus para gerar as cores tetrádicas
    h_t1 = soma(h, 60)
    h_t2 = soma(h, 180)
    h_t3 = soma(h, 240)

    #retorna os valores em rgb
    return volta(h_t1,s,v), volta(h_t2,s,v), volta(h_t3,s,v)

#função para gerar cores quadradas
def cor_quad(r,g,b):
    #converte os valores de rgb para hsv
    h,s,v = hsv(r,g,b)

    #soma o hue com 90, 180 e 270 graus para gerar as cores quadradas
    h_q1 = soma(h, 90)
    h_q2 = soma(h, 180)
    h_q3 = soma(h, 270)

    #retorna o valor em rgb
    return volta(h_q1, s, v), volta(h_q2, s, v), volta(h_q3, s, v)

#chamada de input do usuário
print("R: ")
r = int(input())
print("G: ")
g = int(input())
print("B: ")
b = int(input())

#variável para armazenamento da escolha do usuário
opt = 0
while True:
    #menu de escolhas
    print("Escolha o tipo de paleta de cores:")
    print("1-Complementar")
    print("2-Análogas")
    print("3-Triádicas")
    print("4-Split-complementares")
    print("5-Tetrádicas (retângulo)")
    print("6-Quadradas")

    opt = int(input())

    #opção de cor complementar
    if opt == 1:
        #chamada da função de gerar cores complementares
        cor1 = cor_comp(r, g, b)

        #impressão do valor da cor em rgb
        print("Complementar: "+str(cor1))
        hexa = hexadecimal(cor1[0], cor1[1], cor1[2])
        #impressão do valor da cor em hex
        print("Hex = "+hexa)
        break

    #opção de cores análogas
    elif opt == 2:
        print("Digite o valor do offset (em radianos): ")
        offset = int(input())
        #chamada da função de gerar cores complementares
        cor1, cor2 = cor_ana(r, g, b, offset)

        #impressão do valor da cor em rgb
        print("Análoga1: "+str(cor1))
        hexa = hexadecimal(cor1[0], cor1[1], cor1[2])
        #impressão do valor da cor em hex
        print("Hex = "+hexa)

        #impressão do valor da cor em rgb
        print("Análoga2: "+str(cor2))
        hexa = hexadecimal(cor2[0], cor2[1], cor2[2])
        #impressão do valor da cor em hex
        print("Hex = "+hexa)

        break

    #opção de cores triádicas
    elif opt == 3:
        #chamada da função de gerar cores complementares
        cor1, cor2 = cor_tri(r, g, b)

        #impressão do valor da cor em rgb
        print("Triádica1: "+str(cor1))
        hexa = hexadecimal(cor1[0], cor1[1], cor1[2])
        #impressão do valor da cor em hex
        print("Hex = "+hexa)

        #impressão do valor da cor em rgb
        print("Triádica2: "+str(cor2))
        hexa = hexadecimal(cor2[0], cor2[1], cor2[2])
        #impressão do valor da cor em hex
        print("Hex = "+hexa)
        break

    #opção de cores split-complementares
    elif opt == 4:
        #chamada da função de gerar cores complementares
        cor1, cor2 = split_comp(r, g, b)

        #impressão do valor da cor em rgb
        print("Split-complementar1: "+str(cor1))
        hexa = hexadecimal(cor1[0], cor1[1], cor1[2])
        #impressão do valor da cor em hex
        print("Hex = "+hexa)

        #impressão do valor da cor em rgb
        print("Split-complementar2: "+str(cor2))
        hexa = hexadecimal(cor2[0], cor2[1], cor2[2])
        #impressão do valor da cor em hex
        print("Hex = "+hexa)
        break

    #opção de cores tetrádicas (retangulares)
    elif opt == 5:
        #chamada da função de gerar cores complementares
        cor1, cor2, cor3 = cor_tetra(r, g, b)

        #impressão do valor da cor em rgb
        print("Tetrádica1: "+str(cor1))
        hexa = hexadecimal(cor1[0], cor1[1], cor1[2])
        #impressão do valor da cor em hex
        print("Hex = "+hexa)

        #impressão do valor da cor em rgb
        print("Tetrádica2: "+str(cor2))
        hexa = hexadecimal(cor2[0], cor2[1], cor2[2])
        #impressão do valor da cor em hex
        print("Hex = "+hexa)

        #impressão do valor da cor em rgb
        print("Tetrádica3: "+str(cor3))
        hexa = hexadecimal(cor3[0], cor3[1], cor3[2])
        #impressão do valor da cor em hex
        print("Hex = "+hexa)
        break

    #opção de cores quadradas
    elif opt == 6:
        #chamada da função de gerar cores complementares
        cor1, cor2, cor3 = cor_quad(r, g, b)

        #impressão do valor da cor em rgb
        print("Quadrada1: "+str(cor1))
        hexa = hexadecimal(cor1[0], cor1[1], cor1[2])
        #impressão do valor da cor em hex
        print("Hex = "+hexa)

        #impressão do valor da cor em rgb
        print("Quadrada2: "+str(cor2))
        hexa = hexadecimal(cor2[0], cor2[1], cor2[2])
        #impressão do valor da cor em hex
        print("Hex = "+hexa)

        #impressão do valor da cor em rgb
        print("Quadrada3: "+str(cor3))
        hexa = hexadecimal(cor3[0], cor3[1], cor3[2])
        #impressão do valor da cor em hex
        print("Hex = "+hexa)
        break

    #caso do usuário inserir um valor inválido
    else:
        print("Por favor selecione uma opção válida.")

#impressão da cor original
print("Original: "+str(r)+ " " +str(g)+ " " +str(b))
hexa = hexadecimal(r, g, b)
#impressão do hex da cor original
print("Hex = "+ hexa)