from ase import Atoms
from ase.calculators.emt import EMT
from ase.build import bulk
from ase.db import connect

db_file = 'metals.db'
# Remove existing database if it exists to ensure a clean run
import os
if os.path.exists(db_file):
    os.remove(db_file)

db = connect(db_file)

metals = ['Cu', 'Ag', 'Au']

for metal in metals:
    atoms = bulk(metal, 'fcc', a=3.6)  # Approximate lattice constant for demonstration
    atoms.calc = EMT()
    energy = atoms.get_potential_energy()
    db.write(atoms, formula=metal, energy=energy)

print(f"{'Formula':<10} | {'Energy (eV)':<15}")
print("-" * 28)

for row in db.select():
    print(f"{row.formula:<10} | {row.energy:<15.4f}")
