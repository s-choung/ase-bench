from ase.build import fcc111, add_adsorbate
from ase.constraints import FixAtoms, FixBondLength
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase import Atoms

slab = fcc111('Pt', size=(3, 3, 3), vacuum=10.0)
co = Atoms('CO', positions=[(0, 0, 0), (0, 0, 1.14)])
add_adsorbate(slab, co, height=2.0, position='ontop')

n = len(slab)
c_idx, o_idx = n - 2, n - 1

mask = [atom.tag == 3 for atom in slab]
fix_layer = FixAtoms(mask=mask)
fix_co = FixBondLength(c_idx, o_idx)
slab.set_constraint([fix_layer, fix_co])

slab.calc = EMT()
opt = BFGS(slab)
opt.run(fmax=0.05)

print('Final energy:', slab.get_potential_energy(), 'eV')
print('C-O distance:', slab.get_distance(c_idx, o_idx), 'Å')
