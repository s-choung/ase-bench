from ase.build import fcc111, add_vacuum
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms

slab = fcc111('Cu', size=(3, 3, 3), layers=3)
add_vacuum(slab, height=12)

fix = FixAtoms(mask=[atom.tag > 0 for atom in slab])
slab.set_constraint(fix)

calc = EMT()
slab.calc = calc

print(f"Number of atoms: {len(slab)}")
print(slab.get_cell())
