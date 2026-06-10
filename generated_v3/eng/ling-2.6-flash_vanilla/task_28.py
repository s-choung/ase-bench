from ase import Atoms
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.units import fs, K
from ase.build import bulk

atoms = bulk('Cu', 'fcc').repeat(2)
atoms.calc = EMT()

thermostat = Langevin(atoms, timestep=5*fs, temp=300*K, friction=0.01)

def print_temp(a=atoms):
    print(f'Step {a.get_step()}: T={a.get_temperature():.1f}K')

thermostat.attach(print_temp, interval=50)
thermostat.run(200)
