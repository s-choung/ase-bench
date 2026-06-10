from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase import units

atoms = bulk("Cu", "fcc", a=3.6, cubic=True).repeat((2, 2, 2))
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=300, force_temp=True)

def total_energy(a):
    return a.get_potential_energy() + a.get_kinetic_energy()

print(f"Initial temperature: {atoms.get_temperature():.2f} K")
print(f"Initial energy: {total_energy(atoms):.6f} eV")

dyn = Langevin(
    atoms,
    timestep=5 * units.fs,
    temperature_K=300,
    friction=0.01 / units.fs,
)

dyn.run(100)

print(f"Final temperature: {atoms.get_temperature():.2f} K")
print(f"Final energy: {total_energy(atoms):.6f} eV")
