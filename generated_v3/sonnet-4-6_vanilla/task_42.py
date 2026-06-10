from ase.build import bulk
from ase.calculators.emt import EMT
from ase.db import connect

db = connect('metals.db')

metals = ['Cu', 'Ag', 'Au']
for symbol in metals:
    atoms = bulk(symbol, 'fcc', a={'Cu': 3.6, 'Ag': 4.09, 'Au': 4.08}[symbol])
    atoms.calc = EMT()
    energy = atoms.get_potential_energy()
    db.write(atoms, energy=energy)

for row in db.select():
    print(f"Formula: {row.formula}, Energy: {row.energy:.4f} eV")
