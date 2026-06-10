from ase.build import bulk
from ase.calculators.emt import EMT
from ase.db import connect

db = connect("metals.db")

for el in ("Cu", "Ag", "Au"):
    atoms = bulk(el, crystalstructure="fcc")      # experimental lattice constants are used
    atoms.calc = EMT()
    energy = atoms.get_potential_energy()
    db.write(atoms, energy=energy)

for row in db.select():
    print(row.formula, row.energy)
