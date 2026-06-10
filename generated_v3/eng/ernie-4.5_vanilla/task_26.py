from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize.precon import PreconLBFGS

# Create FCC Ni bulk structure
atoms = bulk('Ni', 'fcc', a=3.52, cubic=True)

# Use EMT calculator with automatic preconditioner
atoms.calc = EMT(precon='auto')  

# Optimizer setup with convergence criterion fmax=0.01
optimizer = PreconLBFGS(atoms, trajectory=None)  # No trajectory file
optimizer.run(fmax=0.01)

# Output results
print(f"Number of steps: {optimizer.get_number_of_steps()}")
print(f"Final energy (eV): {atoms.get_potential_energy():.4f}")
print(f"Final cell parameters (Å): {atoms.cell.cellpar()[0:3]}")  # a, b, c
