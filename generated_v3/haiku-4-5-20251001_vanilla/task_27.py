from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nvtberendsen import NVTBerendsen
from ase.io import write
import numpy as np

atoms = bulk('Ag', 'fcc', a=4.085, cubic=True)
atoms = atoms.repeat((2, 2, 2))
atoms.calc = EMT()

dyn = NVTBerendsen(atoms, timestep=5, temperature_K=500, friction=0.002)

temperatures = []
for i in range(200):
    dyn.run(1)
    if (i + 1) % 50 == 0:
        temp = atoms.get_kinetic_energy() / (1.5 * len(atoms) * 8.617333262e-5)
        temperatures.append(temp)
        print(f"Step {i + 1}: Temperature = {temp:.2f} K")

write('trajectory.traj', atoms)
