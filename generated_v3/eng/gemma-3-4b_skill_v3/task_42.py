import numpy as np
from ase import Atoms
from ase.calculators.emt import EMT
from ase.io import write
from ase.db import connect

# Create Cu bulk structure
cu = bulk('Cu', 'fcc', a=3.6)
cu.calc = EMT()
cu.get_potential_energy()
write('cu_bulk.xyz', cu)

# Create Ag bulk structure
ag = bulk('Ag', 'fcc', a=4.0)
ag.calc = EMT()
ag.get_potential_energy()
write('ag_bulk.xyz', ag)

# Create Au bulk structure
au = bulk('Au', 'fcc', a=4.109)
au.calc = EMT()
au.get_potential_energy()
write('au_bulk.xyz', au)

# Create ASE database
db = connect('bulk_elements.db')

# Store the structures and energies in the database
db.write(cu, key='Cu')
db.write(ag, key='Ag')
db.write(au, key='Au')

# Query the database
results = db.select('*')

# Print each entry's formula and energy
for entry in results:
    formula = entry.formula
    energy = entry.get_potential_energy()
    print(f"Formula: {formula}, Energy: {energy:.6f}")

db.close()
