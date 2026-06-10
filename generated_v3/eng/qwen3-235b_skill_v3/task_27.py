from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase.md.bussi import Bussi
from ase.io.trajectory import Trajectory

atoms = bulk('Ag', 'fcc') * (2, 2, 2)
atoms.calc = EMT()
MaxwellBoltzmannDistribution(atoms, temperature_K=500)
Stationary(atoms)

dyn = Bussi(atoms, timestep=5 * units.fs, temperature_K=500)
traj = Trajectory('md.traj', 'w', atoms)

for step in range(200):
    dyn.run(1)
    traj.write()
    if step % 50 == 0:
        print(f"Step {step}: {atoms.get_temperature():.2f} K")
