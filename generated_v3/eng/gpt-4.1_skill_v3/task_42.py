from ase.build import bulk
from ase.calculators.emt import EMT
from ase.db import connect

db = connect('cu_ag_au_bulk.db')

for sym in ['Cu', 'Ag', 'Au']:
    atoms = bulk(sym, 'fcc', a=None, cubic=True)
    atoms.calc = EMT()
    e = atoms.get_potential_energy()
    db.write(atoms, energy=e)

for row in db.select():
    print(f'{row.formula}: {row.energy:.6f} eV')
