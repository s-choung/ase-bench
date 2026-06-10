from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase import units

atoms = bulk('Cu', cubic=True) * (2, 2, 2)
atoms.calc = EMT()

dyn = Langevin(atoms, timestep=5 * units.fs, temperature_K=300, friction=0.02)

for i in range(200):
    dyn.temperature_K = 300 + 300 * (i + 1) / 200
    dyn.run(1)
    if (i + 1) % 50 == 0:
        print(f"Step: {i + 1}, Temperature: {atoms.get_temperature():.2f} K")
