from ase import Atoms
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations
from ase.units import invcm, _hplanck, _c, _e

# H2O geometry (approximate, in Angstrom)
# Oxygen at origin, hydrogens at ~0.958 Å from O, 104.5° angle
import numpy as np
hoh_angle = 104.5 * np.pi / 180.0  # radians
r_OH = 0.958
H1 = [r_OH, 0, 0]
H2 = [r_OH * np.cos(hoh_angle), r_OH * np.sin(hoh_angle), 0]
O = [0, 0, 0]

atoms = Atoms('OH2', positions=[O, H1, H2])
atoms.calc = EMT()

vib = Vibrations(atoms)
vib.run()
freqs = vib.get_frequencies()  # in cm^-1

print('Vibrational mode frequencies:')
for f in freqs:
    # Energy in eV: E = h * c * freq (freq in cm^-1), convert J to eV
    energy_ev = _hplanck * _c * f * invcm / _e
    print(f'Frequency: {f:.2f} cm^-1, Energy: {energy_ev:.4f} eV')

vib.clean()
