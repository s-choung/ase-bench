from ase import Atoms
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations

# Set up H2O molecule
h2o = Atoms('H2O', positions=[[0.0, 0.0, 0.0],
                              [0.757, 0.586, 0.0],
                              [-0.757, 0.586, 0.0]])
h2o.calc = EMT()

# Run vibrational analysis
vib = Vibrations(h2o)
vib.run()
vib.summary()

# Print frequencies and energies
freqs = vib.get_frequencies().real  # in Hz
for i, f in enumerate(freqs):
    if f > 0:
        freq_cm = f / (2.99792458e10)  # Hz to cm^-1
        energy_ev = f * 4.135667662e-15  # Hz to eV
        print(f"Mode {i}: {freq_cm:.1f} cm^-1, {energy_ev:.5f} eV")

vib.clean()
