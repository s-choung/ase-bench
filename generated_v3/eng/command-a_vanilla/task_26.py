from ase.build import bulk
from ase.optimize import BFGS
from ase.calculators.emt import EMT
from ase.constraints import StrainFilter

# Create Ni FCC bulk
atoms = bulk('Ni', 'fcc', a=3.52)

# Apply EMT calculator
atoms.calc = EMT()

# Apply strain filter and optimizer
strain_filter = StrainFilter(atoms)
opt = BFGS(strain_filter, trajectory=None, precon='auto')

# Optimize
opt.run(fmax=0.01)

# Output results
print(f"Number of steps: {opt.get_number_of_steps()}")
print(f"Final energy: {atoms.get_potential_energy():.6f} eV")
print(f"Final cell parameters: {atoms.cell.cellpar()}")
