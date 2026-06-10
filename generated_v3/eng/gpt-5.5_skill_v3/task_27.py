from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.bussi import Bussi
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

atoms = bulk("Ag", "fcc", a=4.09, cubic=True) * (2, 2, 2)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=500)
Stationary(atoms)

dyn = Bussi(
    atoms,
    timestep=5 * units.fs,
    temperature_K=500,
    taut=100 * units.fs,
)

temps = []
for step in range(50, 201, 50):
    dyn.run(50)
    temp = atoms.get_temperature()
    temps.append((step, temp))
    print(f"Step {step:4d}: T = {temp:8.2f} K")
