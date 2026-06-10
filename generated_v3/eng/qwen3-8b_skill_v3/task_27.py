from ase.build import bulk
from ase.md.bussi import Bussi
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase.units import fs
from ase.calculators.emt import EMT

atoms = bulk('Ag', 'fcc', a=4.08, cubic=True).repeat((2, 2, 2))
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=500)
Stationary(atoms)

dyn = Bussi(atoms, timestep=5*fs, temperature_K=500)

def callback(step, atoms):
    if step % 50 == 0:
        print(f"Step {step}: Temperature = {atoms.get_temperature()} K")

dyn.run(steps=200, callback=callback)
