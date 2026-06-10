from ase.db import Database
from ase import bulk
from ase.calculators.emt import EMT

db = Database('metals.db')
lattice = {'Cu': 3.61, 'Ag': 4.09, 'Au': 4.08}

for symbol in ['Cu', 'Ag', 'Au']:
    a = lattice[symbol]
    atoms = bulk(symbol, 'fcc', a=a)
    atoms.calc = EMT()
    energy = atoms.get_potential_energy()
    formula = atoms.get_chemical_formula()
    db.write(atoms, formula=formula, energy=energy)

for row in db.select():
    print(f"{row.formula}: {row.energy}")
