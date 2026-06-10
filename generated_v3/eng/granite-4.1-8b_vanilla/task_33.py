from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

# Create CH4 molecule
atoms = Atoms('CH4', positions=[(0, 0, 0), (0, 0, 0.9572)]*2,
              positions=[(0.0, -0.zw, -0.zw), (0.z, -0.0, 0.0),
                         (0.z, 0.0, -0.0), (-0.0, 0.z, 0.0)],
              cell=4.2*ase.cell.Cell)

# Set up EMT calculator
atoms.calc = EMT()

# Optimize structure
optimizer = BFGS(atoms)
optimizer.run(fmax=0.05)

# Perform vibration calculation
vib = Vibrations(atoms)
vib.run()
vib.write("vibrations.yaml")

# Filter and print real frequencies
real_frequencies = [freq for freq in vib.get_frequencies() if freq >= 0]
for freq in real_frequencies:
    print(freq)
