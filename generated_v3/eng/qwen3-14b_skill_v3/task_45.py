import numpy as np
from ase import Atoms
from ase.build import molecule
from ase.constraints import FixBondLength
from ase.calculators.emt import EMT
from ase.optimize import BFGS

h2 = molecule('H2')
h2.calc = EMT()

# Initial values
pos = h2.get_positions()
initial_length = np.linalg.norm(pos[0] - pos[1])
initial_energy = h2.get_potential_energy()

# Apply constraint
h2.set_constraint(FixBondLength(0, 1, 0.9))

# Optimize with constraint
opt = BFGS(h2)
opt.run(fmax=0.01)

# Final values
final_length = np.linalg.norm(h2.get_positions()[0] - h2.get_positions()[1])
final_energy = h2.get_potential_energy()

print(f"Initial length: {initial_length:.3f} Å, Energy: {initial_energy:.3f} eV")
print(f"Final length: {final_length:.3f} Å, Energy: {final_energy:.3f} eV")
