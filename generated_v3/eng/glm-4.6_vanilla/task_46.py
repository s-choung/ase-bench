from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.constraints import FixAtoms, FixBondLength
import numpy as np

slab = fcc111('Pt', size=(2, 2, 3), vacuum=10.0)
add_adsorbate(slab, 'CO', height=1.5, position='ontop')

slab.calc = EMT()

bottom_layer = [atom.index for atom in slab if atom.position[2] < slab.positions[:, 2].mean() - 1.0]
c_atom = [atom.index for atom in slab if atom.symbol == 'C'][0]
o_atom = [atom.index for atom in slab if atom.symbol == 'O'][0]

slab.set_constraint([FixAtoms(indices=bottom_layer), FixBondLength(c_atom, o_atom)])

opt = BFGS(slab, trajectory=None)
opt.run(fmax=0.05)

co_distance = slab.get_distance(c_atom, o_atom)
print(f"Final energy: {slab.get_potential_energy():.3f} eV")
print(f"C-O distance: {co_distance:.3f} Å")
