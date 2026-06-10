from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations
from ase.thermochemistry import HarmonicThermo

# bulk Cu, conventional fcc cell
atoms = bulk('Cu', 'fcc', a=3.6)

# small supercell to keep the calculation fast
atoms = atoms * (2, 2, 2)

# attach EMT calculator
atoms.calc = EMT()

# set up and run vibrational analysis
vib = Vibrations('Cu_bulk', atoms)
vib.run()

# vibrational frequencies (in eV)
freqs = vib.get_frequencies()

# Helmholtz free energy at 300 K
thermo = HarmonicThermo(freqs)
F = thermo.get_helmholtz_free_energy(temperature=300)

print(f'Helmholtz free energy (eV): {F}')
