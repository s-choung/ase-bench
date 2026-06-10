from ase import Atoms

al_structure = bulk('Al', 'bcc', a=3.3, cubic=True)
print(al_structure.get_cell())
print(al_structure.get_chemical_formula())
