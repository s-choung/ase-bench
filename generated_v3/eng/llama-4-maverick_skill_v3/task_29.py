from ase import Atoms, units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

atoms = bulk('Pd', 'fcc', a=3.9) * (2, 2, 2)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=500)
Stationary(atoms)

dyn = VelocityVerlet(atoms, timestep=2 * units.fs)
E_init = atoms.get_potential_energy() + atoms.get_kinetic_energy()

for i in range(200):
    dyn.run(1)
    print(f'Step {i+1}, T = {atoms.get_temperature():.2f} K')

E_final = atoms.get_potential_energy() + atoms.get_kinetic_energy()
print(f'Energy difference: {E_final - E_init:.6f} eV')
