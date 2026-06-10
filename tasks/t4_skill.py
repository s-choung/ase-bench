"""T4 Skill: Relax H2O geometry with EMT"""
from ase import Atoms
from ase.optimize import BFGS
from ase.calculators.emt import EMT
import numpy as np

d = 0.9575
t = np.pi / 180 * 104.51
water = Atoms('H2O',
              positions=[(d, 0, 0),
                         (d * np.cos(t), d * np.sin(t), 0),
                         (0, 0, 0)])
water.calc = EMT()
dyn = BFGS(water)
dyn.run(fmax=0.05)
print(f"Energy: {water.get_potential_energy():.4f} eV")
