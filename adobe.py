import colorsys as cor

def hexadecimal(r, g, b):
    h = ""
    h1 = ""
    h2 = ""
    h3 = ""
    h += "#"

    if r==0:
        h1+="00"

    while r > 0:
        a = r%16
        r = r//16
        if a >= 10:
            h1 += chr((a-10)+ord("A"))
        else:
            h1 += str(a)

    if g==0:
        h2+="00"

    while g > 0:
            a = g%16
            g = g//16
            if a >= 10:
                h2 += chr((a-10)+ord("A"))
            else:
                h2 += str(a)

    if b==0:
        h3+="00"

    while b > 0:
            a = b%16
            b = b//16
            if a >= 10:
                h3 += chr((a-10)+ord("A"))
            else:
                h3 += str(a)

    h1 = h1[::-1]
    h2 = h2[::-1]
    h3 = h3[::-1]
    h += h1 + h2 + h3
    return h     

def hsv(r, g, b):
    r1 = r / 255.0 
    g1 = g / 255.0
    b1 = b / 255.0

    return cor.rgb_to_hsv(r1, g1, b1)

def volta(h, s, v):
    r, g, b = cor.hsv_to_rgb(h, s, v)
    return (round(r*255), round(g*255), round(b*255))

def soma(h, grau):
    return (h + (grau/360))%1.0

def cor_comp(r, g, b):
    h,s,v = hsv(r,g,b)

    h_comp = soma(h, 180)

    return volta(h_comp, s, v)

def cor_ana(r, g, b, offset):
    h,s,v = hsv(r,g,b)

    h_ana_menos = soma(h, -offset)
    h_ana_mais = soma(h, offset)

    return volta(h_ana_menos, s, v), volta(h_ana_mais, s, v) 

def cor_tri(r,g,b):
    h,s,v = hsv(r,g,b)

    h_tri1 = soma(h, 120)
    h_tri2 = soma(h, 240)

    return volta(h_tri1, s, v), volta(h_tri2, s, v)

def split_comp(r,g,b):
    h,s,v = hsv(r,g,b)

    h_comp1 = soma(h, 150)
    h_comp2 = soma(h, 210)

    return volta(h_comp1, s, v), volta(h_comp2, s, v)

def cor_tetra(r,g,b):
    h,s,v = hsv(r,g,b)

    h_t1 = soma(h, 60)
    h_t2 = soma(h, 180)
    h_t3 = soma(h, 240)

    return volta(h_t1,s,v), volta(h_t2,s,v), volta(h_t3,s,v)

def cor_quad(r,g,b):
    h,s,v = hsv(r,g,b)

    h_q1 = soma(h, 90)
    h_q2 = soma(h, 180)
    h_q3 = soma(h, 270)

    return volta(h_q1, s, v), volta(h_q2, s, v), volta(h_q3, s, v)


print("R: ")
r = int(input())
print("G: ")
g = int(input())
print("B: ")
b = int(input())

opt = 0
while True:
    print("Escolha o tipo de paleta de cores:")
    print("1-Complementares")
    print("2-Análogas")
    print("3-Triádicas")
    print("4-Split-complementares")
    print("5-Tetrádicas (retângulo)")
    print("6-Quadradas")

    opt = int(input())

    if opt == 1:
        cor1 = cor_comp(r, g, b)
        print("Complementar: "+str(cor1))
        hexa = hexadecimal(cor1[0], cor1[1], cor1[2])
        print("Hex = "+hexa)
        break

    elif opt == 2:
        print("Digite o valor do offset: ")
        offset = int(input())
        cor1, cor2 = cor_ana(r, g, b, offset)

        print("Análoga1: "+str(cor1))
        hexa = hexadecimal(cor1[0], cor1[1], cor1[2])
        print("Hex = "+hexa)

        print("Análoga2: "+str(cor2))
        hexa = hexadecimal(cor2[0], cor2[1], cor2[2])
        print("Hex = "+hexa)

        break

    elif opt == 3:
        cor1, cor2 = cor_tri(r, g, b)

        print("Triádica1: "+str(cor1))
        hexa = hexadecimal(cor1[0], cor1[1], cor1[2])
        print("Hex = "+hexa)
        
        print("Triádica2: "+str(cor2))
        hexa = hexadecimal(cor2[0], cor2[1], cor2[2])
        print("Hex = "+hexa)
        break

    elif opt == 4:
        cor1, cor2 = split_comp(r, g, b)

        print("Split-complementar1: "+str(cor1))
        hexa = hexadecimal(cor1[0], cor1[1], cor1[2])
        print("Hex = "+hexa)
        
        print("Split-complementar2: "+str(cor2))
        hexa = hexadecimal(cor2[0], cor2[1], cor2[2])
        print("Hex = "+hexa)
        break

    elif opt == 5:
        cor1, cor2, cor3 = cor_tetra(r, g, b)

        print("Tetrádica1: "+str(cor1))
        hexa = hexadecimal(cor1[0], cor1[1], cor1[2])
        print("Hex = "+hexa)
                
        print("Tetrádica2: "+str(cor2))
        hexa = hexadecimal(cor2[0], cor2[1], cor2[2])
        print("Hex = "+hexa)

        print("Tetrádica3: "+str(cor3))
        hexa = hexadecimal(cor3[0], cor3[1], cor3[2])
        print("Hex = "+hexa)
        break

    elif opt == 6:
        cor1, cor2, cor3 = cor_quad(r, g, b)

        print("Quadrada1: "+str(cor1))
        hexa = hexadecimal(cor1[0], cor1[1], cor1[2])
        print("Hex = "+hexa)
                
        print("Quadrada2: "+str(cor2))
        hexa = hexadecimal(cor2[0], cor2[1], cor2[2])
        print("Hex = "+hexa)

        print("Quadrada3: "+str(cor3))
        hexa = hexadecimal(cor3[0], cor3[1], cor3[2])
        print("Hex = "+hexa)
        break

    else:
        print("Por favor selecione uma opção válida.")

print("Original: "+str(r)+ " " +str(g)+ " " +str(b))
hexa = hexadecimal(r, g, b)
print("Hex = "+ hexa)