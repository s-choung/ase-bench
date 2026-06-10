from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary, ZeroRotation
from ase.md.bussi import Bussi

atoms = bulk("Ag", "fcc", cubic=True) * (2, 2, 2)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=500)
Stationary(atoms)
ZeroRotation(atoms)

dyn = Bussi(atoms, timestep=5 * units.fs, temperature_K=500, taut=100 * units.fs)

for _ in range(4):
    dyn.run(50)
    print(f"Step {dyn.nsteps}: T = {atoms.get_temperature():.2f} K")
