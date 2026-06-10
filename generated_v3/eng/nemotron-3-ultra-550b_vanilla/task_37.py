from ase import Atoms
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations
from ase.thermochemistry import IdealGasThermo

# Create N2 molecule
d = 1.10  # bond length in Angstrom
n2 = Atoms('N2', positions=[(0, 0, 0), (0, 0, d)])
n2.calc = EMT()

# Calculate vibrational frequencies
vib = Vibrations(n2)
vib.run()
vib_energies = vib.get_energies()  # in eV
vib.clean()

# Get potential energy
potential_energy = n2.get_potential_energy()

# Compute Gibbs free energy
thermo = IdealGasThermo(vib_energies=vib_energies,
                        potentialenergy=potential_energy,
                        atoms=n2,
                        geometry='linear',
                        symmetrynumber=2,
                        spin=1)
G = thermo.get_gibbs_energy(temperature=298.15, pressure=101325)

print(f"Gibbs free energy at 298.15 K, 1 atm: {G:.6f} eV")
