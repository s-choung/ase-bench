from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.neb import NEB
from ase.optimize import QuasiNewton

# fixed Al dimer positions (Å)
d = 2.8
fixed = [[0., 0., 0.], [d, 0., 0.]]

# initial and final position of the moving atom (above / below the dimer)
z0 = 1.5
init_pos = [d/2, 0., z0]
final_pos = [d/2, 0., -z0]

initial = Atoms('Al3', positions=fixed + [init_pos],
                constraints=[FixAtoms(indices=[0, 1])])
final = initial.copy()
final.positions[2] = final_pos

# linear interpolation for the middle image
middle = initial.copy()
middle.positions[2] = (init_pos + final_pos) / 2.

images = [initial, middle, final]

for img in images:
    img.calc = EMT()

neb = NEB(images, k=5.0)
opt = QuasiNewton(neb, trajectory='neb.traj')
opt.run(fmax=0.05)

for i, img in enumerate(images):
    print(f'Image {i}: {img.get_potential_energy():.4f} eV')
