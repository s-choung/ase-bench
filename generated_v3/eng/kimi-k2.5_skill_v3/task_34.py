from ase.build import fcc111, add_adsorbate
from ase.constraints import FixAtoms
from ase.calculators.emt import EMT
from ase.mep import NEB
from ase.optimize import BFGS

slab = fcc111('Cu', size=(2, 2, 4), vacuum=10.0)

initial = slab.copy()
add_adsorbate(initial, 'Cu', height=1.8, position='fcc')

final = slab.copy()
add_adsorbate(final, 'Cu', height=1.8, position='hcp')

constraint = FixAtoms(indices=list(range(len(slab))))
initial.set_constraint(constraint)
final.set_constraint(constraint)

images = [initial] + [initial.copy() for _ in range(5)] + [final]
for img in images:
    img.calc = EMT()

neb = NEB(images)
neb.interpolate(method='idpp')
BFGS(neb).run(fmax=0.05)

energies = [img.get_potential_energy() for img in images]
barrier = max(energies) - energies[0]
print(f"Energy barrier: {barrier:.3f} eV")
