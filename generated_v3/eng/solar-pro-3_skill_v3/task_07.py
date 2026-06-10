import numpy as np
from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import BFGS, FrechetCellFilter
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.md import MDMin

# 1. build Cu FCC bulk and set calculator
cells = bulk('Cu', 'fcc', a=3.6)
cells.calc = EMT()

# 2. minimize and get well‑defined stress state
BFGS(FrechetCellFilter(cells), trajectory='min.traj').run(fmax=0.02)

# 3. give atoms zero mean velocity
from ase.constraints import FixCom
cells.set_constraint(FixCom(mask=[i for i in range(len(cells))]))

# 4. sprinkle velocities → 300 K
MaxwellBoltzmannDistribution(cells, temperature_K=300)

# 5. NVE run
md = VelocityVerlet(cells, timestep=5 * units.fs)   # natural unit step ≈ 2.67 fs
for step in range(1, 51):
    md.run(steps=1)
    e_pot = cells.get_potential_energy()
    e_kin = cells.get_kinetic_energy()
    print(f'Step {step:3d}:  E_tot = {e_pot + e_kin:8.3f} eV  ΔE = {(e_pot + e_kin) - (e_pot + e_kin - e_pot - e_kin):8.3f} eV')
