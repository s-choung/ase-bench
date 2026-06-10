from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import BFGS, FrechetCellFilter
from ase.phonons import Phonons
from ase.thermochemistry import HarmonicThermo
from ase import units

# Cu 2x2x2 fcc supercell (avoids zero-only acoustic modes)
atoms = bulk('Cu', 'fcc').repeat((2,2,2))
atoms.calc = EMT()

# Relax cell + positions
BFGS(FrechetCellFilter(atoms)).run(fmax=0.01)

# Phonon calculation (periodic vibrational frequencies)
ph = Phonons(atoms, 'cu_phonons', delta=0.01)
ph.run()
ph.read(acoustic=True)
freqs_eV = ph.get_frequencies().flatten() * units.invcm_to_eV
non_zero_freqs = freqs_eV[3:]  # Exclude 3 acoustic zero modes

# Harmonic Helmholtz free energy at 300K
thermo = HarmonicThermo(vib_energies=non_zero_freqs, volume=atoms.get_volume())
f_energy = thermo.get_helmholtz_energy(temperature=300)
print(f_energy)
