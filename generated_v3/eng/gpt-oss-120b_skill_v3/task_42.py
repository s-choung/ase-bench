from ase.build import bulk
from ase.calculators.emt import EMT
from ase.db import connect

db = connect('metals.db')
for elem in ('Cu', 'Ag', 'Au'):
    atoms = bulk(elem, 'fcc', a=3.6)   # EMT will use its own lattice constant
    atoms.calc = EMT()
    energy = atoms.get_potential_energy()
    db.write(atoms, formula=atoms.get_chemical_formula(), energy=energy)

for row in db.select():
    print(row.formula, row.energy)
