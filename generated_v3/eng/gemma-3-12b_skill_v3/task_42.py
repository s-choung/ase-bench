from ase.build import bulk
from ase.calculators.emt import EMT
from ase.io import write
from ase.db import connect

# Create the database
db = connect('ase_database.db')

# Define the structures and calculators
cu = bulk('Cu', 'fcc', a=3.6)
ag = bulk('Ag', 'fcc', a=3.6)
au = bulk('Au', 'fcc', a=3.6)

cu.calc = EMT()
ag.calc = EMT()
au.calc = EMT()

# Calculate energies and write to the database
cu.get_potential_energy()
ag.get_potential_energy()
au.get_potential_energy()

write(db, cu)
write(db, ag)
write(db, au)

# Query the database
entries = db.select()

# Print the formula and energy for each entry
for entry in entries:
    formula = entry.get('formula')
    energy = entry.get('energy')
    print(f"Formula: {formula}, Energy: {energy}")

# Clean up the database connection
db.close()
