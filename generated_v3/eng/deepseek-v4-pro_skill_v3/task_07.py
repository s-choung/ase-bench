from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary, ZeroRotation

atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)
ZeroRotation(atoms)

dyn = VelocityVerlet(atoms, timestep=1 * units.fs)

e_start = atoms.get_potential_energy() + atoms.get_kinetic_energy()
print(f"Initial total energy: {e_start:.6f} eV")

dyn.run(50)

e_end = atoms.get_potential_energy() + atoms.get_kinetic_energy()
print(f"Final total energy:   {e_end:.6f} eV")
print(f"Difference:           {e_end - e_start:.6e} eV")
