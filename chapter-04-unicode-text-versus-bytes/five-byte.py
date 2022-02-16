cafe = bytes('café', encoding='utf_8')
print(cafe)
print(cafe[0])
print(cafe[:1])

cafe_arr = bytearray(cafe)
print(cafe_arr)
print(cafe_arr[-1:])

# fromhex constrói uma sequência binária analisando pares de dígitos hexadecimais opcionalmente separados por espaços:
print(bytes.fromhex('31 4b CE A9'))
