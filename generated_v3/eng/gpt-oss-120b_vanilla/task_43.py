from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.db import connect

db = connect('cu_slabs.db')

# create and store Cu (111) slabs with 2, 3, and 4 layers
for n in (2, 3, 4):
    atoms = fcc111('Cu', size=(2, 2, n), vacuum=10.0)
    atoms.calc = EMT()            # optional, ensures energies are available
    db.write(atoms, layers=n)

# retrieve slab with exactly 3 layers and print its atom count
row = db.select(layers=3).first()
print(row.toatoms().get_number_of_atoms())
