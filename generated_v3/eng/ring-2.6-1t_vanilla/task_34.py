from ase import Atoms
from ase.build import fcc111, add_adsorbate
from ase.constraints import FixAtoms
from ase.calculators.emt import EMT
from ase.neb import NEB
from ase.optimize import QuasiNewton

# Slab
slab = fcc111('Cu', size=(3, 3, 4), vacuum=10.0)
# Fix the two bottom layers
mask = [a.tag < 2 for a in slab]
slab.set_constraint(FixAtoms(mask=mask))

# Surface lattice vectors (in-plane)
a1, a2 = slab.cell[0], slab.cell[1]

# fcc and hcp hollow positions (2‑D fractional coordinates)
pos_fcc = (1/3) * a1 + (2/3) * a2
pos_hcp = (2/3) * a1 + (1/3) * a2

z_top = slab.positions[:, 2].max()
height = 1.8                     # adatom height above surface (Å)

# Initial and final configurations
initial = slab.copy()
initial.append(Atoms('Cu', positions=[pos_fcc + [z_top + height]]))
final = slab.copy()
final.append(Atoms('Cu', positions=[pos_hcp + [z_top + height]]))

# NEB setup (5 images, endpoints included)
images = [initial]
for _ in range(3):
    images.append(initial.copy())
images.append(final)

neb = NEB(images, k=0.1)
neb.interpolate('idpp')

# Attach calculator and relax
for img in images:
    img.calc = EMT()

qn = QuasiNewton(neb, trajectory='neb.traj')
qn.run(fmax=0.05)

# Energy barrier
energies = [img.get_potential_energy() for img in images]
barrier = max(energies) - energies[0]
print(f'Energy barrier = {barrier:.4f} eV')
