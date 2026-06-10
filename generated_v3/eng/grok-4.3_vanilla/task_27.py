from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.bussi import Bussi
from ase import units
atoms = bulk('Ag', 'fcc', cubic=True).repeat(2)
atoms.calc = EMT()
dyn = Bussi(atoms, timestep=5*units.fs, temperature_K=500)
dyn.attach(lambda: print(atoms.get_temperature()), interval=50)
dyn.run(200)
