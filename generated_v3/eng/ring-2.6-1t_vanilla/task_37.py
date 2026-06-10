from ase import Atoms
from ase.build import molecule
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations
from ase.thermochemistry import IdealGasThermo

# N2 molecule with EMT
atoms = molecule('N2')
atoms.calc = EMT()

# Vibrational analysis
vib = Vibrations(atoms)
vib.run()
freqs = vib.get_frequencies()                     # eV
freqs_cm = freqs * 8065.54429                     # convert to cm⁻¹
freqs_cm = freqs_cm[freqs_cm > 1e-5]              # keep real vibrations

# Gibbs free energy at 298.15 K, 1 atm
thermo = IdealGasThermo(freqs_cm,
                        geometry='linear',
                        symmetrynumber=2,
                        temperature=298.15,
                        pressure=101325)           # 1 atm in Pa
G = thermo.get_gibbs_energy()
print(f'Gibbs free energy: {G:.4f} eV')
