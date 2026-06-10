from ase.build import molecule
from ase.calculators import EMT
from ase.calculators.lj import LJCoulomb
from ase.geometry import harmonic_frequencies

nitrogen = molecule('N2')
nitrogen.calc = EMT()
freqs = harmonic_frequencies(nitrogen)
print(freqs)
