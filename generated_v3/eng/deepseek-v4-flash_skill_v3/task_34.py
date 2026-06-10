from ase import Atoms
from ase.build import fcc111, add_adsorbate
from ase.constraints import FixAtoms
from ase.calculators.emt import EMT
from ase.mep import NEB
from ase.optimize import BFGS

# Build base slab
slab = fcc111('Cu', size=(3, 3, 3), a=3.61, vacuum=10.0)

# Initial and final states
initial = slab.copy()
adatom = Atoms('Cu')
add_adsorbate(initial, adatom, height=1.5, position='fcc')

final = slab.copy()
add_adsorbate(final, adatom, height=1.5, position='hcp')

# Fix bottom layer (tag=3) in both endpoints
fix_bottom = FixAtoms(mask=[atom.tag == 3 for atom in initial])
initial.set_constraint(fix_bottom)
final.set_constraint(fix_bottom)

# Set calculators
initial.calc = EMT()
final.calc = EMT()

# Build NEB
images = [initial] + [initial.copy() for _ in range(5)] + [final]
neb = NEB(images)
neb.interpolate(method='idpp')

# Set calculators for interior images
for image in images[1:-1]:
    image.calc = EMT()
    image.set_constraint(fix_bottom)  # same constraint

# Optimize
opt = BFGS(neb, trajectory='neb.traj')
opt.run(fmax=0.05)

# Compute and print barrier
energies = [img.get_potential_energy() for img in images]
barrier = max(energies) - energies[0]
print(f"Energy barrier: {barrier:.4f} eV")
