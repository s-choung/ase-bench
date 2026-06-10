from ase.build import graphene_nanoribbon
from ase.calculators.lj import LennardJones
from ase.optimize import BFGS
import numpy as np

atoms = graphene_nanoribbon(5, 10, type="zigzag", saturated=False, vacuum=5.0)

pos = atoms.positions.copy()
cell = atoms.cell.array.copy()

atoms.positions = pos[:, [2, 0, 1]]
atoms.cell = cell[[2, 0, 1]][:, [2, 0, 1]]
atoms.pbc = (True, False, False)

atoms.calc = LennardJones()

opt = BFGS(atoms, logfile=None)
opt.run(fmax=0.01)

print("Final energy:", atoms.get_potential_energy())
print("Cell:")
print(atoms.cell)
