from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.db import connect

# Create database and store structures
db = connect('bulk_energies.db')
for symbol in ['Cu', 'Ag', 'Au']:
    atoms = bulk(symbol, 'fcc', a=3.6)
    atoms.calc = EMT()
    energy = atoms.get_potential_energy()
    db.write(atoms, key=symbol, energy=energy)

# Query and print results
for row in db.select():
    print(f"{row.formula} {row.energy:.6f} eV")
