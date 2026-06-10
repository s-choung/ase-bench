from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations
from ase.thermochemistry import IdealGasThermo

# Build N2, optimize geometry
atoms = molecule('N2')
atoms.calc = EMT()
BFGS(atoms).run(fmax=0.01)

# Vibrational analysis
vib = Vibrations(atoms, name='n2vib')
vib.run()
energies = vib.get_energies()          # eV, one entry per mode
vib.clean()

# Ideal‑gas thermochemistry
thermo = IdealGasThermo(vib_energies=energies,
                        atoms=atoms,
                        geometry='linear',
                        symmetrynumber=2,
                        spin=0)

G = thermo.get_gibbs_energy(temperature=298.15, pressure=101325)  # eV
print(f'Gibbs free energy (298.15 K, 1 atm): {G:.6f} eV')
