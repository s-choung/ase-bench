from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.neb import NEB

slab = fcc111('Cu', size=(3, 3, 3), a=3.615)
add_adsorbate(slab, 'Cu', 1, 'fcc')
slab_final = fcc111('Cu', size=(3, 3, 3), a=3.615)
add_adsorbate(slab_final, 'Cu', 1, 'hcp')

images = [slab, slab_final]
neb = NEB(images)
neb.interpolate(nimages=3, method='idpp')

for img in images:
    img.set_calculator(EMT())

dyn = BFGS(images)
dyn.run(fmax=0.05)

energies = [img.get_potential_energy() for img in images]
barrier = max(energies) - energies[0]
print(f"Energy barrier: {barrier:.3f} eV")
