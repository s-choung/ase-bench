from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations
from ase.thermochemistry import IdealGasThermo

# Relax N2 molecule
atoms = molecule('N2')
atoms.calc = EMT()
BFGS(atoms).run(fmax=0.01)

# Calculate vibrational properties
vib = Vibrations(atoms)
vib.run()
vib_freqs = vib.get_frequencies()
vib_energies = vib.get_energies()
print(f"Vibrational frequencies (cm⁻¹): {vib_freqs.round(2)}")

# Compute Gibbs free energy
thermo = IdealGasThermo(
    vib_energies=vib_energies,
    atoms=atoms,
    geometry='linear',
    symmetrynumber=2,
    spin=0
)
gibbs_energy = thermo.get_gibbs_energy(temperature=298.15, pressure=101325)
print(f"Gibbs free energy at 298.15 K, 1 atm: {gibbs_energy:.3f} eV")

vib.clean()
