from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.db import connect

# Create database and store structures
db = connect('metals.db')
metals = ['Cu', 'Ag', 'Au']
for metal in metals:
    atoms = bulk(metal, 'fcc')
    atoms.calc = EMT()
    energy = atoms.get_potential_energy()
    db.write(atoms, energy=energy)

# Query and print results
for row in db.select():
    print(f"{row.formula}: {row.energy:.6f} eV")
