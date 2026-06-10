from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase import units

# Cu FCC 2×2×2 supercell
atoms = bulk('Cu', 'fcc', a=3.6) * (2, 2, 2)
atoms.calc = EMT()

# initial velocities at 300 K
MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

# Langevin dynamics (initial temperature 300 K)
dyn = Langevin(atoms, timestep=5 * units.fs,
               temperature_K=300, friction=0.01 / units.fs)

# MD with linear temperature ramp 300 K → 600 K
for step in range(200):
    target_T = 300 + (600 - 300) * step / 199   # linear schedule
    dyn.temperature = target_T                 # update thermostat temperature
    dyn.run(1)                                 # one integration step
    if (step + 1) % 50 == 0:
        print(f"Step {step+1:3d}: T = {atoms.get_temperature():.2f} K "
              f"(target {target_T:.2f} K)")
