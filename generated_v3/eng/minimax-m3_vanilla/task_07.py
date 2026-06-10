from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.md.verlet import VelocityVerlet

atoms = bulk("Cu", "fcc", a=3.6) * (3, 3, 3)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=300)

initial_energy = atoms.get_potential_energy() + atoms.get_kinetic_energy()
print(f"Initial total energy: {initial_energy:.6f} eV")

dyn = VelocityVerlet(atoms, timestep=1.0 * units.fs)
dyn.run(50)

final_energy = atoms.get_potential_energy() + atoms.get_kinetic_energy()
print(f"Final total energy:   {final_energy:.6f} eV")
print(f"Energy drift:         {final_energy - initial_energy:.6e} eV")
