from ase import Atoms
from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms, FixBondLength
from ase.optimize import BFGS

slab = fcc111('Pt', size=(3, 3, 3), vacuum=10.0)

n_slab = len(slab)
co = Atoms('CO', positions=[(0, 0, 0), (0, 0, 1.15)])
add_adsorbate(slab, co, height=1.85, position='ontop', mol_index=0)

bottom_z = min(atom.position[2] for atom in slab if atom.symbol == 'Pt')
fix_bottom = FixAtoms(mask=[atom.symbol == 'Pt' and abs(atom.position[2] - bottom_z) < 0.1 for atom in slab])
fix_co = FixBondLength(n_slab, n_slab + 1)

slab.set_constraint([fix_bottom, fix_co])
slab.calc = EMT()

opt = BFGS(slab)
opt.run(fmax=0.05)

print("Final energy:", slab.get_potential_energy())
print("C-O distance:", slab.get_distance(n_slab, n_slab + 1))
