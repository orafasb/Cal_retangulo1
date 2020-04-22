import math
base: float
altura: float
area: float
perimetro: float
diagona: float
hipotenusa:float

base = float(input("Digite o valor da base: "))
altura = float(input("Digite o valor da altura: "))

area = base*altura
perimetro = 2*(base + altura)
diagonal = math.sqrt(base ** 2 + altura ** 2)



print(f"Area é {area:.4f}")
print(f"O Perimetro é {perimetro:.4f}")
print(f"A diagonal é {diagonal:.4f}")
