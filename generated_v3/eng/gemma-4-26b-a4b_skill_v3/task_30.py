import numpy as np
from ase import units
from ase.build import bulk
from ase.md.nptberendsen import NPTBerendsen
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase.calculators.emt import EMT
from ase.filters import UnitCellFilter
from ase.optimize import BFGS

# Setup Cu supercell
atoms = bulk('Cu', 'fcc', a=3.6)
atoms = atoms.repeat((3, 3, 3))
atoms.calc = EMT()

# Initial relaxation of positions and cell (to avoid immediate explosion)
BFGS(UnitCellFilter(atoms)).run(fmax=0.05)

# MD Setup
# Note: NPTBerendsen requires a thermostat/barostat approach. 
# For NPTBerendsen, we initialize velocities first.
MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

# NPT parameters
dt = 5 * units.fs
taut = 100 * units.fs
taup = 1000 * units.fs
target_p = 1.01325e5  # 1 bar in Pascals

dyn = NPTBerendsen(atoms, timestep=dt, temperature_K=300, 
                   taut=taut, pressure=target_p, taup=taup)

# Data logging
v_init = atoms.get_volume()
p_init = atoms.get_pressure()

# Run MD
dyn.run(200)

v_final = atoms.get_volume()
p_final = atoms.get_pressure()

print(f"Initial Volume: {v_init:.2f} A^3, Pressure: {p_init:.2f} bar")
print(f"Final Volume:   {v_final:.2f} A^3, Pressure: {p_final:.2f} bar")
