from ase import Atoms
from ase.calculators.emt import EMT
from ase.db import connect

db = connect('metals.db')

for symbol in ['Cu', 'Ag', 'Au']:
    atoms = Atoms(symbol, cell=[(3.6, 0, 0), (0, 3.6, 0), (0, 0, 3.6)], pbc=True)
    atoms.calc = EMT()
    energy = atoms.get_potential_energy()
    db.write(atoms, metal=symbol, energy=energy)

for row in db.select():
    print(f"Formula: {row.formula}, Energy: {row.energy}")
