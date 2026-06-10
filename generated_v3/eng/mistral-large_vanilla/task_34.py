from ase import Atoms
from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.neb import NEB, IDPP
from ase.io import write

# Create slab and adatom
slab = fcc111('Cu', size=(2, 2, 3), vacuum=10)
adatom = Atoms('Cu', positions=[[0, 0, 10]])
slab += adatom

# Initial and final positions (fcc to hcp hollow)
initial = slab.copy()
final = slab.copy()
final.positions[-1] += [1.476, 0, 0]  # Shift adatom to hcp site

# Relax endpoints
for atoms in [initial, final]:
    atoms.calc = EMT()
    BFGS(atoms).run(fmax=0.05)

# Create NEB with IDPP interpolation
images = [initial]
images += [initial.copy() for _ in range(3)]
images += [final]
neb = NEB(images, climb=True, method='improvedtangent')
neb.interpolate(IDPP)

# Run NEB calculation
for img in images:
    img.calc = EMT()
BFGS(neb).run(fmax=0.05)

# Calculate and print energy barrier
energies = [img.get_potential_energy() for img in images]
barrier = max(energies) - energies[0]
print(f"Energy barrier: {barrier:.3f} eV")
