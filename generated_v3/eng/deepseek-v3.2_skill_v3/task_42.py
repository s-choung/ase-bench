from ase.build import bulk
from ase.calculators.emt import EMT
from ase.db import connect
from ase import units

metals = ['Cu', 'Ag', 'Au']
structures = []

for symbol in metals:
    atoms = bulk(symbol, 'fcc', a=3.6, cubic=True)
    atoms.calc = EMT()
    energy = atoms.get_potential_energy()
    structures.append((atoms, energy))

db = connect('metals.db')
for atoms, energy in structures:
    db.write(atoms, energy=energy, formula=atoms.get_chemical_formula())

for row in db.select():
    print(f"{row.formula}: {row.energy:.6f} eV")
