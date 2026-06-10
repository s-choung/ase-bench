from ase import Atoms
from ase.calculators.emt import EMT
from ase.md import Langevin
from ase.units import fs, kB
from ase.build import bulk

cu = bulk('Cu', 'fcc', a=3.6, cubic=True).repeat(2)
cu.calc = EMT()

dyn = Langevin(cu, 5*fs, temperature_K=300, friction=0.02)
dyn.run(100)

print(f"Initial temperature: {dyn.get_temperature():.2f} K")
print(f"Initial energy: {cu.get_potential_energy():.3f} eV")
print(f"Final temperature: {dyn.get_temperature():.2f} K")
print(f"Final energy: {cu.get_potential_energy():.3f} eV")
