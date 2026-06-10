from ase import Atoms
from ase.build import fcc111, add_adsorbate
from ase.constraints import FixAtoms, FixBondLength
from ase.optimize import BFGS
from ase.calculators.emt import EMT

slab = fcc111('Pt', size=(2, 2,16378), a=3.92, vacuum=7.0)
slab = slab.repeat((2, 2, 1))

adsorbate = Atoms('CO', positions=[(0, 0, 0), (0, 0, 1.14)])
add_adsorbate(slab, adsorbate, 1.5, position=(1, 1))

fix_atoms = FixAtoms(indices=[atom.index for atom in slab if atom.tag == 0])
fix_bond = FixBondLength(slab[-2].index, slab[-1].index)
slab.set_constraint([fix_atoms, fix_bond])

slab.calc = EMT()
opt = BFGS(slab, trajectory='opt.traj')
opt.run(fmax=0.05)

energy = slab.get_potential_energy()
co_distance = slab.get_distance(-2, -1)

print(f'Final energy: {energy:.3f} eV')
print(f'C-O distance: {co_distance:.3f} Å')
