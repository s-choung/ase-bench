from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.mep import NEB
from ase.constraints import FixAtoms

def make_slab(site):
    slab = fcc111('Cu', size=(3, 3, 3), vacuum=10.0)
    add_adsorbate(slab, 'Cu', 2.0, site)
    slab.set_constraint(FixAtoms(mask=[a.tag >= 2 for a in slab]))
    slab.calc = EMT()
    return slab

initial = make_slab('fcc')
BFGS(initial, logfile=None).run(fmax=0.02)

final = make_slab('hcp')
BFGS(final, logfile=None).run(fmax=0.02)

images = [initial] + [initial.copy() for _ in range(3)] + [final]
for img in images[1:4]:
    img.calc = EMT()

neb = NEB(images, climb=True)
neb.interpolate(method='idpp')
BFGS(neb, logfile=None).run(fmax=0.05)

energies = [img.get_potential_energy() for img in images]
barrier = max(energies) - energies[0]
print(f"Energy barrier: {barrier:.4f} eV")
