from ase import db
from ase.build import bulk
from ase.calculators.emt import EMT

db = db.connect('metals.db')
elements = ['Cu', 'Ag', 'Au']

for symbol in elements:
    atoms = bulk(symbol, 'fcc')
    atoms.calc = EMT()
    energy = atoms.get_potential_energy()
    db.write(atoms, symbol=symbol, energy=energy)

for entry in db.select():
    print(f"{entry.formula}: {entry.energy:.3f} eV")
