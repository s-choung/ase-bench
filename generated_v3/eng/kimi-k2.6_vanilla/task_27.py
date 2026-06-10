from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase import units

atoms = bulk('Ag', 'fcc', a=4.09, cubic=True) * [2, 2, 2]
atoms.calc = EMT()
MaxwellBoltzmannDistribution(atoms, temperature_K=500)

dyn = Langevin(atoms, 5 * units.fs, temperature=500, friction=0.1)

def print_temp():
    print(f'Step {dyn.nsteps:4d} T = {atoms.get_temperature():.1f} K')

dyn.attach(print_temp, interval=50)
print_temp()
dyn.run(200)
