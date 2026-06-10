from ase.build import bulk
from ase.calculators.emt import EMT
from ase.db import connect

with connect('bulk_metals.db', overwrite=True) as db:
    for sym in ['Cu', 'Ag', 'Au']:
        atoms = bulk(sym, 'fcc')
        atoms.calc = EMT()
        db.write(atoms, energy=atoms.get_potential_energy())
    for row in db.select():
        print(f"Formula: {row.atoms.get_chemical_formula(reduce=True)}, Energy: {row.energy:.2f} eV")
