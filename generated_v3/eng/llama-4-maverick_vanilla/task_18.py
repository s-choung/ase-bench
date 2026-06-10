from ase import Atoms
from ase.calculators.emt import EMT
from ase.db import connect

db = connect('ase.db')
molecule = db.get_atoms('CH4')
print(molecule.positions)
print(molecule.get_all_distances())
print(molecule.get_chemical_formula())
