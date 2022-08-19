peso_ale = int(input())

ale = peso_ale
gi = int((ale * 2)+4)
nico = int((gi + ale)/5)
print(f'{ale} {gi} {nico}')

if nico >= 0 and nico < 20:
    print("uno")
if nico >= 21 and nico < 40:
    print("dos")
if nico >= 41 and nico < 80:
    print("tres")
else:
    print("cuatro")

