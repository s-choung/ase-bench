from ase.db import connect
from ase import bulk

# Create database connection
db = connect('metals.db')

# Store Cu bulk
atoms = bulk('Cu', 'fcc', a=3.6, cubic=True)
energy = atoms.calc = EMT()
db.write(atoms, formula='Cu', energy=energy)

# Store Ag bulk
atoms = bulk('Ag', 'fcc', a=4.1, cubic=True)
energy = atoms.calc = EMT()
db.write(atoms, formula='Ag', energy=energy)

# Store Au bulk
atoms = bulk('Au', 'fcc', a=4.1, cubic=True)
energy = atoms.calc = EMT()
db.write(atoms, formula='Au', energy=energy)

# Query all entries
for row in db.select():
    print(f"Formula: {row.formula}, Energy: {row.energy} eV")

# Close the database
db.close()
