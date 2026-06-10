from ase.db import connect
from ase.build import bulk
from ase.calculators.emt import EMT

# Connect to a new database or overwrite an existing one
db = connect('my_db.db', append=False)

# List of elements and their bulk structures
elements = [('Cu', bulk('Cu', cubic=True)),
            ('Ag', bulk('Ag', cubic=True)),
            ('Au', bulk('Au', cubic=True))]

# Calculate and store EMT energies for each bulk structure
for elem, atoms in elements:
    atoms.set_calculator(EMT())
    energy = atoms.get_potential_energy()
    db.write(atoms, formula=elem, energy=energy)

# Query all entries and print formula and energy
for row in db.select():
    print(f"{row.formula}: {row.energy} eV")
