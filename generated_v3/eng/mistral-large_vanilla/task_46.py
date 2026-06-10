from ase.build import fcc111, molecule
from ase.constraints import FixAtoms, FixBondLength
from ase.calculators.emt import EMT
from ase.optimize import BFGS

slab = fcc111('Pt', size=(2, 2, 3), vacuum=10.0)
co = molecule('CO')
co.translate([2.5, 2.5, 12.0])
slab += co

mask = [atom.tag == 1 for atom in slab]
slab.set_constraint([FixAtoms(mask=mask), FixBondLength(48, 49)])

slab.calc = EMT()
opt = BFGS(slab)
opt.run(fmax=0.05)

print(f"Final energy: {slab.get_potential_energy():.3f} eV")
print(f"C-O distance: {slab.get_distance(48, 49):.3f} Å")
