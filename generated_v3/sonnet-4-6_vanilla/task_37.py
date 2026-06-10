from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations
from ase.thermochemistry import IdealGasThermo
import numpy as np

# N2 molecule setup
d = 1.1  # initial N-N bond length in Angstrom
n2 = Atoms('N2', positions=[(0, 0, 0), (0, 0, d)])
n2.calc = EMT()

# Geometry optimization
opt = BFGS(n2, logfile=None)
opt.run(fmax=0.001)

print(f"Optimized N-N bond length: {n2.get_distance(0, 1):.4f} Å")

# Potential energy at optimized geometry
e_pot = n2.get_potential_energy()
print(f"Potential energy: {e_pot:.6f} eV")

# Vibrational analysis
vib = Vibrations(n2, name='vib_n2')
vib.run()
vib.summary()

# Get vibrational energies (in eV)
vib_energies = vib.get_energies()
print(f"\nAll vibrational energies: {vib_energies}")

# Filter real (non-imaginary) frequencies for thermochemistry
# For linear molecule: 3N-5 = 1 vibrational mode
# But Vibrations gives 3N=6 modes; we need to pick the real ones
real_vib_energies = np.array([e for e in vib_energies if e.imag == 0 and e.real > 0.01])
print(f"Real vibrational energies used: {real_vib_energies} eV")

# IdealGasThermo
thermo = IdealGasThermo(
    vib_energies=real_vib_energies,
    potentialenergy=e_pot,
    atoms=n2,
    geometry='linear',
    symmetrynumber=2,
    spin=0
)

T = 298.15  # K
P = 101325  # Pa (1 atm)

G = thermo.get_gibbs_energy(temperature=T, pressure=P, verbose=True)
H = thermo.get_enthalpy(temperature=T, verbose=False)
S = thermo.get_entropy(temperature=T, pressure=P, verbose=False)
ZPE = thermo.get_ZPE_correction()

print("\n" + "="*50)
print(f"  Temperature : {T} K")
print(f"  Pressure    : {P/101325:.1f} atm")
print(f"  ZPE         : {ZPE:.4f} eV")
print(f"  Enthalpy    : {H:.4f} eV")
print(f"  Entropy*T   : {S*T/1000*96.485:.4f} eV  (S = {S*1000:.4f} meV/K)")
print(f"  Gibbs (G)   : {G:.4f} eV")
print("="*50)

# Cleanup
vib.clean()
