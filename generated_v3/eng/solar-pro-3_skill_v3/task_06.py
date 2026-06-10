from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.optimize import BFGS
from ase.filters import FrechetCellFilter
import numpy as np
from ase.thermodynamics import pressure

# Cu bulk fcc, 2x2x2 supercell
atoms = bulk('Cu', 'fcc', a=3.6, cubic=True)
atoms *= (2, 2, 2)          # supercell = a*a (size=(2,2,2))
atoms.calc = EMT()

# Langevin thermostat (NVT, 300 K)
atoms.set_calculator(atoms.calc)
LJ = Langevin(atoms,
              timestep=5 * np.fs,
              temperature_K=300,
              friction=0.01 / np.fs)

# Initial thermodynamic info
T0 = atoms.get_temperature()
E0 = atoms.get_potential_energy()
P0 = pressure(atoms)

print(f'Initial: T={T0:.1f} K, E={E0:.2f} eV, P={P0:.2f} bar')

# 100 MD steps
LJ.run(100)

# Final thermodynamic info
T1 = atoms.get_temperature()
E1 = atoms.get_potential_energy()

print(f'Final:   T={T1:.1f} K, E={E1:.2f} eV, P={pressure(atoms):.2f} bar')
