from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import LBFGS
import numpy as np

atoms = Atoms('Au', pbc=True)
atoms.set_cell([[3.9837, 0.0, 0.0],
                [0.0, 3.9837, 0.0],
                [0.0, 0.0, 3.9837]])
atoms.set_positions([[0.0, 0.0, 0.0],
                     [0.5, 0.5, 0.5],
                     [0.5, 0.0, 0.5],
                     [0.0, 0.5, 0.5]])

atoms.calc = EMT()

opt = LBFGS(atoms, fmax=0.01)
opt.run(maxforces=0.01)

print(f"Optimization steps: {opt.n_steps}")
print(f"Final energy: {atoms.get_potential_energy():.4f} eV")
