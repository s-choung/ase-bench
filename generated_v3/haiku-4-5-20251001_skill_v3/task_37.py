from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations
from ase.thermochemistry import IdealGasThermo
from ase import units

# N2 분자 생성
atoms = Atoms('N2', positions=[[0, 0, 0], [0, 0, 1.1]])
atoms.center(vacuum=5.0)
atoms.calc = EMT()

# 구조 최적화
opt = BFGS(atoms)
opt.run(fmax=0.01)
print(f"Optimized N-N distance: {atoms.get_distance(0, 1):.4f} Å")

# 진동 주파수 계산
vib = Vibrations(atoms, name='vib_n2')
vib.run()
vib_energies = vib.get_energies()
vib_freqs = vib.get_frequencies()

print(f"\nVibrational frequencies (cm⁻¹):")
for i, freq in enumerate(vib_freqs):
    print(f"  Mode {i}: {freq:.2f} cm⁻¹")

# Gibbs 자유에너지 계산
thermo = IdealGasThermo(vib_energies=vib_energies, atoms=atoms,
                        geometry='linear', symmetrynumber=2, spin=0)
G = thermo.get_gibbs_energy(temperature=298.15, pressure=101325)
H = thermo.get_enthalpy(temperature=298.15)
S = thermo.get_entropy(temperature=298.15, pressure=101325)

print(f"\nThermochemistry at 298.15 K, 1 atm:")
print(f"  Enthalpy (H): {H:.4f} eV")
print(f"  Entropy (S): {S:.6f} eV/K")
print(f"  Gibbs Free Energy (G): {G:.4f} eV")

vib.clean()
