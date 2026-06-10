from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.velocityverlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary, ZeroRotation
from ase import units

atoms = bulk('Cu', 'fcc', a=3.615, cubic=True) * (2, 2, 2)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)
ZeroRotation(atoms)

dyn = VelocityVerlet(atoms, timestep=1.0 * units.fs)

e0 = atoms.get_total_energy()
print(f"Initial total energy: {e0:.6f} eV")

dyn.run(50)

e1 = atoms.get_total_energy()
print(f"Final total energy:   {e1:.6f} eV")
