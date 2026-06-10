from ase import Atoms
from ase.lattice import MonkhorstSchultz
from ase.build import supercell
from ase.calculators import EMT, LJ
from ase.io import database

slab_width = 4
slab_height = 4
vacuum = 10.0

# Create Cu slab structures
database.load('cu_slabs.rst')
db = database.load('cu_slabs.rst')
for i in range(2, 5):
    cell = (slab_width, slab_height, slab_height)
    a = Atoms(scaled_lengths=cell)
    a.center()
    s = supercell(a, cell, vacuum)
    s.setcell(s.getcell())
    s.calc = EMT(xc='PAW', pseudopotentials='PAW')
    s.get_atomic_numbers()
    s.add_atoms(Atoms([31],positions=[(0.0,0.0,0.0)]))
    db.append(str(i) + '_layers', s)

# Create and load Cu slab with 3 layers
db.load('cu_slabs.rst')
structure = select(db, '3_layers')
print(len(structure))

def select(db, key):
  return db.select_by_key(key)
