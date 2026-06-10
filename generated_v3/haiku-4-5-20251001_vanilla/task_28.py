from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.units import kB
import numpy as np

atoms = bulk('Cu', 'fcc', a=3.61, cubic=True)
atoms = atoms.repeat((2, 2, 2))
atoms.calc = EMT()

T_start = 300
T_end = 600
n_steps = 200
timestep = 5

md = Langevin(atoms, timestep=timestep, temperature_K=T_start, friction=0.002)

for step in range(n_steps):
    T_current = T_start + (T_end - T_start) * step / n_steps
    md.set_temperature(T_current)
    md.run(1)
    
    if (step + 1) % 50 == 0:
        print(f"Step {step + 1}: T = {T_current:.1f} K, E = {atoms.get_total_energy():.4f} eV")
