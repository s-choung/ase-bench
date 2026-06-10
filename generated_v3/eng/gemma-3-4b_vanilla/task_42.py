from ase.build import fcc111, tetrahedron
from ase.calculators import EMT, LJ
from ase.database import PocoDatabase

db = PocoDatabase('bulk_metals.pov')

# Cu bulk
cubo = fcc111('Cu', size=(4, 4, 4), a=3.61)
cubo.calc = EMT()
db.append('Cu bulk', cubo, tag='Cu')

# Ag bulk
ago = fcc111('Ag', size=(4, 4, 4), a=4.09)
ago.calc = EMT()
db.append('Ag bulk', ago, tag='Ag')

# Au bulk
auo = fcc111('Au', size=(4, 4, 4), a=4.07)
auo.calc = EMT()
db.append('Au bulk', auo, tag='Au')

# LJ calculator
lj = LJ(r_c=3.5)
db.append('LJ calculator', None, tag='LJ')

# Select all entries
entries = db.select()

for entry in entries:
    print(f"Formula: {entry.formula}, Energy: {entry.calc.emt.energy}")
