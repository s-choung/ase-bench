from ase import Atoms
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations
from ase.thermochemistry import HarmonicThermo

# Create Cu bulk and set EMT calculator
atoms = Atoms('Cu', cell=[[-1, 0, 1], [0, -1, 1], [1, 1, 0]], scaled=True)
atoms.calc = EMT()

# Relax structure (remove residual forces)
from ase.optimize import BFGS
BFGS(atoms, trajectory='cu.traj').run(fmax=0.01)

# Compute vibrational frequencies
vib = Vibrations(atoms, name='cu_vib')
vib.run()
freqs = vib.get_frequencies()          # in cm-1
vib.imag_modes.log_summary()           # optional: report imaginary modes

# Get harmonic thermo (requires vibrational energies in eV)
vib_energies = vib.get_energies()      # in eV
thermo = HarmonicThermo(vib_energies=vib_energies, atoms=atoms,
                        geometry='nonlinear', symmetrynumber=1, spin=0)

# Helmholtz free energy at T=300 K, P=0 (ideal gas reference)
A = thermo.get_helmholtz_energy(temperature=300.0)
print(f'Helmholtz free energy at 300 K: {A:.6f} eV')
