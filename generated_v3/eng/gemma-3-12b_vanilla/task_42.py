from ase.build import fcc_hcp
from ase.calculators.emt import EMT
from ase.io import write, read
import os

dbfile = 'metals.db'

if os.path.exists(dbfile):
    os.remove(dbfile)

for metal in ['Cu', 'Ag', 'Au']:
    atoms = fcc_hcp(metal, size=3)
    calc = EMT()
    atoms.calc = calc
    atoms.get_potential_energy()
    write(dbfile, atoms)

db = read(dbfile)

for entry in db.select():
    print(f"Formula: {entry.formula}, Energy: {entry.energy}")
