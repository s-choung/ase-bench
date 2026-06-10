from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.neb import NEB
from ase.optimize import MDMin
from ase.constraints import FixAtoms
import numpy as np

# Build Cu(111) slab
slab = fcc111('Cu', size=(4, 4, 4), vacuum=10.0)
slab.calc = EMT()
z0 = slab.positions[:, 2].max()
constraint = FixAtoms(mask=[atom.symbol == 'Cu' and atom.position[2] < z0 - 0.1 for atom in slab])
slab.set_constraint(constraint)

# Initial adatom at fcc hollow
adatom_i = slab.copy()
adatom_i.append('Cu')
pos_i = adatom_i.positions[-1]
pos_i[0] = 1.5
pos_i[1] = np.sqrt(3)/2
pos_i[2] = z0 + 2.0
adatom_i.positions[-1] = pos_i

# Final adatom at hcp hollow
adatom_f = slab.copy()
adatom_f.append('Cu')
pos_f = adatom_f.positions[-1]
pos_f[0] = 3.0
pos_f[1] = np.sqrt(3)
pos_f[2] = z0 + 2.0
adatom_f.positions[-1] = pos_f

# NEB with 5 images, IDPP interpolation
images = [adatom_i]
for i in range(5):
    images.append(adatom_i.copy())
images.append(adatom_f)
neb = NEB(images, climb=False)
neb.interpolate('idpp')

# Optimize path
for image in images:
    image.calc = EMT()
    image.set_constraint(constraint)
optimizer = MDMin(neb, trajectory='neb.traj', logfile=None)
optimizer.run(fmax=0.05)

# Compute energy barrier
energies = [image.get_potential_energy() for image in images]
e0 = energies[0]
emax = max(energies)
barrier = emax - e0
print(barrier)
