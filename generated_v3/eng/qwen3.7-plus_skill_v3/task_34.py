from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT
from ase.mep import NEB
from ase.optimize import BFGS
from ase.constraints import FixAtoms

slab = fcc111('Cu', size=(2, 2, 4), vacuum=10.0, a=3.615)

initial = slab.copy()
add_adsorbate(initial, 'Cu', height=2.0, position='fcc')

final = slab.copy()
add_adsorbate(final, 'Cu', height=2.0, position='hcp')

mask = [atom.tag >= 3 for atom in initial]
constraint = FixAtoms(mask=mask)

images = [initial] + [initial.copy() for _ in range(5)] + [final]

for img in images:
    img.set_constraint(constraint)
    img.calc = EMT()

neb = NEB(images)
neb.interpolate(method='idpp')

BFGS(neb).run(fmax=0.05)

energies = [img.get_potential_energy() for img in images]
barrier = max(energies) - energies[0]
print(f"Energy barrier: {barrier:.4f} eV")
