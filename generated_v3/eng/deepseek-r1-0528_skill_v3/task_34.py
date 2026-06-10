from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.mep import NEB
from ase.optimize import BFGS
import numpy as np

slab = fcc111('Cu', size=(2, 2, 4), vacuum=10.0)
n_slab_atoms = len(slab)
slab_cell = slab.get_cell()

z_positions = slab.get_positions()[:, 2]
unique_z = np.unique(z_positions)
constraint_indices = [atom.index for atom in slab 
                      if atom.position[2] < unique_z[1] + 0.1]

initial = slab.copy()
initial.append('Cu')
initial.positions[-1] = [slab_cell[0, 0] / 3, slab_cell[1, 1] / 3, z_positions.max() + 2.0]

final = initial.copy()
final.positions[-1] = [2 * slab_cell[0, 0] / 3, 2 * slab_cell[1, 1] / 3, z_positions.max() + 2.0]

constraint = FixAtoms(indices=constraint_indices)
initial.set_constraint(constraint)
final.set_constraint(constraint)

images = [initial] + [initial.copy() for _ in range(5)] + [final]
for image in images:
    image.calc = EMT()

neb = NEB(images, climb=True)
neb.interpolate(method='idpp')
opt = BFGS(neb, trajectory='neb.traj')
opt.run(fmax=0.05)

E0 = images[0].get_potential_energy()
E_max = max(image.get_potential_energy() for image in images)
dE = E_max - E0
print(f'Energy barrier: {dE:.3f} eV')
