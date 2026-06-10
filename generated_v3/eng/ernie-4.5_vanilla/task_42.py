from ase.build import bulk
from ase.calculators.emt import EMT
from ase.db import connect

# Create or connect to a database
db = connect('metals.db')

# Define metals and their lattice types
metals = {
    'Cu': 'fcc',
    'Ag': 'fcc',
    'Au': 'fcc'
}

# Insert Cu, Ag, and Au bulk structures with EMT energies into the database
for symbol, lattice in metals.items():
    atoms = bulk(symbol, lattice, cubic=True)
    atoms.set_calculator(EMT())
    energy = atoms.get_potential_energy()
    
    db.write(atoms, name=symbol, energy=energy)

# Query all entries in the database and print formula and energy
for row in db.select():
    print(f"Formula: {row.formula}, Energy: {row.energy:.5f} eV")
