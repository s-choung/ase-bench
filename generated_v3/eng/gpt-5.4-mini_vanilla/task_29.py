from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.velocityverlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase import units

atoms = bulk('Pd', 'fcc', a=3.89, cubic=True) * (2, 2, 2)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=500)
Stationary(atoms)

e0 = atoms.get_total_energy()

dyn = VelocityVerlet(atoms, timestep=2 * units.fs)
dyn.run(200)

e1 = atoms.get_total_energy()
print(f"Initial total energy: {e0:.6f} eV")
print(f"Final total energy:   {e1:.6f} eV")
print(f"Difference:           {e1 - e0:.6e} eV")
