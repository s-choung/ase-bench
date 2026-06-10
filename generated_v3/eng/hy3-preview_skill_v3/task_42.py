from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.db import connect

# Create database
db = connect('metals.db', create=True)

# Store Cu bulk
cu = bulk('Cu', 'fcc', a=3.6)
cu.calc = EMT()
cu_energy = cu.get_potential_energy()
db.write(cu, energy=cu_energy, formula='Cu')

# Store Ag bulk
ag = bulk('Ag', 'fcc', a=4.09)
ag.calc = EMT()
ag_energy = ag.get_potential_energy()
db.write(ag, energy=ag_energy, formula='Ag')

# Store Au bulk
au = bulk('Au', 'fcc', a=4.08)
au.calc = EMT()
au_energy = au.get_potential_energy()
db.write(au, energy=au_energy, formula='Au')

# Query and print all entries
for row in db.select():
    print(f"Formula: {row.formula}, Energy: {row.energy:.3f} eV")
