from ase.build import bulk
from ase.io import write, read

atoms = bulk("Cu", "fcc", a=3.615, cubic=True)

write("POSCAR", atoms, format="vasp")

atoms_read = read("POSCAR", format="vasp")
cell_params = atoms_read.get_cell_lengths_and_angles()

print("Number of atoms:", len(atoms_read))
print("Cell parameters [a, b, c, alpha, beta, gamma]:", cell_params)
