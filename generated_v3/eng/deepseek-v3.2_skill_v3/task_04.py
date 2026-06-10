from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
import numpy as np

atoms = Atoms('OH2', positions=[[0, 0, 0], [0.95, 0, 0], [0.95*np.cos(np.radians(104.5)), 0.95*np.sin(np.radians(104.5)), 0]])
atoms.calc = EMT()
initial_energy = atoms.get_potential_energy()
print(f'Initial energy: {initial_energy:.4f} eV')

opt = BFGS(atoms, trajectory='h2o_opt.traj')
opt.run(fmax=0.05)

final_energy = atoms.get_potential_energy()
print(f'Final energy: {final_energy:.4f} eV')
print(f'Energy change: {final_energy - initial_energy:.4f} eV')
