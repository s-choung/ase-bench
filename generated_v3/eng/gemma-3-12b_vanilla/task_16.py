from ase.build import fcc111, make_cut
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.units import Angstrom

slab = make_cut(fcc111('Fe', size=(2, 2, 4)), '110', 75)
slab.set_cell([2.87, 2.87, 4.0], 'abc')
slab.wrap()
vacuum = 10 * Angstrom
slab.cell[2] += vacuum
slab.center(vacuum=vacuum)

fix = FixAtoms(mask=[atom.tag == 1 for atom in slab])
slab.set_constraint(fix)

calc = EMT()
slab.calc = calc

print(f"Number of atoms: {len(slab)}")
print(f"Cell size: {slab.cell}")
