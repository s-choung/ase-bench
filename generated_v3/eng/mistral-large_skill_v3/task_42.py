from ase.build import bulk
from ase.calculators.emt import EMT
from ase.db import connect

db = connect('metals.db')

for metal in ['Cu', 'Ag', 'Au']:
    atoms = bulk(metal, 'fcc', a=3.6)
    atoms.calc = EMT()
    energy = atoms.get_potential_energy()
    db.write(atoms, metal=metal, energy=energy)

for row in db.select():
    print(f"{row.formula}: {row.energy:.3f} eV")
