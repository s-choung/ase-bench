from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT
from ase.neb import NEB
from ase.optimize import BFGS

slab = fcc111('Cu', size=(2, 2, 4), vacuum=10.0)
slab.calc = EMT()

# Initial: Cu adatom on fcc hollow site
initial = slab.copy()
add_adsorbate(initial, 'Cu', height=2.0, position='hollow')

# Final: Cu adatom shifted to approximate hcp hollow site
final = slab.copy()
adatom_pos = initial[-1].position
final.append(Atoms('Cu', positions=[[adatom_pos[0] + 0.5, adatom_pos[1], adatom_pos[2]]]))

images = [initial] + [initial.copy() for _ in range(5)] + [final]
neb = NEB(images)
neb.interpolate(method='idpp')

for img in images[1:-1]:
    img.calc = EMT()

BFGS(neb).run(fmax=0.05)

energies = [img.get_potential_energy() for img in images]
print(f"Energy barrier: {max(energies) - energies[0]} eV")
