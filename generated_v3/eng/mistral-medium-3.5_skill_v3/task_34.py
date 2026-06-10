from ase import Atoms
from ase.build import fcc111, add_adsorbate, molecule
from ase.calculators.emt import EMT
from ase.mep import NEB
from ase.optimize import BFGS
from ase.constraints import FixAtoms

slab = fcc111('Cu', size=(3, 3, 3), vacuum=10.0)
slab.calc = EMT()
BFGS(slab).run(fmax=0.05)

initial = slab.copy()
hcp_pos = initial.positions[0] + initial.get_cell()[0]/3 + initial.get_cell()[1]/3
initial.set_constraint(FixAtoms(mask=[a.tag > 0 for a in initial]))
final = initial.copy()
add_adsorbate(final, Atoms('Cu'), position=hcp_pos, height=0.0)

images = [initial] + [initial.copy() for _ in range(3)] + [final]
for img in images[1:-1]:
    img.calc = EMT()

neb = NEB(images, climb=True)
neb.interpolate(method='idpp')

BFGS(neb).run(fmax=0.05)
energies = [img.get_potential_energy() for img in images]
barrier = max(energies) - initial.get_potential_energy()
print(f"Energy barrier: {barrier:.3f} eV")
