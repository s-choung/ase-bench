from ase import Atom, Atoms
from ase.build import fcc111, molecule, add_adsorbate
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms, FixBondLength
from ase.optimize import BFGS

slab = fcc111('Pt', size=(2, 2, 3), vacuum=10.0)
co = molecule('CO')
add_adsorbate(slab, co, height=2.0, position=(0, 0))
slab.set_constraint([FixAtoms(indices=range(8, 12)), FixBondLength(12, 13, 1.13)])
slab.calc = EMT()
BFGS(slab).run(fmax=0.05)
print(f"{slab.get_potential_energy():.3f}")
print(f"{slab.get_distance(12, 13):.3f}")
