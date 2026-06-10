from ase import Atom
from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.mep import NEB
from ase.constraints import FixAtoms

# Initial: Cu adatom at fcc hollow
slab0 = fcc111('Cu', size=(3, 3, 4), vacuum=10.0)
slab0.set_constraint(FixAtoms(mask=[a.tag < 2 for a in slab0]))
add_adsorbate(slab0, Atom('Cu'), height=1.8, position='fcc')

# Final: Cu adatom at hcp hollow
slab1 = fcc111('Cu', size=(3, 3, 4), vacuum=10.0)
slab1.set_constraint(FixAtoms(mask=[a.tag < 2 for a in slab1]))
add_adsorbate(slab1, Atom('Cu'), height=1.8, position='hcp')

# 5 total images: initial + 3 intermediates + final
images = [slab0] + [slab0.copy() for _ in range(3)] + [slab1]
for img in images:
    img.calc = EMT()

neb = NEB(images)
neb.interpolate(method='idpp')
BFGS(neb).run(fmax=0.05)

energies = [img.get_potential_energy() for img in images]
print(f"Energy barrier: {max(energies) - energies[0]:.4f} eV")
