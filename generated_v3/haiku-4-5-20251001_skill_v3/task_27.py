from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.bussi import Bussi
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase import units

atoms = bulk('Ag', 'fcc', a=4.09) * (2, 2, 2)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=500)
Stationary(atoms)

md = Bussi(atoms, timestep=5*units.fs, temperature_K=500)

for step in range(200):
    md.run(1)
    if (step + 1) % 50 == 0:
        T = atoms.get_temperature()
        print(f"Step {step + 1}: T = {T:.2f} K")
