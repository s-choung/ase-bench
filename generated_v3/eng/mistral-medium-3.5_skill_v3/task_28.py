from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase import units

atoms = bulk('Cu', 'fcc', a=3.6, cubic=True) * (2, 2, 2)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

dyn = Langevin(atoms, timestep=5*units.fs, temperature_K=300, friction=0.01/units.fs)
dyn.attach(lambda: print(f"Step {dyn.get_number_of_steps():3d}, Temp: {atoms.get_temperature():6.2f}K")
           if dyn.get_number_of_steps() % 50 == 0 else None, interval=1)

for T in range(300, 601, 1):
    dyn.set_temperature(K=T)
    dyn.run(1)
