from ase import Atoms, units
from ase.calculators.emt import EMT
from ase.md.bussi import Bussi
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

# Setup
atoms = Atoms('Ag', cell=[4.09, 4.09, 4.09], pbc=True).repeat([2,2,2])
atoms.calc = EMT()
MaxwellBoltzmannDistribution(atoms, 500)
Stationary(atoms)

# Simulation
dyn = Bussi(atoms, timestep=5*units.fs, temperature_K=500)
for i in range(200):
    dyn.run(steps=50)
    print(f"Step {i*50}: T={atoms.get_temperature():.2f} K")
