from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.db import connect

db = connect('metals.db')

metals = ['Cu', 'Ag', 'Au']
for metal in metals:
    atoms = bulk(metal, 'fcc', a=4.0)
    atoms.calc = EMT()
    energy = atoms.get_potential_energy()
    db.write(atoms, energy=energy)

for row in db.select():
    print(f"Formula: {row.formula}, Energy: {row.energy} eV")
