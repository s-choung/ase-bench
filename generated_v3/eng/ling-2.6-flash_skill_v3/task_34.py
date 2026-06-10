from ase import Atoms
from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.neb import NEB
from ase.optimize import BFGS
from ase.mep import DyNEB, IDPPRateCalculator

# Build Cu(111) slab
slab = fcc111('Cu', size=(3, 3, 3), vacuum=15.0, a=3.6)
slab.set_constraint(FixAtoms(mask=[a.z > slab.get_position(0)[2] for a in slab]))

# Add Cu adatom at fcc hollow site
add_adsorbate(slab, 'Cu', height=2.0, position='fcc')
adatom_index = len(slab) - 1
slab.calc = EMT()

# Optimize initial state
BFGS(slab).run(fmax=0.05)

# Create initial and final images
initial = slab.copy()
final = slab.copy()

# Move adatom from fcc to hcp hollow by translating by a lattice vector
a_vec = final.get_scaled_positions()[adatom_index]
a_vec[0] += 1/3
a_vec[1] += 2/3
final.set_scaled_positions([a_vec if i == adatom_index else final.get_scaled_positions()[i] for i in range(len(final))])

# Generate NEB images with IDPP interpolation
images = [initial] + [initial.copy() for _ in range(5)] + [final]
neb = NEB(images)
neb.interpolate(method='idpp')

# Set calculator and IDPP rate calculator for each image
for img in images[1:-1]:
    img.calc = EMT()
idp = IDPPRateCalculator()
neb.set_idpp_calculator(idp)

# Optimize NEB
dyn = DyNEB(neb, trajectory='neb.traj')
dyn.run(fmax=0.05)

# Calculate and print energy barrier
energies = [img.get_potential_energy() for img in images]
energy_barrier = max(energies) - energies[0]
print(f'Energy barrier: {energy_barrier:.3f} eV')
