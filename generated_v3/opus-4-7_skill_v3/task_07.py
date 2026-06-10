from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase import units

atoms = bulk('Cu', 'fcc', a=3.6, cubic=True) * (3, 3, 3)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

e_init = atoms.get_potential_energy() + atoms.get_kinetic_energy()
print(f"Initial total energy: {e_init:.6f} eV")
print(f"Initial temperature: {atoms.get_temperature():.2f} K")

dyn = VelocityVerlet(atoms, timestep=1.0 * units.fs)
dyn.run(50)

e_final = atoms.get_potential_energy() + atoms.get_kinetic_energy()
print(f"Final total energy: {e_final:.6f} eV")
print(f"Final temperature: {atoms.get_temperature():.2f} K")
print(f"Energy drift: {e_final - e_init:.6e} eV")
