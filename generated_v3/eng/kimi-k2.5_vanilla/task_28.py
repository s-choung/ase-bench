from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase import units

atoms = bulk('Cu', cubic=True) * [2, 2, 2]
atoms.calc = EMT()

dyn = Langevin(atoms, 5 * units.fs, 300, 0.02)

for i in range(200):
    dyn.temp = 300 + 300 * i / 199
    dyn.run(1)
    if i % 50 == 0:
        print(f"Step {i}, T = {atoms.get_temperature():.1f} K")
