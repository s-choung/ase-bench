from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations
from ase.thermochemistry import IdealGasThermo
from ase import units

# Build N2 molecule
atoms = molecule('N2')
atoms.calc = EMT()

# Geometry optimization (required before vibrations)
BFGS(atoms).run(fmax=0.01)

# Vibrational analysis
vib = Vibrations(atoms, name='vib')
vib.run()
vib_energies = vib.get_energies()  # in eV
vib.clean()

# Thermochemistry: Gibbs free energy at 298.15 K, 1 atm
thermo = IdealGasThermo(
    vib_energies=vib_energies,
    atoms=atoms,
    geometry='linear',
    symmetrynumber=2,
    spin=0
)
G = thermo.get_gibbs_energy(temperature=298.15, pressure=101325)
print(f"Gibbs free energy: {G:.6f} eV")
