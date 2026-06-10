from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution

atoms = bulk('Cu', 'fcc', a=3.615, cubic=True)
atoms.calc = EMT()
MaxwellBoltzmannDistribution(atoms, temperature_K=300)

initial_energy = atoms.get_total_energy() + atoms.get_kinetic_energy()
dyn = VelocityVerlet(atoms, timestep=1.0 * units.fs)
dyn.run(50)
final_energy = atoms.get_total_energy() + atoms.get_kinetic_energy()

print("Initial total energy: {:.6f} eV".format(initial_energy))
print("Final total energy:   {:.6f} eV".format(final_energy))
