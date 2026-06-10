from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

atoms = bulk('Cu', 'fcc').repeat((2, 2, 2))
atoms.calc = EMT()
MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)
dyn = Langevin(atoms, 5 * units.fs, temperature_K=300, friction=0.01 / units.fs)
for i in range(201):
    if i % 50 == 0:
        print(atoms.get_temperature())
    if i < 200:
        dyn.set_temperature(300 + 300 * i / 200)
        dyn.run(1)
