import numpy as np
from ase import Atoms
from ase.calculators.emt import EMT
from ase.build import bulk
from ase.optimize import BFGS
from ase.eos import EquationOfState
from ase.visualize import view

# Bulk Ag optimization
elements = 'Ag'
lattice_constant = 3.6  # Å
a_range = 3.5 * 0.95 : 3.5 * 1.05
a_step = 0.01

atoms = bulk(elements, 'fcc', a=lattice_constant)
atoms.calc = EMT()

# Perform optimization
optimizer = BFGS(atoms)
optimizer.run(fmax=0.01)

# Print results
print(f"Equilibrium lattice constant: {atoms.get_cell()[0][0]} Å")
print(f"Bulk modulus: {EquationOfState(atoms.get_volume(), atoms.get_potential_energy(), eos='birchmurnaghan').fit()[2]} GPa")

# Visualizing the optimized structure
view(atoms)
