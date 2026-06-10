from ase.build import molecule
from ase.geometry import get_distances

ch4 = molecule('CH4')
print("Coordinates (Å):\n", ch4.positions)
bonds = [get_distances(ch4.positions[0], pos, cell=ch4.cell, pbc=ch4.pbc)
         for pos in ch4.positions[1:]]
print(f"Bond lengths (Å): {bonds}")
print("Formula:", ch4.get_chemical_formula())
