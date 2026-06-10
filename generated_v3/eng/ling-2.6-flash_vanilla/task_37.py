from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.io import read
from ase.thermochemistry import IdealGasThermo, HarmonicThermo
from ase.vibrations import Vibrations

# Create N2 molecule
atoms = Atoms('N2', positions=[[0, 0, 0], [0, 0, 1.1]])
atoms.set_calculator(EMT())

# Fix center of mass for linear molecule vibrations
constraint = FixAtoms(indices=[0])
atoms.set_constraint(constraint)

# Calculate vibrational frequencies
vib = Vibrations(atoms)
frequencies = vib.get_frequencies()
print("Vibrational frequencies (Hz):", frequencies)

# Compute Gibbs free energy using IdealGasThermo
thermo = IdealGasThermo(
    frequencies=frequencies,
    potentialenergy=atoms.get_potential_energy(),
    atoms=atoms,
    symmetrynumber=2,
)

T = 298.15  # K
P = 101325  # Pa (1 atm)
gibbs_free_energy = thermo.get_gibbs_free_energy(T, P)
print(f"Gibbs free energy at {T} K and {P} Pa: {gibbs_free_energy:.2f} J/mol")
