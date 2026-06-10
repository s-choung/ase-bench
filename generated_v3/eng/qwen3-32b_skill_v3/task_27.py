from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.bussi import Bussi
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
import ase.units as units

atoms = bulk('Ag', 'fcc', a=4.086).repeat((2, 2, 2))
atoms.calc = EMT()
MaxwellBoltzmannDistribution(atoms, temperature_K=500)
Stationary(atoms)

md = Bussi(atoms, timestep=5 * units.fs, temperature_K=500, taut=100 * units.fs)

for step in range(0, 200, 50):
    md.run(50)
    temp = atoms.get_temperature()
    print(f"Step {step + 50}: {temp:.2f} K")
