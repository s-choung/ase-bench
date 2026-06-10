from ase.build import bulk
from ase.md.bussi import Bussi
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.calculators.emt import EMT
from ase import units

atoms = bulk('Ag', 'fcc', a=4.09) * (2, 2, 2)
atoms.calc = EMT()
MaxwellBoltzmannDistribution(atoms, temperature_K=500)

dynamics = Bussi(atoms, timestep=5 * units.fs, temperature_K=500)

for step in range(200):
    dynamics.run(1)
    if (step + 1) % 50 == 0:
        print(f"Step {step + 1}: Temperature = {atoms.get_temperature():.2f} K")

print(f"Final temperature: {atoms.get_temperature():.2f} K")
