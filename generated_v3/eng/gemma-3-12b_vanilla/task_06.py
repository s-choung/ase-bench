from ase.build import fcc
from ase.md.langevin import Langevin
from ase.calculators.emt import EMT
import numpy as np

atoms = fcc('Cu', size=(2, 2, 2))
calc = EMT()
atoms.calc = calc

md = Langevin(1.5, timestep=5)
atoms.get_potential_energy()

for i in range(100):
    atoms.run(md, 1)

print(f"Initial Temperature: {md.temperature}")
print(f"Final Temperature: {md.temperature}")
print(f"Final Energy: {atoms.get_potential_energy()}")
