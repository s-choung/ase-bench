from ase import Atoms
from ase.build import fcc111
from ase.constraints import FixAtoms, FixBondLength
from ase.optimize import BFGS
from ase.calculators.emt import EMT

slab = fcc111('Pt', size=(3, 3, 3), vacuum=10.0)
co = Atoms('CO', positions=[[0, 0, 3.0], [0, 0, 4.128]])
atoms = slab + co

atoms.set_constraint([
    FixAtoms(mask=[i < 9 for i in range(len(slab))] + [False]*2),
    FixBondLength(len(slab), len(slab)+1, 1.128)
])

atoms.set_calculator(EMT())
dyn = BFGS(atoms)
dyn.run(fmax=0.05)

print("Final energy:", atoms.get_potential_energy())
print("C-O distance:", atoms.get_distance(len(slab), len(slab)+1))
