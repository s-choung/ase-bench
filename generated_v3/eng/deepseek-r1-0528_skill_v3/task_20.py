from ase.build import nanotube

atoms = nanotube(6, 6, length=4) 
print("Number of atoms:", len(atoms))
print("Cell lengths and angles (Å, degrees):", atoms.get_cell_lengths_and_angles())
print("Periodic boundary conditions:", atoms.pbc)
