from ase import Atoms
from ase.constraints import UnitCellFilter
from ase.build import bulk
from ase.optimize import PreconLBFGS
from ase.calculators.emt import EMT

# Create Ni FCC bulk structure
atoms = bulk('Ni', crystalstructure='fcc', a=3.52, cubic=True)
atoms.set_calculator(EMT())

# Apply UnitCellFilter constraint for cell optimization
atoms.set_constraint(UnitCellFilter(atoms))

# Optimize using PreconLBFGS
opt = PreconLBFGS(atoms, precon='auto')
opt.run(fmax=0.01)

# Print results
print(f"Number of steps: {opt.get_number_of_steps()}")
print(f"Final energy: {atoms.get_potential_energy()} eV")
print(f"Final cell parameters: {atoms.get_cell_lengths_and_angles()} Angstrom, degrees")
