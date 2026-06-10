import numpy as np
from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

# Setup structure
atoms = bulk('Al', 'fcc', a=4.05)
atoms = atoms * (2, 2, 2)
atoms.calc = EMT()

# Initial conditions
MaxwellBoltzmannDistribution(atoms, temperature_K=500)
Stationary(atoms)

# Pressure conversion: 10 GPa to eV/Ang^3
target_pressure = 10 * units.GPa / (units.eV / units.Ang**3)

print(f"Initial Volume: {atoms.get_volume():.3f} A^3")

# NPT MD
md = NPTBerendsen(
    atoms, 
    timestep=2 * units.fs, 
    temperature_K=500, 
    pressure_kb=target_pressure, 
    tau_p=100 * units.fs, 
    tau_t=100 * units.fs
)
md.run(100)

print(f"Final Volume: {atoms.get_volume():.3f} A^3")
