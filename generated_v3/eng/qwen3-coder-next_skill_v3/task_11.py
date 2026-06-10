from ase import bulk

al = bulk('Al', 'bcc', a=3.3, cubic=True)
print("Cell:", al.get_cell())
print("Chemical formula:", al.get_chemical_formula())
