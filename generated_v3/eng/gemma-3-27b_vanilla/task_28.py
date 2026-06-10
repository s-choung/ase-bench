from ase.build import fcc111
from ase.md.langevin import Langevin
from ase.io import write
import numpy as np

atoms = fcc111('Cu', size=(2, 2, 2), vacuum=1.0)
atoms.set_cell([8.0, 8.0, 8.0], scale_axes=True)

dyn = Langevin(atoms, 300, 5, 0.005)
temp_list = []

for step in range(200):
    dyn.run(1)
    if (step + 1) % 50 == 0:
        temp = dyn.get_temperature()
        temp_list.append(temp)
        print(f"Step {step + 1}: Temperature = {temp:.2f} K")

    if step > 100:
        dyn.temperature = 300 + (600 - 300) * (step - 100) / 100

write('cu_md.traj', atoms)
