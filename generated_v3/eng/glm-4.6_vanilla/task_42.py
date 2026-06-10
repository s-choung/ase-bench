from ase import Atoms
from ase.calculators.emt import EMT
from ase.build import bulk
from ase.db import connect

db = connect('metals.db')

for symbol in ['Cu', 'Ag', 'Au']:
    atoms = bulk(symbol, 'fcc', a=4.0)
    atoms.calc = EMT()
    energy = atoms.get_potential_energy()
    db.write(atoms, energy=energy)

for row in db.select():
    print(f"{row.formula}: {row.energy:.3f} eV")
