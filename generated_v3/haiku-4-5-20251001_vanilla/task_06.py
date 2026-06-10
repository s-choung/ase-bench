from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.units import kB
import numpy as np

atoms = bulk('Cu', 'fcc', a=3.61, cubic=True)
atoms = atoms.repeat((2, 2, 2))

atoms.calc = EMT()

md = Langevin(atoms, timestep=5, temperature_K=300, friction=0.002)

initial_temp = atoms.get_kinetic_energy() / (1.5 * len(atoms) * kB)
initial_energy = atoms.get_total_energy()

print(f"Initial Temperature: {initial_temp:.2f} K")
print(f"Initial Energy: {initial_energy:.4f} eV")

for i in range(100):
    md.run(1)

final_temp = atoms.get_kinetic_energy() / (1.5 * len(atoms) * kB)
final_energy = atoms.get_total_energy()

print(f"Final Temperature: {final_temp:.2f} K")
print(f"Final Energy: {final_energy:.4f} eV")
