from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.neb import NEB
from ase.optimize import BFGS
from ase.io import write

# Create surface and adatom in initial (fcc hollow) and final (hcp hollow) positions
slab = fcc111('Cu', size=(3, 3, 4), vacuum=10.0)
initial = slab.copy()
final = slab.copy()

# Initial position: fcc hollow site (atoms are 1-indexed in ASE's fcc111)
initial.append('Cu')
initial[-1].position = (1., 1., slab.cell[2, 2] * 3/4 + 1.8)  # fcc hollow

# Final position: hcp hollow site
final.append('Cu')
final[-1].position = (0., 0., slab.cell[2, 2] * 3/4 + 1.8)  # hcp hollow

# Fix all slab atoms below top 2 layers
mask = [a.index < len(slab) - 18 for a in initial]  # 3x3 surface: 9 atoms/layer * 2 layers = 18
initial.set_constraint(FixAtoms(mask=mask))
final.set_constraint(FixAtoms(mask=mask))

# Set calculator
initial.calc = EMT()
final.calc = EMT()

# Create NEB images
images = [initial] + [initial.copy() for _ in range(5)] + [final]
for image in images[1:-1]:
    image.calc = EMT()
    image.set_constraint(FixAtoms(mask=mask))  # Apply same constraint

# Setup and run NEB
neb = NEB(images)
neb.interpolate(method='idpp')  # IDPP interpolation

# Optimize NEB
qn = BFGS(neb, trajectory='neb_trajectory.traj')
qn.run(fmax=0.05)

# Calculate energy barrier
initial_energy = images[0].get_potential_energy()
max_energy = max(img.get_potential_energy() for img in images)
barrier = max_energy - initial_energy

print(f"Diffusion energy barrier: {barrier:.3f} eV")
write('neb_final.traj', images[-1])  # Save final image
