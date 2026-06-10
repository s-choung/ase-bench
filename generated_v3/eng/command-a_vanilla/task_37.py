from ase.calculators.emt import EMT
from ase.vibrations import Vibrations
from ase.thermochemistry import IdealGasThermo
from ase import Atoms

# Set up N2 molecule
n2 = Atoms('N2', positions=[[0, 0, 0], [0, 0, 1.1]], calculator=EMT())
n2.center(vacuum=5.0)

# Calculate vibrational frequencies
vib = Vibrations(n2)
vib.run()
frequencies = vib.get_frequencies()

# Set up IdealGasThermo and compute Gibbs free energy
thermo = IdealGasThermo(vib_freqs=frequencies,
                        geometry='linear',
                        atoms=n2,
                        symmetrynumber=2,
                        spin=0)

gibbs_energy = thermo.get_gibbs_energy(temperature=298.15, pressure=101325)

print(f"Gibbs free energy at 298.15K and 1 atm: {gibbs_energy:.4f} eV")
