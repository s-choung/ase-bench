from ase import *
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md import Bussi
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution

atoms = bulk('Ag', 'fcc', a=4.086, cubic=True) * (2,2,2)
atoms.calc = EMT()
MaxwellBoltzmannDistribution(atoms, 500.0)
dynamics = Bussi(atoms, 500.0, 5.0)
for i in range(200):
    dynamics.run(1)
    if (i + 1) % 50 == 0:
        print(f"Step {i+1}, Temperature: {dynamics.temperature} K")
