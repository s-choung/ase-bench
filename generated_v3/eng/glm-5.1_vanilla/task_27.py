from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.bussi import Bussi
from ase import units

atoms = bulk('Ag', 'fcc') * (2, 2, 2)
atoms.calc = EMT()

md = Bussi(atoms, timestep=5 * units.fs, temperature_K=500, taut=100 * units.fs)

def print_temp():
    print(f"Step {md.nsteps}, T = {atoms.get_temperature():.2f} K")

md.attach(print_temp, interval=50)
md.run(200)
