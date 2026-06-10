from ase.build import fcc111
from ase.build import molecule, add_adsorbate
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.neb import NEB

# Create initial and final states
slab = fcc111('Cu', size=(2, 2, 4), vacuum=10.0)
initial = slab.copy()
final = slab.copy()

# Add Cu adatom at fcc hollow site
Cu_adatom = molecule('Cu')
add_adsorbate(initial, Cu_adatom, height=1.8, position='fcc')
initial.set_constraint(FixAtoms(mask=[atom.tag >= 3 for atom in initial]))  # Fix bottom layers
initial.calc = EMT()

# Add Cu adatom at hcp hollow site
add_adsorbate(final, Cu_adatom, height=1.8, position='hcp')
final.set_constraint(FixAtoms(mask=[atom.tag >= 3 for atom in final]))  # Fix bottom layers
final.calc = EMT()

# Create NEB images
images = [initial] + [initial.copy() for _ in range(4)] + [final]
for image in images[1:-1]:
    image.calc = EMT()

# Interpolate using IDPP
neb = NEB(images, interpolate='idpp')

# Run NEB optimization
optimizer = BFGS(neb)
optimizer.run(fmax=0.05)

# Calculate energy barrier
energies = [image.get_potential_energy() for image in images]
initial_energy = energies[0]
max_energy = max(energies)
energy_barrier = max_energy - initial_energy

print(f"Energy barrier: {energy_barrier} eV")
