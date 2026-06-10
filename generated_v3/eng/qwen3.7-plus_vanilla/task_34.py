from ase.build import fcc111, add_adsorbate
from ase.constraints import FixAtoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.neb import NEB
from ase.mep.idpp import idpp_interpolate

slab1 = fcc111('Cu', (3, 3), 3, vacuum=10.0)
add_adsorbate(slab1, 'Cu', 2.0, 'fcc')

slab2 = fcc111('Cu', (3, 3), 3, vacuum=10.0)
add_adsorbate(slab2, 'Cu', 2.0, 'hcp')

images = [slab1] + [slab1.copy() for _ in range(3)] + [slab2]

for img in images:
    img.set_calculator(EMT())
    mask = [i < len(img) - 1 for i in range(len(img))]
    img.set_constraint(FixAtoms(mask=mask))

idpp_interpolate(images, max_steps=50)

neb = NEB(images, climb=True)
opt = BFGS(neb)
opt.run(fmax=0.05)

energies = [img.get_potential_energy() for img in images]
print(f"Energy barrier: {max(energies) - energies[0]:.4f} eV")
