from ase.build import fcc100

atoms = fcc100('Cu', layers=3, size=(3,3,3), vacuum=12)
print(f"Number of atoms: {len(atoms)}")
print(f"Cell:\n{atoms.get_cell()}")
