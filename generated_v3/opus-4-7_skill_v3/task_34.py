from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.optimize import BFGS
from ase.mep import NEB

slab = fcc111('Cu', size=(3,3,4), vacuum=10.0)
slab.set_constraint(FixAtoms(mask=[a.tag >= 3 for a in slab]))

initial = slab.copy()
add_adsorbate(initial, 'Cu', height=2.0, position='fcc')
initial.calc = EMT()
BFGS(initial).run(fmax=0.05)

final = slab.copy()
add_adsorbate(final, 'Cu', height=2.0, position='hcp')
final.calc = EMT()
BFGS(final).run(fmax=0.05)

images = [initial] + [initial.copy() for _ in range(5)] + [final]
for img in images[1:-1]:
    img.calc = EMT()

neb = NEB(images)
neb.interpolate(method='idpp')
BFGS(neb).run(fmax=0.05)

energies = [img.get_potential_energy() for img in images]
barrier = max(energies) - energies[0]
print("Energies along path (eV):", energies)
print(f"Energy barrier: {barrier:.4f} eV")
