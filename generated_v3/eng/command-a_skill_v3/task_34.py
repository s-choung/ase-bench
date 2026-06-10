from ase import Atoms
from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.mep import NEB
from ase.optimize import BFGS

# Create initial and final states
slab = fcc111('Cu', size=(2, 2, 2), vacuum=10.0)
initial = slab.copy()
final = slab.copy()

# Place adatom in fcc hollow (initial) and hcp hollow (final)
initial.extend(Atoms('Cu', positions=[[0.5, 0.5, 1.8],]))  # fcc hollow
final.extend(Atoms('Cu', positions=[[0.5, 0.0, 1.8],]))   # hcp hollow

# Set up NEB calculation
images = [initial] + [initial.copy() for _ in range(5)] + [final]
for img in images[1:-1]:
    img.calc = EMT()

neb = NEB(images)
neb.interpolate(method='idpp')

# Optimize NEB path
opt = BFGS(neb)
opt.run(fmax=0.05)

# Calculate and print energy barrier
energies = [img.get_potential_energy() for img in images]
barrier = max(energies) - energies[0]
print(f'Energy barrier: {barrier:.3f} eV')
