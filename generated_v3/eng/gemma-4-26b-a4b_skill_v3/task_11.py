from ase.build import bulk

atoms = bulk('Al', 'bcc', a=3.3, cubic=True)

print(f"Cell:\n{atoms.get_cell()}")
print(f"Formula: {atoms.get_chemical_formula()}")
