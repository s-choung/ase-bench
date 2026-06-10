from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.filters import FrechetCellFilter
from ase.db import connect

db = connect('metals.db', create=True)

for metal in ['Cu', 'Ag', 'Au']:
    atoms = bulk(metal, 'fcc', a=3.6)
    atoms.calc = EMT()
    BFGS(FrechetCellFilter(atoms)).run(fmax=0.01)
    db.write(atoms, formula=atoms.get_chemical_formula(), energy=atoms.get_potential_energy())

print(f"{'Formula':<10} {'Energy (eV)':<15}")
print("-" * 25)
for row in db.select():
    print(f"{row.formula:<10} {row.energy:<15.6f}")
