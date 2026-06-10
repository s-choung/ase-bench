from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase import units
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

# Build Cu FCC supercell
atoms = bulk('Cu', 'fcc', a=3.6) * (2, 2, 2)
atoms.calc = EMT()

# Initialize dynamics
MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)
dyn = Langevin(atoms, timestep=5*units.fs, temperature_K=300, friction=0.01/units.fs)

# Run MD and print results
t0 = atoms.get_temperature()
e0 = atoms.get_potential_energy()
dyn.run(100)
t1 = atoms.get_temperature()
e1 = atoms.get_potential_energy()

print(f"Initial: T = {t0:.3f} K, E = {e0:.5f} eV")
print(f"Final:   T = {t1:.3f} K, E = {e1:.5f} eV")
