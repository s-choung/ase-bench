from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

atoms = bulk("Cu", "fcc", a=3.6, cubic=True) * (3, 3, 3)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=300, force_temp=True)
Stationary(atoms)

def total_energy(a):
    return a.get_potential_energy() + a.get_kinetic_energy()

e0 = total_energy(atoms)
print(f"Initial total energy: {e0:.8f} eV")

dyn = VelocityVerlet(atoms, timestep=1.0 * units.fs)
dyn.run(50)

e1 = total_energy(atoms)
print(f"Final total energy:   {e1:.8f} eV")
print(f"Energy drift:         {e1 - e0:.8e} eV")
