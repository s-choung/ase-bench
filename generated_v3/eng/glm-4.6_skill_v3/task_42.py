from ase.build import bulk
from ase.calculators.emt import EMT
from ase.db import connect

elements = ['Cu', 'Ag', 'Au']
db = connect('metals.db')

for elem in elements:
    atoms = bulk(elem, 'fcc', a=3.6 if elem == 'Cu' else 4.0 if elem == 'Ag' else 4.1)
    atoms.calc = EMT()
    energy = atoms.get_potential_energy()
    db.write(atoms, formula=elem, energy=energy)

for row in db.select():
    print(f"{row.formula}: {row.energy:.3f} eV")
