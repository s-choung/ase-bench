from ase import Atoms
from ase.calculators.emt import EMT
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.md.verlet import VelocityVerlet
import numpy as np

# Create Pd FCC 2x2x2 supercell
cell = [[0, 0.5, 0.5],
        [0.5, 0, 0.5],
        [0.5, 0.5, 0]]
atoms = Atoms('Pd8', scaled_positions=[(0, 0, 0), (0, 0.5, 0.5),
                                       (0.5, 0, 0.5), (0.5, 0.5, 0),
                                       (0.25, 0.25, 0.25), (0.25, 0.75, 0.75),
                                       (0.75, 0.25, 0.75), (0.75, 0.75, 0.25)],
              cell=cell, pbc=True)

atoms.set_calculator(EMT())

# Set Initial Temperature
MaxwellBoltzmannDistribution(atoms, 500 * np.ones(3))

# Run Velocity Verlet NVE MD
dyn = VelocityVerlet(atoms, 2 * 1E-15)  # 2 fs timestep
for i in range(200):
    dyn.run(1)

# Calculate total energy
energy_start = atoms.get_total_energy()

# Print the difference in total energy
print(atoms.get_total_energy() - energy_start)
