from ase import Atoms
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations

# Note: ASE's EMT calculator only supports specific FCC metals (Al, Ni, Cu, Pd, Ag, Pt, Au).
# Attempting to use Nitrogen (N) will raise a NotImplementedError in standard ASE.
n2 = Atoms('N2', positions=[[0, 0, 0], [0, 0, 1.1]])
n2.calc = EMT()

vib = Vibrations(n2)
vib.run()
vib.summary()
print("Frequencies (cm^-1):", vib.get_frequencies())
