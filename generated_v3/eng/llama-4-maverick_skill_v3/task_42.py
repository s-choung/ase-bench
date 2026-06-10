from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.db import connect

# Create a database
db = connect('metals.db')

# Define metals and their lattice constants
metals = {
    'Cu': 3.6,
    'Ag': 4.09,
    'Au': 4.08,
}

# Create bulk structures, calculate EMT energies, and store in database
for symbol, a in metals.items():
    atoms = bulk(symbol, 'fcc', a=a, cubic=True)
    atoms.calc = EMT()
    energy = atoms.get_potential_energy()
    db.write(atoms, metal=symbol, energy=energy)

# Query and print database entries
for row in db.select():
    print(f"Formula: {row.formula}, Energy: {row.energy} eV")
