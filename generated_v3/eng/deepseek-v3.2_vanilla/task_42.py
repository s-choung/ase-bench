from ase.db import connect
from ase.build import bulk
from ase.calculators.emt import EMT

db = connect('metals.db')

metals = ['Cu', 'Ag', 'Au']
for symbol in metals:
    atoms = bulk(symbol, 'fcc', a=3.6)
    atoms.calc = EMT()
    energy = atoms.get_potential_energy()
    db.write(atoms, energy=energy, formula=atoms.get_chemical_formula())

for row in db.select():
    print(f'{row.formula}: {row.energy:.3f} eV')
