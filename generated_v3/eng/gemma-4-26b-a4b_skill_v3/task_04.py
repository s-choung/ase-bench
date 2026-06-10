from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS

# Initialize H2O molecule
atoms = molecule('H2O')
atoms.calc = EMT()

# Energy before optimization
energy_before = atoms.get_potential_energy()
print(f"Energy before: {energy_before:.6f} eV")

# Optimization using BFGS
opt = BFGS(atoms)
opt.run(fmax=0.05)

# Energy after optimization
energy_after = atoms.get_potential_energy()
print(f"Energy after: {energy_after:.6f} eV")
