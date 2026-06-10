from ase.build import fcc111, molecule, add_adsorbate
from ase.constraints import FixAtoms, FixBondLength
from ase.calculators.emt import EMT
from ase.optimize import BFGS
import numpy as np

# Build Pt(111) slab (3 layers), size 2x2, vacuum=10 Å
slab = fcc111('Pt', size=(2,2,3), vacuum=10.0)

# CO molecule
co = molecule('CO')

# Adsorb CO, 1.8 Å above ontop
add_adsorbate(slab, co, height=1.8, position='ontop')

# Find indices for bottom layer (lowest z)
z = slab.positions[:,2]
bottom = np.where(z <= np.sort(z)[3])[0]  # bottom 4 atoms (for 2x2 slab)

# Find C and O indices (CO is last two atoms added)
C_idx = len(slab) - 2
O_idx = len(slab) - 1

# Set constraints: fix bottom layer and the C-O bond
constraints = [FixAtoms(indices=bottom), FixBondLength(C_idx, O_idx)]
slab.set_constraint(constraints)

# EMT calculator
slab.calc = EMT()

# Optimize
opt = BFGS(slab)
opt.run(fmax=0.05)

# Output final energy and C-O bond length
energy = slab.get_potential_energy()
co_dist = slab.get_distance(C_idx, O_idx)
print(f'Final energy: {energy:.6f} eV')
print(f'C-O distance: {co_dist:.4f} Å')
