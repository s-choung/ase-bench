from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

# Create and setup N2 molecule
atoms = Atoms('N2', positions=[[0, 0, 0], [0, 0, 1.1]])
atoms.calc = EMT()

# Optimize geometry
dyn = BFGS(atoms)
dyn.run(fmax=0.01)

# Calculate vibrational frequencies
vib = Vibrations(atoms)
vib.run()
frequencies = vib.get_frequencies().real
vib.clean()

# Print non-zero frequencies
nvibs = frequencies[frequencies > 20]  # Filter out translational/rotational modes
for freq in nvibs:
    print(f"{freq:.2f}")
