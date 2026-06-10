from ase import Atoms
from ase.calculators.emt import EMT
from ase.build import bulk
from ase.db import connect

# Create/connect to database
db = connect('bulk_metals.db')

# Store each bulk structure with EMT energy
for metal, lattice_constant in [('Cu', 3.615), ('Ag', 4.09), ('Au', 4.07)]:
    atoms = bulk(metal, 'fcc', a=lattice_constant)
    atoms.calc = EMT()
    energy = atoms.get_potential_energy()
    db.write(atoms, metal=metal, energy=energy)

# Query and print all entries
for row in db.select():
    print(f"{row.formula}: {row.energy:.3f} eV")
