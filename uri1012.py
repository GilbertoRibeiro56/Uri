lista = input() .split()
A = float(lista[0])
B = float(lista[1])
C = float(lista[2])

a_tri = (A*C)/2
a_cir = (3.14159 * C * C)
a_tra = ((A + B)*C)/2
a_qua = B**2
a_ret = A * B

print(f'TRIANGULO: {a_tri:.3f}')
print(f'CIRCULO: {a_cir:.3f}')
print(f'TRAPEZIO: {a_tra:.3f}')
print(f'QUADRADO: {a_qua:.3f}')
print(f'RETANGULO: {a_ret:.3f}')
