from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.interpolate import idpp_interpolate
from ase.neb import NEB
from ase.optimize import BFGS

# Create 3-layer 3x3 Cu(111) slab with vacuum
clean_slab = fcc111('Cu', size=(3, 3, 3), vacuum=10.0, a=3.614)
max_z = clean_slab.positions[:, 2].max()
lx, ly = clean_slab.cell[0, 0], clean_slab.cell[1, 1]

# Initial state: Cu adatom at fcc hollow site
initial = clean_slab.copy()
initial.append('Cu')
initial.positions[-1] = [lx/3, ly/3, max_z + 1.9]

# Final state: Cu adatom at adjacent hcp hollow site
final = clean_slab.copy()
final.append('Cu')
final.positions[-1] = [2*lx/3, ly/3, max_z + 1.9]

# Initialize 5 total NEB images
images = [initial.copy() for _ in range(5)]
images[-1] = final.copy()

# Assign calculators and perform IDPP interpolation
for atoms in images:
    atoms.calc = EMT()
idpp_interpolate(images, apply_constraint=True)

# Relax NEB path
neb = NEB(images, k=0.1)
opt = BFGS(neb)
opt.run(fmax=0.05)

# Calculate and print energy barrier
energies = [atoms.get_potential_energy() for atoms in images]
barrier = max(energies) - energies[0]
print(f"Energy barrier: {barrier:.3f} eV")
