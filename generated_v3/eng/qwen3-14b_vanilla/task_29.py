from ase.build import fcc
from ase.calculators.emt import EMT
from ase.md.velocityverlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution

atoms = fcc('Pd', a=3.88, size=(2, 2, 2))
atoms.set_calculator(EMT())
MaxwellBoltzmannDistribution(atoms, temperature_K=500)
md = VelocityVerlet(atoms, timestep=2e-15)
initial_energy = atoms.get_total_energy()
for _ in range(200):
    md.step()
final_energy = atoms.get_total_energy()
print(final_energy - initial_energy)
