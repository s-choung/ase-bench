from ase import Atoms, units
from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms, FixBondLength
from ase.optimize import BFGS
from ase.io import write

# Slab
slab = fcc111('Pt', size=(3, 3, 3), vacuum=10.0)

# CO molecule
co = molecule('CO')
add_adsorbate(slab, co, height=1.8, position='ontop')

# Fix bottom layer
mask = [atom.tag == 1 for atom in slab]  # bottom layer atoms
slab.set_constraint([FixAtoms(mask=mask), FixBondLength(co, 0, 1)])

# Setup
slab.calc = EMT()
slab.set_calculator(slab.calc)

# Center and velocity
from ase.md.velocitydistribution import Stationary, ZeroRotation
Stationary(slab)
ZeroRotation(slab)

# Optimize
opt = BFGS(slab)
opt.run(fmax=0.05)

# Output
co_distance = co.get_distance(0, 1)
print(f'Final energy: {slab.get_potential_energy():.6f} eV')
print(f'C-O distance: {co_distance:.3f} Å')
