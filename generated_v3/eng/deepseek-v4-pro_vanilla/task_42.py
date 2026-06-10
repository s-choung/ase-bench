from ase.build import bulk
from ase.calculators.emt import EMT
from ase.db import connect

# Create an ASE database
db = connect('bulk_metals.db')

# Metals to process
metals = ['Cu', 'Ag', 'Au']

for metal in metals:
    atoms = bulk(metal, 'fcc')          # default lattice constant
    atoms.calc = EMT()                  # attach EMT calculator
    energy = atoms.get_potential_energy()
    db.write(atoms, energy=energy)      # store structure and energy

# Query and print all entries
for row in db.select():
    print(f"Formula: {row.formula}, Energy: {row.energy:.3f} eV")
