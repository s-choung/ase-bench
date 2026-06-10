from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.neb import NEB

# Create initial surface with adatom on fcc hollow
slab = fcc111('Cu', size=(1, 1, 1), vacuum=10.0)
add_adsorbate(slab, 'Cu', height=1.8, position='ontop')

# Create final structure with adatom on hcp hollow
final = slab.copy()
final[0].position = [0.5, 0.5, 1.8]  # Example hcp position

# Set up NEB with 5 images
images = [slab] + [slab.copy() for _ in range(3)] + [final]
neb = NEB(images)
neb.interpolate(method='idpp')

# Set calculators
for img in images:
    img.calc = EMT()

# Optimize NEB path
opt = BFGS(neb)
opt.run(fmax=0.05)

# Calculate energy barrier
energies = [img.get_energy() for img in images]
barrier = max(energies) - slab.get_energy()
print(f"Energy barrier: {barrier} eV")
