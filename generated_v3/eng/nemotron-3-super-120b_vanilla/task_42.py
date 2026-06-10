from ase.build import bulk
from ase.calculators.emt import EMT
from ase.db import connect

# Create (or overwrite) the ASE database
db = connect('metals.db')

# Define metals and their bulk structures
for symbol in ['Cu', 'Ag', 'Au']:
    atoms = bulk(symbol, cubic=True)          # fcc bulk
    atoms.calc = EMT()
    energy = atoms.get_potential_energy()
    # Store atoms with formula and energy as key-value pairs
    db.write(atoms, data={'formula': atoms.get_chemical_formula(), 'energy': energy})

# Query all entries and print formula and energy
for row in db.select():
    print(f"Formula: {row.formula}, Energy: {row.energy:.3f} eV")
