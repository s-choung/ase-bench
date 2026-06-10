from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase import units

atoms = bulk('Pd', 'fcc', cubic=True) * (2, 2, 2)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=500)
Stationary(atoms)

def total_energy(a):
    return a.get_potential_energy() + a.get_kinetic_energy()

e_initial = total_energy(atoms)

dyn = VelocityVerlet(atoms, timestep=2 * units.fs)
dyn.run(200)

e_final = total_energy(atoms)

print(f"Initial total energy: {e_initial:.6f} eV")
print(f"Final total energy:   {e_final:.6f} eV")
print(f"Energy difference:    {e_final - e_initial:.6e} eV")
