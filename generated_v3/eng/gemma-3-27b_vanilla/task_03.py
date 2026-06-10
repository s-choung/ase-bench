from ase.build import add_adsorbate
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.optimize import BFGS
from ase.io import write
import numpy as np

a = 3.16
cell = np.array([[a, 0, 0], [0, a * np.sqrt(3)/2, 0], [0, 0, 3.0]])
atoms = ase.build.monolayer('MoS2', size=(4, 4), cell=cell)

atoms.set_cell(cell + np.array([[0, 0, 10], [0, 0, 10], [0, 0, 10]]))

print(atoms.cell)

calc = EMT()
atoms.set_calculator(calc)

constraint = FixAtoms(mask=[atom.index for atom in atoms if atom.position[2] < 1])
atoms.set_constraint(constraint)

dyn = BFGS(atoms, trajectory='MoS2.traj')
dyn.run(fmax=0.02)

write('MoS2.xyz', atoms)
