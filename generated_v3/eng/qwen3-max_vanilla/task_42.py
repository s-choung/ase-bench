from ase import Atoms
from ase.calculators.emt import EMT
from ase.db import connect

# Create bulk structures
cu = Atoms('Cu', cubic=True, pbc=True)
cu.set_cell([3.6]*3, scale_atoms=True)

ag = Atoms('Ag', cubic=True, pbc=True)
ag.set_cell([4.1]*3, scale_atoms=True)

au = Atoms('Au', cubic=True, pbc=True)
au.set_cell([4.1]*3, scale_atoms=True)

# Set EMT calculator and compute energies
for atoms in [cu, ag, au]:
    atoms.calc = EMT()
    atoms.get_potential_energy()

# Store in database
with connect('metals.db') as db:
    db.write(cu)
    db.write(ag)
    db.write(au)

# Query and print
with connect('metals.db') as db:
    for row in db.select():
        print(f"{row.formula}: {row.energy:.6f} eV")
