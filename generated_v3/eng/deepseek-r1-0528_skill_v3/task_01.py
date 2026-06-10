from ase.build import bulk
atoms = bulk('Cu', 'fcc', a=3.615)
supercell = atoms * (2, 2, 2)
print(f"Cell vectors:\n{supercell.cell}\n")
print(f"Number of atoms: {len(supercell)}")
