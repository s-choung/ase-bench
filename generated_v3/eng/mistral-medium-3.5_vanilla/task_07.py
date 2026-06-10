from ase import Atoms
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase import units
from ase.md import MDLogger

cu = Atoms('Cu', cell=(3.6, 3.6, 3.6), pbc=True)
cu.calc = EMT()
cu.set_momenta(MDLogger.get_temperatures([300], [cu], time_const=100 * units.fs))

dyn = VelocityVerlet(cu, timestep=1 * units.fs)
print(f'Initial energy: {cu.get_potential_energy() + cu.get_kinetic_energy():.6f} eV')

dyn.run(50)
print(f'Final energy: {cu.get_potential_energy() + cu.get_kinetic_energy():.6f} eV')
