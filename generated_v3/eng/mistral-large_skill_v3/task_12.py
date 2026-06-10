from ase.build import bulk
from ase import Atoms

atoms = bulk('Ti', 'hcp', a=2.95, c=2.95 * 1.59)
print("Cell vectors (Å):")
print(atoms.get_cell())
print("\nAtomic positions (Å):")
for atom in atoms:
    print(f"{atom.symbol} {atom.position}")
