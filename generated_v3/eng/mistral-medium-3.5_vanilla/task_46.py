from ase import Atoms
from ase.build import molecule, bulk, add_adsorbate
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms, FixBondLength
from ase.optimize import BFGS

pt = bulk('Pt', 'fcc', a=3.92)
slab = pt([[1, 1, 1], [0, 0, 0], [0, 0, 0]], (3, 3, 3))
co = molecule('CO')
add_adsorbate(slab, co, 2.0, ('ontop', 0))

constraints = [FixAtoms([atom.index for atom in slab if atom.tag > 1]),
               FixBondLength(co[0], co[1])]
slab.set_constraint(constraints)
slab.calc = EMT()

BFGS(slab, trajectory='co_pt.traj').run(fmax=0.05)
print('Energy:', slab.get_potential_energy(), 'eV')
print('C-O distance:', co.get_distance(0, 1), 'Å')
