from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.mep import NEB
from ase.optimize import BFGS

# Build initial and final states: two fixed Al at (0,0,0) and (0,0,4), moving Al between them
cell = [6, 6, 6]
initial = Atoms('Al3', positions=[[0,0,0], [0,0,4], [0,0,1]], cell=cell, pbc=False)
final   = Atoms('Al3', positions=[[0,0,0], [0,0,4], [0,0,3]], cell=cell, pbc=False)

# Keep the two end atoms fixed during relaxation
fix = FixAtoms(indices=[0, 1])
initial.set_constraint(fix)
final.set_constraint(fix)

# Create NEB images: initial + 3 intermediate + final
images = [initial] + [initial.copy() for _ in range(3)] + [final]
for img in images:
    img.set_constraint(fix)
    img.calc = EMT()

# Linear interpolation
neb = NEB(images)
neb.interpolate(method='linear')

# Optimize the NEB path
opt = BFGS(neb, logfile=None)
opt.run(fmax=0.05, steps=200)

# Print energy of each image
for i, img in enumerate(images):
    print(f"Image {i}: energy = {img.get_potential_energy():.6f} eV")
