from ase.build import fcc111, add_adsorbate
from ase.neb import NEB, IDPP
from ase.optimize import FIRE
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms

# Build constrained Cu FCC(111) slab
slab = fcc111('Cu', size=(2,2,3), vacuum=10.0)
slab.set_tags([0]*4 + [1]*4 + [2]*4)
slab.set_constraint(FixAtoms(mask=[t < 2 for t in slab.get_tags()]))

# Initial (fcc hollow) and final (hcp hollow) adatom structures
initial = slab.copy()
add_adsorbate(initial, 'Cu', height=2.0, position=(0.0, 0.0))
final = slab.copy()
hcp_pos = (slab.cell[0][0]/3, slab.cell[1][1]/3)
add_adsorbate(final, 'Cu', height=2.0, position=hcp_pos)

# 5 images with IDPP interpolation
images = [initial.copy() for _ in range(5)]
images[-1] = final.copy()
neb = NEB(images, interpolator=IDPP())
neb.interpolate()

# Assign EMT calculator and optimize
for img in images:
    img.calc = EMT()
opt = FIRE(neb)
opt.run(fmax=0.01)

# Compute and print energy barrier
energies = [img.get_potential_energy() for img in images]
print(f'Energy barrier: {max(energies) - energies[0]:.3f} eV')
