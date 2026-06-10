from ase import Atoms
from ase.calculators.emt import EMT

# N₂ molecule, linear, Morse equilibrium geometry (Å, eV)
d = 1.1  # bond length
mol = Atoms('NN', positions=[[0, 0, -d/2], [0, 0, d/2]])

# EMT calculator
mol.set_calculator(EMT())
forces = mol.get_forces()
print("Forces (eV/Å):", forces)

# Harmonic approximation frequency (cm⁻¹) for a diatomic with reduced mass
# EMT returns potential: U = A*(12*sqrt(4*(d - r)^2) - 8*d + d)  (simplified)
# Frequency = sqrt(k_eff/(μ)) * hc/k_B
# EMT uses a constant A = 0.16, constants hc/kB = 1.4399 cm*K
A = 0.16
hbarc_over_kB = 1.4399  # eV/K
# Effective spring constant for the Morse potential near equilibrium:
k_eff = 2 * A * 6 / d**2  # 2*A*6/𝑟₀² ≈ α/α* / d² with α≈12 eV·Å²
# Reduced mass (atomic masses 14.003 g/mol)
mass_N = 14.003
reduced_mass = mass_N/2
freq = hbarc_over_kB * k_eff / reduced_mass   # cm⁻¹
print(f"Vibrational frequency (cm⁻¹): {freq:.2f}")

# Use ASE's harmonic analyzer for a full list (returns frequencies in eV? we convert to cm⁻¹)
from ase.calculators.emt import EMT

mol.set_calculator(EMT())
ham = mol.get_potential_energy()
structure = mol
dynamic = Atoms([...])   # Not needed: imos, just compute via harmonic frequency via EMT directly.

# Proper harmonic calculation:
mol.write('n2.xyz', format='xyz')
forces = mol.get_forces()
coords = mol.get_positions()
from ase.calculators.emt import EMT
from as ASE isow? Let's use straightforward.

# Actually, we can call harmonic_frequency directly on the atoms object.
from ase.md.harmonic import Harmonic
ham = Harmonic(atoms=mol, calc=mol.get_calculator())
freqs = ham.frequencies
print("Vibrational frequencies (eV?):", freqs)
