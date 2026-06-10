from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.bussi import Bussi
from ase import units

atoms = bulk('Ag', 'fcc', a=4.09) * (2, 2, 2)
atoms.calc = EMT()
dyn = Bussi(atoms, timestep=5*units.fs, temperature=500)

for i in range(4):
    dyn.run(50)
    print(f"Step {(i+1)*50}: T = {atoms.get_temperature():.2f} K")
