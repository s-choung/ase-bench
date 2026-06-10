from ase import Atoms
from ase.optimize import BFGS
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations
from ase.thermochemistry import IdealGasThermo

# Set up N2 molecule with approximate bond length
n2 = Atoms('N2', positions=[(0, 0, 0), (0, 0, 1.10)])
n2.calc = EMT()

# Optimize geometry
BFGS(n2).run(fmax=0.01)

# Calculate vibrational frequencies
vib = Vibrations(n2)
vib.run()
vib_energies = vib.get_energies()

# Compute Gibbs free energy at 298.15 K and 1 atm
thermo = IdealGasThermo(
    vib_energies=vib_energies,
    geometry='linear',
    spin=0,
    symmetrynumber=2,
    natoms=2
)

G = thermo.get_gibbs_energy(temperature=298.15, pressure=101325)
print(f'Gibbs free energy of N2 at 298.15 K, 1 atm: {G:.6f} eV')
