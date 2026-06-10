from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.bussi import Bussi
from ase import units

atoms = bulk('Ag', 'fcc', a=4.09) * (2, 2, 2)
atoms.calc = EMT()

from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
MaxwellBoltzmannDistribution(atoms, temperature_K=500)
Stationary(atoms)

md = Bussi(atoms, timestep=5 * units.fs, temperature_K=500, taut=100 * units.fs)

def print_temperature(md_step):
    if md_step % 50 == 0:
        print(f"Step {md_step}: Temperature = {atoms.get_temperature()} K")

md.attach(print_temperature, interval=1, args=(md.nsteps,))
md.run(200)
