from ase.build import bulk
from ase.calculators.emt import EMT
from ase.db import connect

db = connect('metals.db', append=False)

for metal in ['Cu', 'Ag', 'Au']:
    atoms = bulk(metal, 'fcc')
    atoms.calc = EMT()
    energy = atoms.get_potential_energy()
    db.write(atoms, metal=metal, energy=energy)

print(f"{'Formula':<10} {'Energy (eV)':>15}")
print("-" * 26)
for row in db.select():
    print(f"{row.formula:<10} {row.energy:>15.6f}")
