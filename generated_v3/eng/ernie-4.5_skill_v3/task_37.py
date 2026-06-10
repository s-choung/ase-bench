from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations
from ase.thermochemistry import IdealGasThermo
from ase import units

# Create N2 molecule
atoms = Atoms('N2', positions=[[0., 0., -0.7], [0., 0., 0.7]])

# Attach calculator and optimize
atoms.calc = EMT()
BFGS(atoms).run(fmax=0.01)

# Calculate vibrational frequencies
vib = Vibrations(atoms)
vib.run()
vib_energies = vib.get_energies()
frequencies = vib.get_frequencies()

# Calculate Gibbs free energy (1 atm = 101325 Pa)
thermo = IdealGasThermo(
    vib_energies=vib_energies,
    atoms=atoms,
    geometry='linear',
    symmetrynumber=2,
    spin=0  # N2 has no unpaired electrons
)

G = thermo.get_gibbs_energy(temperature=298.15, pressure=101325.)

# Output results
print(f"Vibrational frequencies (cm⁻¹): {frequencies}")
print(f"Gibbs free energy at 298.15K and 1 atm: {G / units.eV:.4f} eV")
