from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import PreconLBFGS
import numpy as np

atoms = bulk('Ni', 'fcc', a=3.52)
atoms.calc = EMT(precon='auto')

opt = PreconLBFGS(atoms, trajectory='Ni_EMT_opt.traj')
opt.run(fmax=0.01)

print(f"Number of steps: {opt.steps}")
print(f"Final energy: {atoms.get_potential_energy()}")
cell_lengths_angles = atoms.get_cell_lengths_and_angles()
print(f"Cell parameters: a={cell_lengths_angles[0]:.3f} Å, b={cell_lengths_angles[1]:.3f} Å, c={cell_lengths_angles[2]:.3f} Å, α={cell_lengths_angles[3]:.2f}°, β={cell_lengths_angles[4]:.2f}°, γ={cell_lengths_angles[5]:.2f}°")
