def infijo_a_postfijo(expresion):
    precedencia = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    pila = Pila()
    postfijo = []
    tokens = expresion.split()

    for token in tokens:
        if token.isnumeric():
            postfijo.append(token)
        elif token in precedencia:
            while (not pila.is_empty() and
                   precedencia.get(pila.peek(), 0) >= precedencia[token]):
                postfijo.append(pila.pop())
            pila.push(token)
        elif token == '(':
            pila.push(token)
        elif token == ')':
            while not pila.is_empty() and pila.peek() != '(':
                postfijo.append(pila.pop())
            pila.pop()  # Eliminar '('
    
    while not pila.is_empty():
        postfijo.append(pila.pop())

    return ' '.join(postfijo)

def evaluar_postfijo(expresion):
    pila = Pila()
    tokens = expresion.split()

    for token in tokens:
        if token.isnumeric():
            pila.push(int(token))
        else:
            b = pila.pop()
            a = pila.pop()
            if token == '+':
                pila.push(a + b)
            elif token == '-':
                pila.push(a - b)
            elif token == '*':
                pila.push(a * b)
            elif token == '/':
                pila.push(a / b)

    return pila.pop()

if __name__ == "__main__":
    expresion = input("Introduce una expresión en notación infija: ")
    postfijo = infijo_a_postfijo(expresion)
    print(f"Notación postfija: {postfijo}")
    resultado = evaluar_postfijo(postfijo)
    print(f"Resultado: {resultado}")
