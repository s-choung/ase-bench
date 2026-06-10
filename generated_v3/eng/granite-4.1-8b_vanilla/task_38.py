from ase import Atoms
from ase.calculators.emt import EMT
from ase.calculations.vibrationalanalysis import VibrationalAnalysis
from ase.units import Bohr, Hartree
from ase.thermochemistry import HarmonicThermo

# Lattice constant for bulk Cu (Angstroms)
a = 3.615

# Create a face-centered cubic Cu bulk structure
atoms = Atoms('Cu', positions=[[0, 0, 0], 
                                [a/2, a/2, 0], 
                                [a/2, 0, a/2], 
                                [0, a/2, a/2]], 
              cell=[a, a, a], pbc=True)

# Set up the EMT calculator
atoms.set_calculator(EMT())

# Optimize geometry to get the equilibrium structure
atoms.get_potential_energy()

# Perform vibrational analysis
vib = VibrationalAnalysis(atoms)
vib.run()

# Convert frequencies from atomic units (1/Bohr) to cm⁻¹
frequencies_cm = vib.get_frequencies() * Hartree / (Bohr**2) / (1.98644586e-23)  # 1 eV = 1.98644586e-23 J

# Compute Helmholtz free energy at 300 K using HarmonicThermo
thermo = HarmonicThermo(vib, T=300)
free_energy_ev = thermo.get_free_energy('Hvib+Ee')

# Print the Helmholtz free energy
print(f"Helmholtz free energy at 300 K: {free_energy_ev:.4f} eV")
