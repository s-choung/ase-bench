from ase.build import bulk

atoms = bulk('Cu', 'fcc', a=3.61)
atoms *= (2, 2, 2)

print("Cell:")
print(atoms.cell)
print(f"Number of atoms: {len(atoms)}")
