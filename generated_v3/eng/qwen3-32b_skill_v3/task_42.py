from ase.build import bulk
from ase.calculators.emt import EMT
from ase.db import connect

metals = ['Cu', 'Ag', 'Au']
with connect('metals.db') as db:
    for symbol in metals:
        atoms = bulk(symbol, 'fcc')
        atoms.calc = EMT()
        energy = atoms.get_potential_energy()
        db.write(atoms, energy=energy, symbol=symbol)

with connect('metals.db') as db:
    for row in db.select():
        print(f"{row.symbol} {row.energy} eV")
