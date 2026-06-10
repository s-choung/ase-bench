from ase import units
from ase.build import bulk
from ase.md.bussi import Bussi
from ase.calculators.emt import EMT

atoms = bulk('Ag', 'fcc', a=4.09, cubic=True)
atoms = atoms.repeat((2, 2, 2))
atoms.calc = EMT()

def print_temp(atoms=atoms):
    print(f"Step: {atoms.md.current_step:3d}, Temperature: {atoms.get_temperature():.2f} K")

atoms.md = Bussi(atoms, timestep=5 * units.fs, temperature_K=500)
atoms.md.attach(print_temp, interval=50)

atoms.md.run(200)
