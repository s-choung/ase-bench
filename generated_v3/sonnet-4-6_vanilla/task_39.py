from ase.build import bulk
from ase.io import write, read

au = bulk('Au', 'fcc', a=4.08)
write('au_bulk.xyz', au)

atoms = read('au_bulk.xyz')
print("원자 종류와 위치:")
for atom in atoms:
    print(f"{atom.symbol}: {atom.position}")
