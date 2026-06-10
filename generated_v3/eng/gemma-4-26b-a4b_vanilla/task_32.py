import numpy as np
from ase import Atoms
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations

# Define H2O molecule geometry
# Using dummy coordinates for a water molecule
# Note: EMT is intended for metals, but the prompt requires its use.
h2o = Atoms('H2O',
             positions=[[0.0000, 0.0000, 0.7572],
                        [0.0000, 0.7572, -0.5864],
                        [0.0000, -0.7572, -0.5864]])

h2o.calc = EMT()

# Calculate vibrational modes
vib = Vibrations(h2o)
vib.run()

# Get frequencies and modes
freqs = vib.get_frequencies()

# Conversion factor: 1 eV to cm^-1 (approx 8065.54)
ev_to_cm = 8065.54

print(f"{'Mode':<10} {'Freq (cm^-1)':<15} {'Freq (eV)':<15}")
for i, f in enumerate(freqs):
    # Handle near-zero frequencies (translations/rotations)
    f_cm = f if f > 1e-3 else 0.0
    f_ev = f_cm / ev_to_cm
    print(f"{i+1:<10} {f_cm:<15.2f} {f_ev:<15.5f}")

vib.clean()
