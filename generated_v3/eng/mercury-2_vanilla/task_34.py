# ASE script: NEB diffusion barrier for Cu adatom fcc→hcp on Cu(111)
from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT
from ase.neb import NEB, IDPP
from ase.optimize import BFGS

# Build Cu(111) slab
slab = fcc111('Cu', size=(3, 3, 4), vacuum=10.0, periodic=True)

# Initial (fcc) and final (hcp) configurations
initial = slab.copy()
add_adsorbate(initial, 'Cu', height=1.8, position='fcc')
final = slab.copy()
add_adsorbate(final, 'Cu', height=1.8, position='hcp')

# Create images (5 total: initial + 3 intermediates + final)
images = [initial] + [initial.copy() for _ in range(3)] + [final]

# IDPP interpolation for intermediate images
idpp = IDPP(images[1:-1])
idpp.interpolate()

# Attach EMT calculator to all images
calc = EMT()
for img in images:
    img.set_calculator(calc)

# NEB setup and optimization
neb = NEB(images)
optimizer = BFGS(neb)
optimizer.run(fmax=0.05)

# Energy barrier
energies = [img.get_potential_energy() for img in images]
barrier = max(energies) - energies[0]
print(f'Diffusion barrier: {barrier:.3f} eV')
