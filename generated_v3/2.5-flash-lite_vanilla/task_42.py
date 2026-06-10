from ase.db import connect
from ase.calculators.emt import EMT
from ase.build import bulk

# Create a new database
db = connect('metals.db')

# Define elements and their bulk structures
elements = ['Cu', 'Ag', 'Au']

for element in elements:
    # Create bulk structure
    atoms = bulk(element, 'fcc', a=4.0)

    # Attach EMT calculator and calculate energy
    atoms.calc = EMT()
    energy = atoms.get_potential_energy()

    # Store in database
    db.write(atoms, energy=energy, formula=element)

# Select all entries from the database
for row in db.select():
    print(f"Formula: {row.formula}, Energy: {row.energy}")
