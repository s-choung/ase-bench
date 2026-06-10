from ase.build import bulk
from ase.calculators.emt import EMT
from ase.db import connect

# Connect to a new database file
db = connect('metals.db')

# Define metals to process
metals = ['Cu', 'Ag', 'Au']

# Create and store structures
for symbol in metals:
    atoms = bulk(symbol, 'fcc', a=3.6)
    atoms.calc = EMT()
    energy = atoms.get_potential_energy()
    # Store atoms and energy in the database
    db.write(atoms, formula=symbol, energy=energy)

# Query all entries and print results
print(f"{'Formula':<10} | {'Energy (eV)':<12}")
print("-" * 25)

for row in db.select():
    # Access data via the row object
    print(f"{row.formula:<10} | {row.energy:<12.4f}")

# Close database connection
db.close()
