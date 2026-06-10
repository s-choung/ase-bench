from ase import Atoms
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations
from ase.units import invcm   # 1 cm⁻¹ in eV

# Approximate H2O geometry (bond length ≈ 0.96 Å, angle ≈ 104.5°)
h2o = Atoms('H2O',
            positions=[[0.0, 0.0, 0.0],
                       [0.757, 0.586, 0.0],
                       [-0.757, 0.586, 0.0]])

h2o.calc = EMT()
vib = Vibrations(h2o)
vib.run()

freqs = vib.get_frequencies()          # in cm⁻¹
for i, f in enumerate(freqs):
    zpe = 0.5 * f * invcm               # zero‑point energy in eV
    print(f'Mode {i}: {f:8.2f} cm-1   ZPE = {zpe:.6f} eV')
