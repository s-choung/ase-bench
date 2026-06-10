from ase.build import bulk
from ase.calculators.emt import EMT
from ase.db import connect

db = connect(':memory:')

for element, latconst in [('Cu', 3.615), ('Ag', 4.085), ('Au', 4.078)]:
    atoms = bulk(element, 'fcc', a=latconst)
    atoms.calc = EMT()
    energy = atoms.get_potential_energy()
    db.write(atoms, energy=energy)

for row in db.select():
    print(f'{row.formula}: {row.energy:.6f} eV')
