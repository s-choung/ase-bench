from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.mep import NEB
from ase.constraints import FixAtoms

slab = fcc111('Cu', size=(3, 3, 4), vacuum=10.0)
slab.set_constraint(FixAtoms(mask=[a.tag <= 2 for a in slab]))

initial = slab.copy()
initial.set_constraint(FixAtoms(mask=[a.tag <= 2 for a in initial]))
add_adsorbate(initial, 'Cu', height=1.6, position='fcc')
initial.calc = EMT()

final = slab.copy()
final.set_constraint(FixAtoms(mask=[a.tag <= 2 for a in final]))
add_adsorbate(final, 'Cu', height=1.6, position='hcp')
final.calc = EMT()

images = [initial] + [initial.copy() for _ in range(5)] + [final]
neb = NEB(images, method='idpp')
neb.interpolate()

for img in images[1:-1]:
    img.calc = EMT()

BFGS(neb, trajectory='neb.traj').run(fmax=0.05)

energies = [img.get_potential_energy() for img in images]
barrier = max(energies[1:-1]) - energies[0]
print(f"Energy barrier: {barrier:.4f} eV")
