from ase.build import bulk
from ase.calculators.emt import EMT
from ase.db import connect

db = connect('metals.db')

a_vals = {'Cu': 3.61, 'Ag': 4.09, 'Au': 4.08}   # approximate lattice constants (Å)

for sym in ['Cu', 'Ag', 'Au']:
    atoms = bulk(sym, 'fcc', a=a_vals[sym], cubic=True)
    atoms.calc = EMT()
    e = atoms.get_potential_energy()
    db.write(atoms, energy=e)

for row in db.select():
    atoms = row.toatoms()
    print(atoms.get_chemical_formula(), row.energy)
