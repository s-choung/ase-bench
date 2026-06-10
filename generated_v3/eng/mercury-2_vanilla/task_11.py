from ase.build import bulk

# Create BCC Al with lattice constant 3.3 Å, cubic cell
al = bulk('Al', 'bcc', a=3.3, cubic=True)

# Output cell parameters and chemical formula
print('Cell:', al.get_cell())
print('Formula:', al.get_chemical_formula())
