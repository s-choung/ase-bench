from ase.build import bulk

atoms = bulk('Al', 'bcc', a=3.3, cubic=True)
print("Chemical formula:", atoms.get_chemical_formula())
print("Cell:\n", atoms.get_cell())
