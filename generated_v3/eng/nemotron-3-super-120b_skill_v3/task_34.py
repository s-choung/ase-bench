from ase import Atom
from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.optimize import BFGS
from ase.mep import NEB

# Build Cu(111) slab
slab = fcc111('Cu', size=(3, 3, 4), vacuum=10.0)

# Cu adatom
ad = Atom('Cu')

# Initial (fcc hollow)
slab_i = slab.copy()
add_adsorbate(slab_i, ad, height=2.0, position='fcc')
# Fix all slab atoms, let only the adatom move
mask_i = [atom.tag >= 3 for atom in slab_i]  # tag >=3 for adatom? easier: fix all but last
# Actually we know adatom is last added:
fix_i = [idx for idx in range(len(slab_i)) if idx != len(slab_i)-1]
slab_i.set_constraint(FixAtoms(indices=fix_i))
slab_i.calc = EMT()

# Final (hcp hollow)
slab_f = slab.copy()
add_adsorbate(slab_f, ad, height=2.0, position='hcp')
fix_f = [idx for idx in range(len(slab_f)) if idx != len(slab_f)-1]
slab_f.set_constraint(FixAtoms(indices=fix_f))
slab_f.calc = EMT()

# Create images (5 total -> 3 intermediates)
images = [slab_i] + [slab_i.copy() for _ in range(3)] + [slab_f]
for im in images:
    im.calc = EMT()

# NEB with IDPP interpolation
neb = NEB(images)
neb.interpolate(method='idpp')
BFGS(neb).run(fmax=0.05)

# Energies and barrier
energies = [im.get_potential_energy() for im in images]
barrier = max(energies) - energies[0]
print(f'Diffusion barrier: {barrier:.3f} eV')
