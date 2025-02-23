def es_primo(n):
    """Determina si un número es primo."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def encontrar_primos(hasta):
    """Encuentra todos los números primos hasta un número dado."""
    primos = []
    for num in range(2, hasta + 1):
        if es_primo(num):
            primos.append(num)
    return primos
def descomposicion_en_factores(x):
    """Descomposición en factores de un número."""
    factores = []
    for primo in encontrar_primos(x):
        while x % primo == 0:
            factores.append(primo)
            x = x // primo
    return factores
# Pedir al usuario que introduzca el número a descomponer
numero = int(input("Introduce el número a descomponer en factores primos: "))
print(f"Los factores primos de {numero} son: {descomposicion_en_factores(numero)}")