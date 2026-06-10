from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase import units

# Cu FCC 2×2×2 supercell
atoms = bulk('Cu', 'fcc', a=3.6) * (2, 2, 2)
atoms.calc = EMT()

# initial velocities (300 K)
MaxwellBoltzmannDistribution(atoms, temperature_K=300)

# initial state
E0 = atoms.get_total_energy()
T0 = atoms.get_temperature()

# Langevin dynamics: 5 fs step, 300 K, friction 0.02 ps⁻¹
dyn = Langevin(atoms, timestep=5 * units.fs, temperature_K=300, friction=0.02)
dyn.run(100)

# final state
E1 = atoms.get_total_energy()
T1 = atoms.get_temperature()

print(f'Initial   T = {T0:6.2f} K, E = {E0:10.3f} eV')
print(f'Final     T = {T1:6.2f} K, E = {E1:10.3f} eV')
