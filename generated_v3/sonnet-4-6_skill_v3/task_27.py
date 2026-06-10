from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.bussi import Bussi
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase import units

atoms = bulk('Ag', 'fcc', a=4.09, cubic=True) * (2, 2, 2)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=500)
Stationary(atoms)

md = Bussi(atoms, timestep=5*units.fs, temperature_K=500, taut=100*units.fs)

print(f"{'Step':>6}  {'Temperature (K)':>16}")
print("-" * 26)

for step in range(0, 201, 50):
    if step > 0:
        md.run(50)
    T = atoms.get_temperature()
    print(f"{step:>6}  {T:>16.2f}")
