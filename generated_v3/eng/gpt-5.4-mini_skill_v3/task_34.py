import numpy as np
from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.mep import NEB
from ase.optimize import BFGS

slab = fcc111('Cu', size=(2, 2, 4), vacuum=10.0, orthogonal=True)
slab.calc = EMT()

z = slab.positions[:, 2].max()
fcc_pos = (0.0, 0.0)
hcp_pos = (slab.cell[0, 0] / 3.0, slab.cell[1, 1] / 3.0)

initial = slab.copy()
add_adsorbate(initial, 'Cu', height=1.8, position=fcc_pos)
initial.set_constraint(FixAtoms(mask=[a.tag > 1 for a in initial]))
initial.calc = EMT()

final = slab.copy()
add_adsorbate(final, 'Cu', height=1.8, position=hcp_pos)
final.set_constraint(FixAtoms(mask=[a.tag > 1 for a in final]))
final.calc = EMT()

images = [initial] + [initial.copy() for _ in range(5)] + [final]
for img in images[1:-1]:
    img.calc = EMT()

neb = NEB(images)
neb.interpolate(method='idpp')
BFGS(neb, trajectory='neb.traj').run(fmax=0.05)

energies = [img.get_potential_energy() for img in images]
barrier = max(energies) - energies[0]
print(f"Energy barrier: {barrier:.6f} eV")
