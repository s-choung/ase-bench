import numpy as np
from ase import Atoms
from ase.calculators.emt import EMT
from ase.mep import NEB
from ase.optimize import BFGS
from ase.constraints import FixAtoms

# --- Define initial and final states ---
# Two fixed Al atoms at x=0 and x=5; third Al moves between them
initial = Atoms('Al3',
                positions=[(0.0, 0.0, 0.0),    # fixed left
                           (1.0, 0.0, 0.0),    # mobile: left side
                           (5.0, 0.0, 0.0)])   # fixed right
initial.set_constraint(FixAtoms(indices=[0, 2]))  # fix atom 0 and atom 2
initial.calc = EMT()

final = initial.copy()
final.positions[1] = [4.0, 0.0, 0.0]  # mobile atom moved to right side

# --- Build NEB images: 3 intermediate + initial + final = 5 images ---
n_images = 3
images = [initial] + [initial.copy() for _ in range(n_images)] + [final]
neb = NEB(images, climb=True)
neb.interpolate(method='linear')

# Set calculator on intermediate images only (initial and final already have one)
for img in images[1:-1]:
    img.calc = EMT()

# --- Optimize NEB ---
opt = BFGS(neb)
opt.run(fmax=0.05)

# --- Print energies ---
print("\nImage  |  Energy (eV)")
print("-" * 30)
for i, img in enumerate(images):
    e = img.get_potential_energy()
    tag = ""
    if i == 0:
        tag = " (initial)"
    elif i == len(images) - 1:
        tag = " (final)"
    print(f"  {i:2d}    |  {e:8.4f}{tag}")
