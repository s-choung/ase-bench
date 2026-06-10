from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.mep import NEB
from ase.mep.idpp import IDPP
from ase.optimize import BFGS

# Build Cu(111) slab (3 layers, 4x4 surface)
slab = fcc111('Cu', size=(4, 4, 3), vacuum=10.0)

# fcc and hcp hollow sites on Cu(111)
# Both lie above the surface; difference is stacking (fcc = atop a hollow of layer 2)
# Use cartesian placement at height z above a surface atom's lateral position offset to 3-fold site
a = slab.cell.lengths()[0] / 4  # nearest-neighbor distance in surface plane
z_height = 1.9  # adatom height above surface

# fcc hollow: position offset such that it sits above a triangle of atoms
# Use simple offset coordinates relative to a surface atom
x0, y0 = 1.0/3 * a, 1.0/3 * a
x1, y1 = 2.0/3 * a, 2.0/3 * a

initial = slab.copy()
add_adsorbate(initial, 'Cu', z_height, position=(x0, y0))
final = slab.copy()
add_adsorbate(final, 'Cu', z_height, position=(x1, y1))

# Fix bottom layer
for atoms in [initial, final]:
    mask = [atom.tag > 1 for atom in atoms]  # bottom layer is tag 0
    atoms.set_constraint(FixAtoms(mask=mask))
    atoms.calc = EMT()

images = [initial] + [initial.copy() for _ in range(5)] + [final]
for img in images:
    img.calc = EMT()

# IDPP interpolation
neb = NEB(images, k=0.1, climb=True)
neb.interpolate(method='idpp')

# Optimize
opt = BFGS(neb, logfile=None)
opt.run(fmax=0.05, steps=200)

# Compute energy barrier
energies = [img.get_potential_energy() for img in images]
e_initial = energies[0]
e_max = max(energies)
barrier = e_max - e_initial
print(f"Energy barrier: {barrier:.4f} eV")
