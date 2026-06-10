from ase import Atoms, units
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations
from ase.thermochemistry import IdealGasThermo

# Create N2 molecule
n2 = Atoms('N2', positions=[(0, 0, 0), (1.1, 0, 0)])
n2.calc = EMT()

# Optimize structure
opt = BFGS(n2)
opt.run(fmax=0.01)

# Calculate vibrational frequencies
vib = Vibrations(n2)
vib.run()
frequencies = vib.get_frequencies()

# Calculate Gibbs free energy
thermo = IdealGasThermo(vib_energies=frequencies * units.invcm,
                        atoms=n2, geometry='linear', 
                        symmetrynumber=2, spin=0)

G = thermo.get_gibbs_energy(temperature=298.15, pressure=101325)
print(f'Gibbs Free Energy at 298.15K and 1 atm: {G:.2f} eV')

# Clean up
vib.clean()
