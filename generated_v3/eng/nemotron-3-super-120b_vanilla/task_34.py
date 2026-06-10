from ase.build import fcc111, add_adsorbate
from ase import Atoms
from ase.calculators.emt import EMT
from ase.neb import NEB
from ase.optimize import BFGS

# Cu(111) slab
slab = fcc111('Cu', size=(2,2,3), vacuum=10.0)

# Single Cu adatom
adatom = Atoms('Cu', positions=[[0,0,0]])

# Initial (fcc hollow) and final (hcp hollow) states
initial = slab.copy()
add_adsorbate(initial, adatom, height=2.0, position='fcc')
final = slab.copy()
add_adsorbate(final, adatom, height=2.0, position='hcp')

# EMT calculator
calc = EMT()
initial.set_calculator(calc)
final.set_calculator(calc)

# NEB images (5 total, including endpoints)
n_images = 5
images = [initial.copy() for _ in range(n_images)]
images[0] = initial
images[-1] = final
for img in images:
    img.set_calculator(calc)

# IDPP interpolation and NEB setup
neb = NEB(images, climb=False)
neb.interpolate(method='idpp')

# Optimize the band
opt = BFGS(neb)
opt.run(fmax=0.05)

# Compute barrier (max energy minus initial energy)
energies = [img.get_potential_energy() for img in images]
barrier = max(energies) - energies[0]
print(f'Diffusion barrier: {barrier:.3f} eV')
