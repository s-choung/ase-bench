from ase.build import fcc111, add_adsorbate
from ase.constraints import FixAtoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.neb import NEB
from ase.io.trajectory import Trajectory
from ase.build.tools import minimize_rotation_and_translation

slab = fcc111('Cu', size=(3, 3, 3), a=3.6, vacuum=10.0)
add_adsorbate(slab, 'Cu', height=1.7, position='fcc')
slab.set_calculator(EMT())

c = FixAtoms(indices=[atom.index for atom in slab if atom.position[2] < 8.0])
slab.set_constraint(c)

initial = slab.copy()
final = slab.copy()
final.positions[-1] = slab.positions[-1] + [1 / 3, 1 / 3, 0.0]
minimize_rotation_and_translation(initial, final)

images = [initial]
for i in range(3):
    img = initial.copy()
    images.append(img)
images.append(final)

neb = NEB(images, climb=True)
neb.interpolate('idpp')
neb.set_calculator(EMT())

opt = BFGS(neb, trajectory='neb.traj')
opt.run(fmax=0.05)

traj = Trajectory('neb.traj')
energies = [image.get_potential_energy() for image in traj]
energy_barrier = max(energies) - energies[0]

print(f'Energy barrier: {energy_barrier:.3f} eV')
