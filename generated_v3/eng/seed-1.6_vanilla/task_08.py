from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

# N2 molecule
atoms = Atoms('N2', positions=[[0, 0, 0], [1.1, 0, 0]])
atoms.calc = EMT()

# Optimize geometry
BFGS(atoms).run(fmax=1e-3)

# Vibrational analysis
vib = Vibrations(atoms)
vib.run()

# Convert eV to cm⁻¹ and print vibrational modes (filter zero/rot/trans)
freqs_cm = vib.get_frequencies() * 8065.54429
vibrational = [f for f in freqs_cm if abs(f) > 1e-2]
print("Vibrational frequency (cm⁻¹):", vibrational)
