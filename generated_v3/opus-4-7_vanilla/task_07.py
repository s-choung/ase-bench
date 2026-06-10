from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.md.verlet import VelocityVerlet
from ase import units

atoms = bulk('Cu', 'fcc', a=3.6, cubic=True).repeat((3, 3, 3))
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=300)

E0 = atoms.get_total_energy()
print(f"Initial total energy: {E0:.6f} eV")

dyn = VelocityVerlet(atoms, timestep=1.0 * units.fs)
dyn.run(50)

E1 = atoms.get_total_energy()
print(f"Final total energy:   {E1:.6f} eV")
print(f"Energy drift:         {E1 - E0:.6e} eV")
