from ase.build import fcc111, molecule, add_adsorbate
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms, FixBondLength
from ase.optimize import BFGS

slab = fcc111('Pt', size=(2, 2, 3), vacuum=10.0)

bottom_idx = [i for i, a in enumerate(slab) if a.tag == 0]

co = molecule('CO')
add_adsorbate(slab, co, 1.8, position='ontop')

c_idx = len(slab) - 2
o_idx = len(slab) - 1

slab.set_constraint([FixAtoms(indices=bottom_idx),
                     FixBondLength(c_idx, o_idx)])

slab.calc = EMT()
BFGS(slab).run(fmax=0.05)

E = slab.get_potential_energy()
d = slab.get_distance(c_idx, o_idx, mic=True)

print(f'Energy = {E:.4f} eV')
print(f'C-O distance = {d:.4f} Ang')
