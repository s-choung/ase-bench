from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin

atoms = bulk('Cu', 'fcc', cubic=True).repeat((2, 2, 2))
atoms.calc = EMT()

dyn = Langevin(atoms, 5 * units.fs, temperature=300 * units.kB, friction=0.02)

for i in range(200):
    dyn.temp = (300 + 300 * i / 200) * units.kB
    dyn.run(1)
    if (i + 1) % 50 == 0:
        print(f"Step {i+1}: {atoms.get_temperature():.1f} K")
