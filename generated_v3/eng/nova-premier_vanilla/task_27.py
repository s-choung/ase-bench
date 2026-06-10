from ase import Atoms, units
from ase.calculators.emt import EMT
from ase.md.nvtberendsen import NVTBerendsen
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution

# Ag lattice constant and bulk modulus
a = 4.09
bulk_modulus = 100 * units.GPa

# Create silver 2x2x2 supercell and EMT calculator
atoms = Atoms('Ag', positions=[(0, 0, 0)], cell=[(a, 0, 0), (0, a, 0), (0, 0, a)], pbc=True)
atoms *= (2, 2, 2)
atoms.calc = EMT()

# Set initial velocities
MaxwellBoltzmannDistribution(atoms, 500 * units.kB)

# NVT dynamics (Bussi thermostat)
dyn = NVTBerendsen(atoms, timestep=5*units.fs, temperature_K=500, taut=100*units.fs)

# Run and log temperature
for i in range(200):
    dyn.run(50)
    temp = atoms.get_temperature()
    print(f"Step: {i*50}, Temperature: {temp:.2f} K")
