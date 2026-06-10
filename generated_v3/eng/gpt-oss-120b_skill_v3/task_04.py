from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS

# Build H2O molecule and attach EMT calculator
atoms = molecule('H2O')
atoms.calc = EMT()

# Energy before optimization
e_initial = atoms.get_potential_energy()
print("Initial energy (eV):", e_initial)

# Optimize geometry
BFGS(atoms).run(fmax=0.01)

# Energy after optimization
e_final = atoms.get_potential_energy()
print("Final energy (eV):", e_final)
