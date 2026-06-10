from ase import Atoms
from ase.calculators import EMT
from ase.optimize import BFGS

# Define the water molecule
water = Atoms("O H H",
              positions=[[0.0, 0.0, 0.0],
                        [0.757, 0.586, 0.0],
                        [-0.757, 0.586, 0.0]],
              cell=[10, 10, 10],
              pbc=True)

# Initialize the EMT calculator
water.calc = EMT()

# Perform energy calculation before optimization
initial_energy = water.get_potential_energy()
print(f"Initial energy: {initial_energy:.6f} Hartree")

# Perform geometry optimization using BFGS
BFGS(water).run()

# Perform energy calculation after optimization
final_energy = water.get_potential_energy()
print(f"Final energy: {final_energy:.6f} Hartree")
