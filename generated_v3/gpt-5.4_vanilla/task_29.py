from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase import units

atoms = bulk('Pd', 'fcc', cubic=True) * (2, 2, 2)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=500)

epot0 = atoms.get_potential_energy()
ekin0 = atoms.get_kinetic_energy()
etot0 = epot0 + ekin0

dyn = VelocityVerlet(atoms, timestep=2 * units.fs)
dyn.run(200)

epot1 = atoms.get_potential_energy()
ekin1 = atoms.get_kinetic_energy()
etot1 = epot1 + ekin1

print(f"Initial total energy: {etot0:.10f} eV")
print(f"Final total energy:   {etot1:.10f} eV")
print(f"Delta E:              {etot1 - etot0:.10e} eV")
