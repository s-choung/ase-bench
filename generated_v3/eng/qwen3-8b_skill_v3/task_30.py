from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
import ase.units as units

atoms = bulk('Cu', 'fcc', a=3.6).repeat((3, 3, 3))
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

dyn = NPTBerendsen(atoms, timestep=5*units.fs, temperature_K=300, pressure=1*units.bar, taut=100*units.fs, taup=1000*units.fs)
dyn.run(200)

print(f"Initial volume: {atoms.get_volume()} Å³")
print(f"Final volume: {atoms.get_volume()} Å³")
