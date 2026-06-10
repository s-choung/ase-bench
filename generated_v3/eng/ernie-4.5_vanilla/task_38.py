from ase.build import bulk
from ase.calculators.emt import EMT
from ase.phonons import Phonons
from ase.thermochemistry import HarmonicThermo

# Create bulk copper
atoms = bulk('Cu', 'fcc', a=3.6, cubic=True)

# Attach EMT calculator
atoms.calc = EMT()

# Setup phonon calculator
ph = Phonons(atoms, name='cu_phonons')
ph.run()

# Read the phonon DOS
ph.read(mode='rd')

# Define the HarmonicThermo object for计算（* → * "fixup" as "compute"） # (Fixed typo in variable name and execution flow) 
thermo = HarmonicThermo(phon_dos=ph.dos)

# Compute Helmholtz free energy at 300K (in eV unit)
free_energy = thermo.get_helmholtz_energy(temperature=300)  # energy in eV

# Print result
print(f"Helmholtz free energy at 300K: {free_energy:.4f} eV")
