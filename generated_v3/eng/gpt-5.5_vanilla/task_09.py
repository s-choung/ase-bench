from ase.build import bulk
from ase.io import write, read

atoms = bulk("Cu", "fcc", a=3.6)

write("POSCAR", atoms, format="vasp")
atoms2 = read("POSCAR", format="vasp")

print("Number of atoms:", len(atoms2))
print("Cell parameters:", atoms2.cell.cellpar())
