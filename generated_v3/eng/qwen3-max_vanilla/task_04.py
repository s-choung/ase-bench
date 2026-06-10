from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS

# Create H2O molecule
water = Atoms('H2O', positions=[[0.0, 0.0, 0.0],
                                [0.95, 0.0, 0.0],
                                [0.0, 0.95, 0.0]])

# Set EMT calculator
water.calc = EMT()

# Print initial energy
initial_energy = water.get_potential_energy()
print(f"Initial energy: {initial_energy:.6f} eV")

# Optimize geometry
opt = BFGS(water)
opt.run(fmax=0.05)

# Print final energy
final_energy = water.get_potential_energy()
print(f"Final energy: {final_energy:.6f} eV")
