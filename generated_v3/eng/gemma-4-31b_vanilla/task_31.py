import numpy as np
from ase import Atoms
from ase.build import bulk
from ase.md.npt import NPTBerendsen
from ase.md.langevin import Langevin
from ase.calculators.emt import EMT
from ase.units import GPa

# Setup supercell and calculator
atoms = bulk('Al', 'fcc', a=4.05)
atoms = atoms * (2, 2, 2)
atoms.calc = EMT()

# Pressure conversion: 10 GPa to eV/Ang^3
target_pressure = 10 * GPa

# MD setup
# Temperature: 500K, Pressure: 10GPa
# NPTBerendsen requires a thermostat (Langevin)
dyn = Langevin(atoms, temperature_K=500, timestep=2.0 * 1e-15, friction=0.01)
npt = NPTBerendsen(atoms, 
                   temperature_K=500, 
                   pressure_Pa=target_pressure, 
                   tau_p=100 * 2.0 * 1e-15, 
                   tau_t=100 * 2.0 * 1e-15)

print(f"Initial Volume: {atoms.get_volume():.3f} A^3")

# Run MD
npt.run(100)

print(f"Final Volume: {atoms.get_volume():.3f} A^3")
