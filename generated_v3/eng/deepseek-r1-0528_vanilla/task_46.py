from ase.build import fcc111, add_adsorbate
from ase.constraints import FixAtoms, FixBondLength
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.io import read
import numpy as np

# Build 3-layer Pt(111) slab
slab = fcc111('Pt', size=(2, 2, 3), vacuum=10.0)
slab.center()

# Create CO molecule and place on Pt slab
co = read('CO.xyz')  # CO molecule from built-in example
add_adsorbate(slab, co, height=2.0, position='ontop')

# Identify atom indices for constraints
bottom_layer_indices = [atom.index for atom in slab if atom.tag == 0]  # Bottom layer tagged 0
slab.set_constraint(FixAtoms(indices=bottom_layer_indices))

# Identify C and O atoms (last two atoms added)
c_atom = slab[-2]
o_atom = slab[-1]
slab.append(FixBondLength(c_atom.index, o_atom.index))

# Set calculator and optimize
slab.calc = EMT()
opt = BFGS(slab, trajectory=None, logfile=None)
opt.run(fmax=0.05)

# Output results
eo = slab.get_potential_energy()
d_co = np.linalg.norm(slab.get_positions()[-2] - slab.get_positions()[-1])
print(f'Final energy: {eo:.3f} eV')
print(f'C-O distance: {d_co:.3f} Å')
