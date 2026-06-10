from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase import units
import numpy as np

# Create Al FCC 2x2x2 supercell
atoms = bulk('Al', 'fcc', a=4.05).repeat((2, 2, 2))
atoms.calc = EMT()

# Initialize velocities at 500K
MaxwellBoltzmannDistribution(atoms, temperature_K=500)
Stationary(atoms)

# Convert pressure: 10 GPa to eV/Ang^3
pressure_GPa = 10.0
pressure_evAng3 = pressure_GPa * 6.241509074e-3  # 1 GPa = 6.2415e-3 eV/Ang^3

# Set up NPT Berendsen MD
dyn = NPTBerendsen(atoms, 
                   timestep=5*units.fs, 
                   temperature_K=500, 
                   pressure=pressure_evAng3,
                   taut=0.5*units.fs, 
                   taup=1.0*units.fs)

# Print initial volume
print(f"Initial volume: {atoms.get_volume():.3f} Ang^3")

# Run MD for 100 steps
dyn.run(100)

# Print final volume
print(f"Final volume: {atoms.get_volume():.3f} Ang^3")
