from ase.build import bulk
from ase.io import write, read

atoms = bulk("Cu", "fcc", a=3.6, cubic=True)

write("POSCAR", atoms, format="vasp")

atoms_read = read("POSCAR", format="vasp")

print("Number of atoms:", len(atoms_read))
print("Cell parameters:", atoms_read.cell.cellpar())
