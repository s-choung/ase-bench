from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT
from ase.mep import NEB
from ase.optimize import BFGS

# 1. Setup Slab
slab = fcc111('Cu', size=(3, 3, 3), vacuum=10.0)
slab.calc = EMT()

# 2. Initial State (fcc hollow)
initial = slab.copy()
add_adsorbate(initial, 'Cu', height=1.5, position='fcc')
initial.calc = EMT()

# 3. Final State (hcp hollow)
final = slab.copy()
add_adsorbate(final, 'Cu', height=1.5, position='hcp')
final.calc = EMT()

# 4. NEB Setup
images = [initial] + [initial.copy() for _ in range(5)] + [final]
for img in images:
    img.calc = EMT()

neb = NEB(images)
neb.interpolate(method='idpp')

# Optimize images
optimizer = BFGS(neb)
optimizer.run(fmax=0.05)

# 5. Calculate Barrier
energies = [img.get_potential_energy() for img in images]
barrier = max(energies) - energies[0]
print(f"Diffusion Barrier: {barrier:.4f} eV")
