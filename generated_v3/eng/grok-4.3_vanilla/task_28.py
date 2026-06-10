from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase import units

atoms = bulk('Cu', 'fcc', cubic=True) * (2, 2, 2)
atoms.calc = EMT()
dyn = Langevin(atoms, 5 * units.fs, temperature_K=300, friction=0.02)

for i in range(200):
    T = 300 + 300 * i / 200
    dyn.set_temperature(temperature_K=T)
    dyn.run(1)
    if (i + 1) % 50 == 0:
        print(atoms.get_temperature())
