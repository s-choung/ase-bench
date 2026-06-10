from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase import units

# Cu fcc 2x2x2 supercell
atoms = bulk('Cu', 'fcc', a=3.6) * (2, 2, 2)
atoms.calc = EMT()

# initial velocities at 300 K
MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

# MD parameters
t0, tf = 300.0, 600.0          # K
steps = 200
dt = 5 * units.fs
friction = 0.01 / units.fs

dyn = Langevin(atoms, timestep=dt, temperature_K=t0,
               friction=friction)

for i in range(steps):
    # linear temperature ramp
    T = t0 + (tf - t0) * (i + 1) / steps
    dyn.temperature = T
    dyn.run(1)                # one MD step

    if (i + 1) % 50 == 0:
        print(f"Step {i + 1:3d}, T = {atoms.get_temperature():.1f} K")
