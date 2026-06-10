from ase.db import connect
from ase.build import bulk
from ase.calculators.emt import EMT

# Create and connect to a new database
db = connect('metals.db')

# Store Cu, Ag, and Au bulk structures with EMT energies
for symbol in ['Cu', 'Ag', 'Au']:
    atoms = bulk(symbol, 'fcc', a=4.0)  # Initial guess for lattice constant
    atoms.calc = EMT()
    energy = atoms.get_potential_energy()
    
    db.write(atoms, symbol=symbol, energy=energy)

# Query and print all entries
for entry in db.select():
    formula = entry.symbols  # Alternatively: entry.toatoms().get_chemical_formula()
    # Some database backends might require converting entry to atoms to get formula reliably
    # Using toatoms() method:
    atoms = entry.toatoms()
    formula = atoms.get_chemical_formula()
    print(f"Formula: {formula}, Energy: {entry.energy:.3f} eV")
