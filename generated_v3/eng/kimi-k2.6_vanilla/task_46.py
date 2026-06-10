from ase.build import fcc111, add_adsorbate, molecule
from ase.calculators.lj import LennardJones
from ase.constraints import FixAtoms, FixBondLength
from ase.optimize import BFGS

slab = fcc111('Pt', size=(2, 2, 3), vacuum=10.0)
co = molecule('CO')
n = len(slab)
add_adsorbate(slab, co, height=1.8, position='ontop', mol_index=0)

slab.set_constraint([
    FixAtoms(mask=[a.tag == 3 for a in slab]),
    FixBondLength(n, n + 1)
])

slab.calc = LennardJones(sigma=2.0, epsilon=0.1)

BFGS(slab).run(fmax=0.05)

print(f'Energy: {slab.get_potential_energy():.3f} eV')
print(f'C-O distance: {slab.get_distance(n, n + 1):.3f} A')
