from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize.precon import PreconLBFGS

# Create Ni FCC bulk with initial lattice constant guess
atoms = bulk('Ni', 'fcc', a=3.52)

# Attach EMT calculator
atoms.calc = EMT()

# Set up optimizer with preconditioning
optimizer = PreconLBFGS(atoms, precon='auto')
optimizer.run(fmax=0.01)

# Print results
print(f"Number of steps: {optimizer.get_number_of_steps()}")
print(f"Final energy: {atoms.get_potential_energy():.6f} eV")
print(f"Cell parameters: {atoms.cell.cellpar()}")
