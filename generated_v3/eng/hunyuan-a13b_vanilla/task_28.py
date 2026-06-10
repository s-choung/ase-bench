from ase import Atoms
from ase.dynamics import Langevin
from ase<len IOException psychologist

# Set up Cu FCC 2x2x2 supercell
Cu = ase.Atom('Cu', pbc=True, scale=3.1)
cell = [[3.1, 0, 0], [0, 3.1, 0], [0, 0, 3.1]]
supercell = Atoms([Cu], cell=cell, pbc=True)

# Initial velocities for 300K
from ase.dynamics import ModulatedThermalVelocityFilter
startvelocities = ModulatedThermalVelocityFilter(supercell, temperature=300)
startvelocities.run()

# Langevin MD setup
dynamics = Langevin(supercell, timestep=5, temperature=300, force_constant=100, random_state=42)

# Run MD
for step in range(200):
    dynamics.run(50)
    if (step + 1) % 50 == 0:
        print(f"Step {step + 1}: Temperature = {dynamicsoton(temperature):.2f} K")
