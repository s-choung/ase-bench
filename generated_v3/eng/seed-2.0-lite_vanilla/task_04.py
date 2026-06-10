from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS

# Initialize water molecule and attach EMT calculator
atoms = molecule('H2O')
atoms.calc = EMT()

# Print pre-optimization energy
initial_energy = atoms.get_potential_energy()
print(f"Energy before optimization: {initial_energy:.4f} eV")

# Run BFGS geometry optimization
optimizer = BFGS(atoms)
optimizer.run(fmax=0.01)  # Converge forces below 0.01 eV/Å

# Print post-optimization energy
final_energy = atoms.get_potential_energy()
print(f"Energy after optimization: {final_energy:.4f} eV")
