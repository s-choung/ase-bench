from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT
from ase.neb import NEB
from ase.optimize import BFGS
from ase.constraints import FixAtoms

slab = fcc111('Cu', size=(3, 3, 4), vacuum=10.0)
mask = [tag >= 3 for tag in slab.get_tags()]

def relax_state(site):
    atoms = slab.copy()
    add_adsorbate(atoms, 'Cu', 1.8, site)
    atoms.set_constraint(FixAtoms(mask=mask + [False]))
    atoms.calc = EMT()
    BFGS(atoms, logfile=None).run(fmax=0.05)
    return atoms

initial = relax_state('fcc')
final = relax_state('hcp')

images = [initial] + [initial.copy() for _ in range(5)] + [final]
for img in images:
    img.calc = EMT()

neb = NEB(images)
neb.interpolate(method='idpp')
BFGS(neb, logfile=None).run(fmax=0.05)

energies = [img.get_potential_energy() for img in images]
print(f"Energy barrier: {max(energies) - energies[0]:.4f} eV")
