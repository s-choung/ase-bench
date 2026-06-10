from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase import units

atoms = bulk('Cu', 'fcc', a=3.615).repeat((2, 2, 2))
atoms.calc = EMT()
MaxwellBoltzmannDistribution(atoms, temperature_K=300)

dyn = Langevin(atoms, timestep=5 * units.fs, temperature_K=300, friction=0.02)

nsteps = 200
T_start, T_end = 300, 600

for i in range(nsteps):
    T_target = T_start + (T_end - T_start) * i / (nsteps - 1)
    dyn.set_temperature(temperature_K=T_target)
    dyn.run(1)
    if (i + 1) % 50 == 0:
        print(f"Step {i+1}: target T = {T_target:.1f} K, current T = {atoms.get_temperature():.1f} K")
