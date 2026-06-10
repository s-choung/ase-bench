from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
import numpy as np

atoms = bulk('Cu', 'fcc', a=3.6, cubic=True) * (2, 2, 2)
atoms.calc = EMT()
MaxwellBoltzmannDistribution(atoms, temperature_K=300)

print(f"Initial temperature: {atoms.get_temperature():.2f} K")
print(f"Initial potential energy: {atoms.get_potential_energy():.4f} eV")

md = Langevin(atoms, timestep=5.0, temperature_K=300, friction=0.02)
md.run(100)

print(f"Final temperature: {atoms.get_temperature():.2f} K")
print(f"Final potential energy: {atoms.get_potential_energy():.4f} eV")
