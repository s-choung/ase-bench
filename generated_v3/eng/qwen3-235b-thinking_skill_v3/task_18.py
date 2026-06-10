from ase.build import molecule

ch4 = molecule('CH4')
print(ch4.symbols)
print(ch4.positions)
for i in range(1, 5):
    print(ch4.get_distance(0, i))
