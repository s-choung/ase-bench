from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.bussi import Bussi
from ase import units

# Build 2x2x2 FCC Ag supercell
atoms = bulk('Ag', 'fcc', a=4.09, cubic=True)
atoms = atoms * (2, 2, 2)

# Set up EMT calculator
atoms.calc = EMT()

# Bussi thermostat (NVT) at 500 K, 5 fs timestep
dyn = Bussi(atoms, timestep=5*units.fs, temperature_K=500)

# Run 200 steps, printing temperature every 50 steps
for i in range(200):
    dyn.run(1)
    if (i + 1) % 50 == 0:
        temp = atoms.get_temperature()
        print(f"Step {i+1}: Temperature = {temp:.2f} K")
