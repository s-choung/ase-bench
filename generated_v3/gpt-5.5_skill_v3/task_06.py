from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase import units

atoms = bulk("Cu", "fcc", a=3.6, cubic=True) * (2, 2, 2)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

print(f"Initial T = {atoms.get_temperature():.2f} K")
print(f"Initial Epot = {atoms.get_potential_energy():.6f} eV")
print(f"Initial Etot = {atoms.get_total_energy():.6f} eV")

dyn = Langevin(
    atoms,
    timestep=5 * units.fs,
    temperature_K=300,
    friction=0.01 / units.fs,
)
dyn.run(100)

print(f"Final T = {atoms.get_temperature():.2f} K")
print(f"Final Epot = {atoms.get_potential_energy():.6f} eV")
print(f"Final Etot = {atoms.get_total_energy():.6f} eV")
