import numpy as np
from ase import Atoms
from ase.build import bulk
from ase.md.velocityverlet import VelocityVerlet
from ase.md.temperatureaccelerator import MaxwellBoltzmannDistribution
from ase.calculators.emt import EMT
from ase import units

# Setup Pd FCC supercell
atoms = bulk('Pd', 'fcc', a=3.89) * (2, 2, 2)
atoms.calc = EMT()

# Initial temperature 500K
MaxwellBoltzmannDistribution(atoms, temperature_K=500)

# MD Parameters
timestep = 2.0 * units.fs
dyn = VelocityVerlet(atoms, timestep=timestep)

# Initial energy
e_start = atoms.get_total_energy() + atoms.get_kinetic_energy()

# Run 200 steps
dyn.run(200)

# Final energy
e_end = atoms.get_total_energy() + atoms.get_kinetic_energy()

print(f"Energy Difference: {abs(e_end - e_start):.6f} eV")
