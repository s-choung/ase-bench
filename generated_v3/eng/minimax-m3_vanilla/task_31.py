from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
import numpy as np

# Convert GPa to eV/Ang^3
pressure_GPa = 10.0
pressure_au = pressure_GPa * units.GPa / (units.eV / units.Ang**3)

# Build Al FCC 2x2x2 supercell
atoms = bulk('Al', 'fcc', a=4.05) * (2, 2, 2)
atoms.calc = EMT()

# Initial volume
v0 = atoms.get_volume()
print(f"Initial volume: {v0:.4f} Ang^3")

# Set up NPT dynamics
MaxwellBoltzmannDistribution(atoms, temperature_K=500)
dyn = NPTBerendsen(atoms, timestep=1.0 * units.fs,
                   temperature=500, pressure_au=pressure_au,
                   taut=100 * units.fs, taup=1000 * units.fs)

dyn.run(100)

# Final volume
v1 = atoms.get_volume()
print(f"Final volume:   {v1:.4f} Ang^3")
