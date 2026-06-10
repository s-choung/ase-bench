from ase.atoms import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations
from ase.thermochemistry import IdealGasThermo

# Build and prepare N2 molecule
atoms = Atoms('N2', positions=[(0, 0, 0), (0, 0, 1.1)], pbc=False)
atoms.calc = EMT()

# Relax geometry to minimum energy
opt = BFGS(atoms)
opt.run(fmax=0.01)

# Calculate vibrational frequencies
vib = Vibrations(atoms)
vib.run()
all_freqs = vib.get_frequencies()
# Filter out translational/rotational near-zero modes
vib_freqs = [f for f in all_freqs if f > 100]  # Only retains physical vibrational mode

# Convert cm-1 frequencies to eV for thermochemistry
vib_energies = [f / 8065.54 for f in vib_freqs]
potential_energy = atoms.get_potential_energy()

# Initialize ideal gas thermochemistry calculator
thermo = IdealGasThermo(
    atoms=atoms,
    geometry='linear',
    symmetrynumber=2,
    potentialenergy=potential_energy,
    vib_energies=vib_energies
)

# Calculate and print results
gibbs_energy = thermo.get_gibbs_energy(temperature=298.15, pressure=101325)
print(f"N2 vibrational frequency: {vib_freqs[0]:.2f} cm⁻¹")
print(f"Gibbs free energy at 298.15 K, 1 atm: {gibbs_energy:.4f} eV")
