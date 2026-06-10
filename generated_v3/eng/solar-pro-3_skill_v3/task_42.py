from ase.db import connect
from ase.calculators.emt import EMT
from ase.build import bulk

# ----- create the database -----
db = connect('metals.db')

# ----- define structures -----
for el in ('Cu', 'Ag', 'Au'):
    atoms = bulk(el, 'fcc', a=4.0)          # arbitrary lattice constant
    atoms.calc = EMT()                     # compute EMT energy

    db.write(atoms, formula=el, energy=atoms.get_potential_energy())
    print(f'Inserted {el}: formula={atoms.get_formula()}, energy={atoms.get_potential_energy():.6f} eV')
