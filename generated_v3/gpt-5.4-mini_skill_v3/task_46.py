from ase.build import fcc111, molecule, add_adsorbate
from ase.constraints import FixAtoms, FixBondLength
from ase.calculators.emt import EMT
from ase.optimize import BFGS

slab = fcc111('Pt', size=(2, 2, 3), vacuum=10.0)
co = molecule('CO')
add_adsorbate(slab, co, height=1.8, position='ontop')

slab.set_constraint([
    FixAtoms(mask=[atom.tag == 1 for atom in slab]),
    FixBondLength(len(slab) - 2, len(slab) - 1),
])

slab.calc = EMT()
BFGS(slab).run(fmax=0.05)

e = slab.get_potential_energy()
d = slab.get_distance(len(slab) - 2, len(slab) - 1)

print(e)
print(d)
