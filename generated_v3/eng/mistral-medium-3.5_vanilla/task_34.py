from ase import Atoms
from ase.build import fcc111, add_adsorbate
from ase.neb import NEB
from ase.calculators.emt import EMT
from ase.io.trajectory import Trajectory

# Create Cu(111) surface
slab = fcc111('Cu', (3, 3, 3), periodic=True)
slab.calc = EMT()

# Add Cu adatom at fcc hollow
add_adsorbate(slab, 'Cu', 2.0, 'fcc')

# Create NEB images
images = [slab.copy() for _ in range(5)]
neb = NEB(images, method='idpp')
neb.interpolate()

# Set calculator for all images
for image in images:
    image.calc = EMT()

# Final state: adatom at hcp hollow
images[-1].positions[-1] = images[0].positions[-1] + slab.cell[0]/3 + slab.cell[1]/3

# Run NEB
neb.run()

# Calculate energy barrier
energies = [image.get_total_energy() for image in images]
barrier = max(energies) - energies[0]
print(f"Energy barrier: {barrier:.2f} eV")
