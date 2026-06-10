from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.units import fs

# Cu lattice constant (Å)
a = 3.615

# 2x2x2 fcc supercell
cu = bulk('Cu', 'fcc', a=a, cubic=True) * (2, 2, 2)
cu.calc = EMT()

# Initial velocities at 300 K
MaxwellBoltzmannDistribution(cu, temperature_K=300)

print(f"Initial temperature: {cu.get_temperature():.2f} K")
print(f"Initial total energy: {cu.get_total_energy():.6f} eV")

# Langevin dynamics: 5 fs timestep, 300 K, light friction
dyn = Langevin(cu, timestep=5 * fs, temperature=300, friction=0.01)
dyn.run(100)

print(f"Final temperature: {cu.get_temperature():.2f} K")
print(f"Final total energy: {cu.get_total_energy():.6f} eV")
