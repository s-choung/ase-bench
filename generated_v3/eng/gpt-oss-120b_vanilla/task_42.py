from ase.build import bulk
from ase.calculators.emt import EMT
from ase.db import connect

# --- create database -------------------------------------------------
db = connect('metals.db')

# --- list of elements ------------------------------------------------
for element in ('Cu', 'Ag', 'Au'):
    atoms = bulk(element, 'fcc', a=3.6)      # lattice constant approx.; EMT will correct it
    atoms.calc = EMT()
    energy = atoms.get_potential_energy()
    db.write(atoms, name=element, energy=energy)

# --- query and print -------------------------------------------------
for row in db.select():
    print(f"{row.formula}: {row.energy:.3f} eV")
