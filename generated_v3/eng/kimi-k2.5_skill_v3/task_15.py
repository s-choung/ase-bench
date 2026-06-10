from ase.build import fcc100

atoms = fcc100('Cu', size=(3, 3, 3), vacuum=12.0)
print(f"Number of atoms: {len(atoms)}")
print(f"Cell:\n{atoms.cell}")
print(f"Cell lengths: {atoms.cell.lengths()}")
