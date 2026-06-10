from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS

# Initialize H2O molecule and assign EMT calculator
atoms = molecule('H2O')
atoms.calc = EMT()

# Calculate and print pre-optimization energy
initial_energy = atoms.get_potential_energy()
print(f"Energy before optimization: {initial_energy:.4f} eV")

# Run BFGS geometry optimization
opt = BFGS(atoms)
opt.run(fmax=0.05)

# Calculate and print post-optimization energy
final_energy = atoms.get_potential_energy()
print(f"Energy after optimization: {final_energy:.4f} eV")
