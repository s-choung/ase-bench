from ase.build import bulk

atoms = bulk('Al', 'bcc', a=3.3, cubic=True)
print("Cell matrix:\n", atoms.cell)
print("Chemical formula:", atoms.get_chemical_formula())
