from ase import Atoms
from ase.calculators.emt import EMT
from ase.db import connect

atoms_Cu = bulk('Cu', 'fcc', a=3.6)
atoms_Ag = bulk('Ag', 'fcc', a=4.09)
atoms_Au = bulk('Au', 'fcc', a=4.08)

for atoms in [atoms_Cu, atoms_Ag, atoms_Au]:
    atoms.calc = EMT()

with connect('bulk.db') as db:
    db.write(atoms_Cu, tag='Cu', energy=atoms_Cu.get_potential_energy())
    db.write(atoms_Ag, tag='Ag', energy=atoms_Ag.get_potential_energy())
    db.write(atoms_Au, tag='Au', energy=atoms_Au.get_potential_energy())

    for row in db.select():
        print(row.formula, row.energy)
