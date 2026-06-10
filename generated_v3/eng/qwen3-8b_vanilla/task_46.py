import numpy as np
from ase import Atoms, fcc111
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms, FixBondLength
from ase.optimize import BFGS

slab = fcc111('Pt', size=(3, 3, 3), a=3.92, vacuum=10.0)
co = Atoms('CO', positions=[[0.5, 0.5, 0.0], [0.5, 0.5, 1.1]], calculator=EMT())
slab += co

bottom_layer_indices = list(range(9))
constraint1 = FixAtoms(indices=bottom_layer_indices)
co_indices = [-2, -1]
constraint2 = FixBondLength(indices=co_indices, bond_length=1.1)

slab.calc = EMT()
opt = BFGS(slab, constraints=[constraint1, constraint2], fmax=0.05)
opt.run()

print(f"Final energy: {slab.get_potential_energy()} eV")
c_pos = slab.get_positions()[-2]
o_pos = slab.get_positions()[-1]
print(f"C-O distance: {np.linalg.norm(c_pos - o_pos):.3f} Å")
