from ase.build import bulk
from ase.calculators.emt import EMT
from ase.phonon import Phonon
from ase.thermo import HarmonicThermo

# bulk Cu structure
atoms = bulk('Cu', 'fcc', a=3.6)
atoms.set_calculator(EMT())

# phonon calculation (2×2×2 supercell, 0.01 Å displacement)
phonon = Phonon(atoms, (2, 2, 2), delta=0.01)
phonon.run()
freqs = phonon.get_frequencies()          # THz

# harmonic free energy at 300 K
F = HarmonicThermo(freqs).get_helmholtz_free_energy(temperature=300)
print(F, "eV")
