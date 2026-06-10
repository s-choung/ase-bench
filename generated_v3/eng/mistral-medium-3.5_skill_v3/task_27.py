from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.bussi import Bussi
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase import units

atoms = bulk('Ag', 'fcc', a=4.09) * (2, 2, 2)
atoms.calc = EMT()
MaxwellBoltzmannDistribution(atoms, temperature_K=500)
Stationary(atoms)
dyn = Bussi(atoms, timestep=5*units.fs, temperature_K=500)
def log():
    print(dyn.atoms.get_temperature())
dyn.attach(log, interval=50)
dyn.run(200)
