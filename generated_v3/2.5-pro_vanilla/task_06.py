```python
import ase.units as units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution

atoms = bulk('Cu', 'fcc', a=3.6) * (2, 2, 2)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=300)

print(f"Initial Temperature: {atoms.get_temperature():.2f} K")
print(f"Initial Energy: {atoms.get_total_energy():.4f} eV")

dyn = Langevin(atoms, 
               timestep=5 * units.fs, 
               temperature_K=300,
