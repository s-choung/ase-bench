from ase.db import connect
from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT

# Create a database
db_path = 'materials.db'
db = connect(db_path)

# List of materials to be stored
materials = ['Cu', 'Ag', 'Au']
structure_type = 'fcc'
lattice_constant = 3.6  # Approximate lattice constants for fcc

for material in materials:
    # Create the bulk structure
    atoms = bulk(material, structure_type, a=lattice_constant, cubic=True)
    # Set the EMT calculator
    atoms.set_calculator(EMT())
    # Calculate the energy
    energy = atoms.get_potential_energy()
    # Store in the database
    db.write(atoms, data={'energy': energy})

# Close the database connection
db.close()

# Query all entries
db = connect(db_path)
for row in db.select():
    formula = row.formula
    energy = row.data['energy']
    print(f'Formula: {formula}, Energy: {energy}')

# Close the database connection
db.close()
