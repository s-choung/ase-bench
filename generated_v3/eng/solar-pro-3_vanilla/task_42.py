from ase import Atoms
from ase.db import connect
from ase.calculators.emt import EMT

# Create the database
db = connect('metals.db')

# Bulk copper (fcc)
cu = Atoms('Cu', cell=(4.0, 4.0, 4.0, 90, 90, 90))
cu.set_cell(cu.get_cell(), scale_atoms=True)
EMT().calculate(cu)
db.write(cu, name='Cu_bulk', formula='Cu', energy=cu.get_potential_energy())

# Bulk silver (fcc)
ag = Atoms('Ag', cell=(4.5, 4.5, 4.5, 90, 90, 90))
ag.set_cell(ag.get_cell(), scale_atoms=True)
EMT().calculate(ag)
db.write(ag, name='Ag_bulk', formula='Ag', energy=ag.get_potential_energy())

# Bulk gold (fcc)
au = Atoms('Au', cell=(4.0, 4.0, 4.0, 90, 90, 90))
au.set_cell(au.get_cell(), scale_atoms=True)
EMT().calculate(au)
db.write(au, name='Au_bulk', formula='Au', energy=au.get_potential_energy())

# Query and print
for row in db.select():
    print(f"Formula: {row.formula}, Energy: {row.energy}")
