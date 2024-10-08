
def sum(a, b):
    """Función que suma"""
    resultado = a + b
    return (resultado)
    
def mul(a, b):
    """Función que multiplica"""
    resultado = a * b
    return (resultado)
    
    # programa principal -main-
  
a = int(input('a?: '))
b = int(input('b?: '))

print(f'Sum of {a} and {b} is {sum(a, b)}')
print(f'mul of {a} and {b} is {mul(a, b)}')
