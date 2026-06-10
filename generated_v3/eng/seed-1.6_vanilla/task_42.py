from ase.build import bulk
from ase.calculators.emt import EMT
from ase.db import connect

# Create database and store bulk metals with EMT energies
with connect('metal_bulks.db') as db:
    for metal in ('Cu', 'Ag', 'Au'):
        atoms = bulk(metal)
        atoms.calc = EMT()
        atoms.get_potential_energy()
        db.write(atoms)

# Query and print formula + energy
with connect('metal_bulks.db') as db:
    for entry in db.select():
        print(f'Formula: {entry.formula}, Energy: {entry.energy:.6f} eV')
