from ase.build import fcc_111
from ase.md.bussi import Bussi
from ase.calculators.emt import EMT
from ase.md.velocity import Velocity
import numpy as np

atoms = fcc_111('Ag', size=2)
calc = EMT()
atoms.set_calculator(calc)

dt = 5.0
temp = 300.0
gamma = 1.0
bussi = Bussi(temp, gamma, dt)
md = Velocity(atoms, dt, bussi)

md.run(500000)

for i in range(0, 500000, 50):
    md.update_timestep(dt)
    print(f"Step {i}: Temperature = {atoms.get_temp():.2f} K")
