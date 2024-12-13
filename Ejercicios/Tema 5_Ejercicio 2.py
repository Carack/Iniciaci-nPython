str = 'código de práctica de prueba de geeks'

def invierte_palabras (frase):
    palabras = frase.split (' ')
    invertir = ' '.join(reversed(palabras))
    return invertir

print(invierte_palabras(str))

