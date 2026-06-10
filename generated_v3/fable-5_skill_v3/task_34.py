from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.optimize import BFGS
from ase.mep import NEB

slab = fcc111('Cu', size=(3, 3, 4), vacuum=10.0)
mask = [a.tag >= 3 for a in slab]

initial = slab.copy()
add_adsorbate(initial, 'Cu', height=2.0, position='fcc')
initial.set_constraint(FixAtoms(mask=mask))
initial.calc = EMT()
BFGS(initial).run(fmax=0.02)

final = slab.copy()
add_adsorbate(final, 'Cu', height=2.0, position='hcp')
final.set_constraint(FixAtoms(mask=mask))
final.calc = EMT()
BFGS(final).run(fmax=0.02)

images = [initial] + [initial.copy() for _ in range(5)] + [final]
for img in images[1:-1]:
    img.calc = EMT()

neb = NEB(images)
neb.interpolate(method='idpp')
BFGS(neb).run(fmax=0.05)

energies = [img.get_potential_energy() for img in images]
barrier = max(energies) - energies[0]
print(f"Energy barrier (fcc -> hcp): {barrier:.4f} eV")
