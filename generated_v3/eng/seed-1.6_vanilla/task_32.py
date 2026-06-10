from ase import molecule
from ase.calculators.emt import EMT
from ase.optimizers import BFGS
from ase.vibrations import Vibrations

# Setup H2O, optimize, compute vibrations
atoms = molecule('H2O')
atoms.calc = EMT()
BFGS(atoms).run(fmax=1e-3)
vib = Vibrations(atoms)
vib.run()

# Convert cm⁻¹ to eV (1 cm⁻¹ = 1.23984193e-4 eV)
conv = 1.23984193e-4

# Print vibrational modes (skip translational/rotational zeros)
for idx, freq in enumerate(vib.get_frequencies()):
    if freq > 1:
        energy = freq * conv
        print(f'Mode {idx+1}: {freq:.2f} cm⁻¹, {energy:.6f} eV')
