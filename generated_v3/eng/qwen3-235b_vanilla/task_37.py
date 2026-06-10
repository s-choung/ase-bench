from ase import Atoms
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations
from ase.thermochemistry import IdealGasThermo

# Create N2 molecule
d = 1.10  # bond length in Å
n2 = Atoms('N2', positions=[(0, 0, 0), (0, 0, d)])
n2.center(vacuum=5.0)
n2.calc = EMT()

# Calculate vibrational frequencies
vib = Vibrations(n2, name='n2_vib')
vib.run()
freqs = vib.get_frequencies()

# Filter out real, positive frequencies (exclude imaginary and zero modes)
real_freqs = [freq for freq in freqs if freq > 0]

# Use IdealGasThermo to compute Gibbs free energy
thermo = IdealGasThermo(
    potentialenergy=n2.get_potential_energy(),
    entropy=0,  # Not used directly; will compute from vibrations
    temperatures=[298.15],
    spin=0,
    geometry='linear',
    symmetrynumber=2,
    vib_energies=real_freqs[:1],  # Only one vibrational mode for diatomic
    natoms=2
)

g = thermo.get_gibbs_energy(temperature=298.15, pressure=1.0)

print(g)
