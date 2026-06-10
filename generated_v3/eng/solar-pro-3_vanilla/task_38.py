from ase import Atoms
from ase.calculators.emt import EMT
from ase.thermodynamics import HarmonicThermo

# Cu FCC bulk with lattice constant 3.614 Å
Cu_bulk = Atoms('Cu4', 
                positions=[[0,0,0], [1.807,1.807,1.807], [0,1.807,3.614], [1.807,0,3.614]],
                cell=[3.614,3.614,3.614],
                pbc=True)
Cu_bulk.set_cell(Cu_bulk.get_cell(), scale_atoms=True)
Cu_bulk.calc = EMT()

# Compute phonon frequencies
frc = Cu_bulk.get_forces()
vib = Cu_bulk.get_vibrations()
freq = vib.get_frequencies()

# Harmonic thermodynamics at 300 K
thermo = HarmonicThermo(Cu_bulk, temperatures=[300])
helmholtz = thermo.get_helmholtz()

print(f"Phonon frequencies (eV): {freq}")
print(f"Helmholtz free energy (eV): {helmholtz}")
