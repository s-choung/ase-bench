from ase import Atoms
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations
from ase.thermochemistry import IdealGasThermo

# N2 molecule setup
n2 = Atoms('N2', positions=[(0, 0, 0), (0, 0, 1.1)], symmetrynumber=2)
n2.calc = EMT()

# Vibrational analysis
vib = Vibrations(n2)
vib.run()
vib.summary()

# Calculate Gibbs free energy
thermo = IdealGasThermo(vib_energies=vib.get_energies(), geometry='linear', atoms=n2, symmetrynumber=2)
print(f"Gibbs free energy: {thermo.get_gibbs_energy(temperature=298.15, pressure=1.0)}")
