from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary, ZeroRotation
from ase.md.verlet import VelocityVerlet
from ase import units

atoms = bulk('Pd', 'fcc', a=3.89).repeat((2, 2, 2))
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=500)
Stationary(atoms)
ZeroRotation(atoms)

dyn = VelocityVerlet(atoms, timestep=2 * units.fs)

e0 = atoms.get_total_energy()
dyn.run(200)
e1 = atoms.get_total_energy()

print(f"Initial total energy: {e0:.8f} eV")
print(f"Final total energy:   {e1:.8f} eV")
print(f"Difference:           {e1 - e0:.8e} eV")
