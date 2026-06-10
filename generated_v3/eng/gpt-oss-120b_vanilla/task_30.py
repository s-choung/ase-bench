#!/usr/bin/env python3
# NPT MD of Cu FCC 3×3×3 supercell using EMT + NPTBerendsen

from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase import units
import numpy as np

# ----- build system -------------------------------------------------
atoms = bulk('Cu', 'fcc', a=3.6) * (3, 3, 3)   # 3×3×3 supercell
atoms.set_calculator(EMT())

# ----- initial state ------------------------------------------------
V0 = atoms.get_volume()                     # Å³
P0 = atoms.get_pressure() * 1e3            # bar (get_pressure() → kbar)
print(f'Initial volume = {V0:.2f} Å³, pressure = {P0:.2f} bar')

# ----- NPT dynamics ------------------------------------------------
timestep = 5 * units.fs
taut = 100 * units.fs          # temperature coupling time
taup = 1000 * units.fs         # pressure coupling time
external_pressure = 1e-4 * units.GPa   # 1 bar in GPa

dyn = NPTBerendsen(atoms,
                   timestep,
                   temperature_K=300,
                   externalstress=external_pressure,
                   ttime=taut,
                   pfactor=taup)

dyn.run(200)   # 200 steps

# ----- final state --------------------------------------------------
Vf = atoms.get_volume()
Pf = atoms.get_pressure() * 1e3   # bar
print(f'Final volume   = {Vf:.2f} Å³, pressure = {Pf:.2f} bar')
