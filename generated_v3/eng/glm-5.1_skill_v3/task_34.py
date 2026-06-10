from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.optimize import BFGS
from ase.mep import NEB

# Build initial and final states
slab = fcc111('Cu', size=(2, 2, 3), vacuum=10.0)

initial = slab.copy()
add_adsorbate(initial, 'Cu', height=1.8, position='fcc')

final = slab.copy()
add_adsorbate(final, 'Cu', height=1.8, position='hcp')

# Fix bottom two layers (8 atoms in a 2x2x3 slab)
constraint = FixAtoms(indices=list(range(8)))

# Relax initial and final states
for atoms in [initial, final]:
    atoms.calc = EMT()
    atoms.set_constraint(constraint)
    BFGS(atoms).run(fmax=0.05)

# Setup NEB with 5 intermediate images
images = [initial] + [initial.copy() for _ in range(5)] + [final]
neb = NEB(images)
neb.interpolate(method='idpp')

# Attach calculators to intermediate images
for img in images[1:-1]:
    img.calc = EMT()

# Run NEB optimization
opt = BFGS(neb)
opt.run(fmax=0.05)

# Calculate and print energy barrier
energies = [img.get_potential_energy() for img in images]
barrier = max(energies) - energies[0]
print(f"Energy barrier: {barrier:.4f} eV")
