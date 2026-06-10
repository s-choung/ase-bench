from ase import Atoms
from ase.md.langevin import Langevin
from ase.calculators.emt import EMT
from ase.units import fs, kB

cu = Atoms('Cu', positions=[[0, 0, 0]], cell=[[3.6, 0, 0], [0, 3.6, 0], [0, 0, 3.6]], pbc=True)
cu *= (2, 2, 2)
cu.calc = EMT()

dyn = Langevin(cu, 5*fs, 300*kB, 0.002)
print(f'Initial T: {cu.get_temperature():.2f} K, E: {cu.get_potential_energy():.4f} eV')

dyn.run(100)

print(f'Final T: {cu.get_temperature():.2f} K, E: {cu.get_potential_energy():.4f} eV')
