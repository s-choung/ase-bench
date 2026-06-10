from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.optimize import BFGS
from ase.mep import NEB
from ase import Atoms

# Create Cu(111) slab (3x3, 4 layers, 10Å vacuum)
slab = fcc111('Cu', size=(3, 3, 4), vacuum=10.0)

# Fix bottom two layers (tags 1 and 2)
slab.set_constraint(FixAtoms(mask=[a.tag <= 2 for a in slab]))

# Adatom and adsorption height
adatom = Atoms('Cu')
height = 1.8

# Initial state: adatom at fcc hollow
initial = slab.copy()
add_adsorbate(initial, adatom, height, position='fcc')
initial.calc = EMT()

# Final state: adatom at hcp hollow
final = slab.copy()
add_adsorbate(final, adatom, height, position='hcp')
final.calc = EMT()

# NEB with 5 intermediate images (7 total)
images = [initial] + [initial.copy() for _ in range(5)] + [final]
for img in images[1:-1]:
    img.calc = EMT()

neb = NEB(images)
neb.interpolate(method='idpp')

BFGS(neb, trajectory='neb.traj').run(fmax=0.05)

energies = [img.get_potential_energy() for img in images]
barrier = max(energies) - energies[0]
print(f"Diffusion barrier: {barrier:.4f} eV")
