from ase.build import bulk

atoms = bulk('Cu', 'fcc', a=3.615) * (2, 2, 2)
print("Cell info:", atoms.get_cell_lengths_and_angles())
print("Number of atoms:", len(atoms))
