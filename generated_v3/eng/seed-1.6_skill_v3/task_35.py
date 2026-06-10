from ase import Atoms
from ase.constraints import FixAtoms
from ase.mep import NEB
from ase.optimize import BFGS
from ase.calculators.emt import EMT

# Initial state: 2 fixed Al, moving Al at 0.5Å
initial = Atoms('Al3', positions=[(0,0,0), (2,0,0), (0.5,0,0)], pbc=False)
initial.set_constraint(FixAtoms(indices=[0,1]))
initial.calc = EMT()

# Final state: moving Al at 1.5Å
final = Atoms('Al3', positions=[(0,0,0), (2,0,0), (1.5,0,0)], pbc=False)
final.set_constraint(FixAtoms(indices=[0,1]))
final.calc = EMT()

# 3 images total
images = [initial, initial.copy(), final]

# NEB setup with linear interpolation
neb = NEB(images)
neb.interpolate(method='linear')
images[1].calc = EMT()

# Optimize
BFGS(neb).run(fmax=0.05)

# Print image energies
for i, img in enumerate(images):
    print(f'Image {i} energy: {img.get_potential_energy():.4f} eV')
