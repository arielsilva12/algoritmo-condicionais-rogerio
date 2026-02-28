def verificar_triangulo_lado(a, b, c):
    if a < (b + c) and b < (a + c) and c < (a + b):
        return True
    else:
        return False
    
def classificar_triangulo_lado(a: int, b: int, c: int) -> str:
    if a == b == c:
        return 'Equilátero'
    elif a != b and a != c and b != c:
        return 'Escaleno'
    else:
        return 'Isósceles'
    
def verificar_triangulo_angulo(angulo1, angulo2, angulo3):
    if angulo1 + angulo2 + angulo3 == 180:
        return 'Sim, é triângulo!'
    else:
        return 'Não é um triângulo!'
    
def classificar_triangulo_angulo(angulo1: int, angulo2:int, angulo3:int) -> str:
    if angulo1 == 90 or angulo2 == 90 or angulo3 == 90:
        return 'Retângulo'
    elif angulo1 < 90 and angulo2 < 90 and angulo3 < 90:
        return 'Acutângulo'
    else:
        return 'Obtusângulo'