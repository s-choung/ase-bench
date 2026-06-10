from ase import units
from ase.build import bulk
from ase.atoms import Atoms
from ase.md.langevin import Langevin
from ase.calculators.emt import EMT
import numpy as np

# Create FCC Cu supercell
atoms: Atoms = bulk('Cu', 'fcc', a=3.6, cubic=True)
atoms = atoms.repeat((2, 2, 2))
atoms.calc = EMT()

# Initialize velocities at 300K
temp_initial = 300.0
atoms.set_velocities(np.random.RandomState(42).standard_normal(
    (len(atoms), 3)) * np.sqrt(units.kB * temp_initial / atoms.get_masses()[0]))

# Set up Langevin dynamics
dyn = Langevin(atoms, 5 * units.fs, units.kB * temp_initial, 0.002)

# Run temperature ramp (300->600K over 200 steps)
temp_final = 600.0
for step in range(200):
    dyn.temperature = units.kB * (temp_initial + 
        (temp_final - temp_initial) * step / 199)  # Linear ramp
    dyn.run(1)
    
    if step % 50 == 0:  # Print every 50 steps including step0
        print(f'Step {step+1}: T = {atoms.get_temperature():.1f} K')
