from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.md.velocity import MaxwellBoltzmannDistribution
from ase.units import fs

# Create Cu FCC 2x2x2 supercell
atoms = bulk('Cu', 'fcc', a=3.615) * (2, 2, 2)
atoms.calc = EMT()

# Initialize velocities at 300 K
MaxwellBoltzmannDistribution(atoms, temperature_K=300)

# Set up Langevin dynamics
timestep = 5 * fs
dyn = Langevin(atoms, timestep=timestep, temperature=300)  # initial temperature

steps = 200
for i in range(steps):
    # Linear temperature ramp from 300 K to 600 K
    target_T = 300 + (i / steps) * (600 - 300)
    dyn.temperature = target_T
    dyn.step()
    if (i + 1) % 50 == 0:
        T = atoms.get_temperature()
        print(f'Step {i+1}: T = {T:.2f} K')
