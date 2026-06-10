import numpy as np
from ase.build import fcc111
from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms, FixBondLength
from ase.optimize import BFGS

slab = fcc111('Pt', size=(2, 2, 3), vacuum=10.0)
top_pos = slab[np.argmax(slab.positions[:, 2])].position
system = slab + Atoms('CO', positions=[top_pos + np.array([0, 0, 1.2]), top_pos + np.array([0, 0, 2.3])])
system.set_calculator(EMT())

c_idx, o_idx = len(slab), len(slab) + 1
pt_idx = np.where(system.symbols == 'Pt')[0]
bottom_idx = pt_idx[system.positions[pt_idx, 2] == system.positions[pt_idx, 2].min()].tolist()

system.set_constraint([FixAtoms(indices=bottom_idx), FixBondLength(c_idx, o_idx)])
BFGS(system).run(fmax=0.05)

print(f"Final energy: {system.get_potential_energy():.4f} eV")
print(f"Final C-O distance: {system.get_distance(c_idx, o_idx):.4f} A")
