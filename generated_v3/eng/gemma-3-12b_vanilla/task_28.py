from ase.build import fcc
from ase.md.langevin import Langevin
from ase.calculators.emt import EMT
from ase.units import fs

atoms = fcc('Cu', size=2)
calc = EMT()
atoms.calc = calc

dynamics = Langevin(1.0, 0.02, fs * 5)
atoms.get_potential_energy()

for step in range(200):
    atoms.run(dynamics, 1)
    if step % 50 == 0:
        print(f"Step {step}: Temperature = {atoms.get_temp():.2f} K")
