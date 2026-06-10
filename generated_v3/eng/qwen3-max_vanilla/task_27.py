from ase import Atoms
from ase.build import bulk
from ase.md.nvtbussi import NVTBerendsen
from ase.units import fs
from ase.calculators.emt import EMT

# Create Ag FCC 2x2x2 supercell
atoms = bulk('Ag', 'fcc', a=4.09).repeat((2, 2, 2))
atoms.calc = EMT()

# Set up NVT Bussi thermostat
md = NVTBerendsen(atoms, timestep=5*fs, temperature_K=500, taut=100*fs)

# Run MD and print temperature every 50 steps
for step in range(200):
    md.run(1)
    if (step + 1) % 50 == 0:
        temp = atoms.get_temperature()
        print(f'Step {step + 1}: Temperature = {temp:.2f} K')
