import numpy as np
from ase import Atoms
from ase.calculators.emt import EMT

# Build H₂O geometry (optimized coordinates, arbitrary scaling)
coords = np.array([
    [-0.9572,  0.2771,  0.0000],   # O
    [ 0.0000, -0.0746, -0.6640],   # H1
    [ 0.0000, -0.0746,  0.6640]    # H2
])

water = Atoms('H2O', positions=coords, cell=(4., 4., 4.), pbc=False)
water.set_cell((4., 4., 4.), scale_atoms=True)

calc = EMT()
water.set_calculator(calc)

# Harmonic vibrational analysis – returns frequencies (THz) and force constants
freqs_thz, fc = water.calculators[0].harmonic_analysis()

# Convert to required units
freqs_cm = freqs_thz * 100  # cm^-1 (1 THz = 100 cm^-1)
energies_ev = (freqs_thz * h / (2*np.pi)) * 1.23984193e-4  # eV
h = 6.62607015e-34  # Planck constant in J·s

print('Vibrational mode frequencies (cm⁻¹):')
for i, w in enumerate(water):
    if i != water.periodic_images[w]:
        print(f'  {i} - {freqs_cm[i]:.2f} cm⁻¹')
print('\nTotal vibrational energy (eV):')
print(f'{energies_ev:.4f} eV')
