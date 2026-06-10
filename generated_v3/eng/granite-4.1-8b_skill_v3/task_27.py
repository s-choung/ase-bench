from ase import Atoms
from ase.build import bulk
from ase.calculators.eam import EAM
from ase.md.bussi import Bussi
from ase.optimize import BFGS
from ase import units
import numpy as np

# Create bulk Ag FCC structure
ag = bulk('Ag', 'fcc', a=4.09)

# Build 2x2x2 supercell
supercell = ag.repeat(2)

# Set up EAM calculator for Ag
supercell.calc = EAM(database='eam/alloy.eam')  # Ensure the correct EAM potential file is available

# Relax the supercell to get an initial equilibrium structure
relaxer = BFGS(supercell)
relaxer.run(fmax=0.0001)
supercell.calc = EAM(database='eam/alloy.eam')  # Reset calculator for MD

# Apply Bussi thermostat for NVT MD
md = Bussi(supercell, timestep=5 * units.fs, temperature_K=500, friction=0.1 / units.fs)
md.attach(lambda atoms, step: print(f'Step {step:4d}  Temp = {atoms.get_temperature():6.2f} K'),
          print_interval=50)

# Perform MD for 200 steps
md.run(steps=200)
