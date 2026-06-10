from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations
import numpy as np

water = Atoms('H2O',
              positions=[[0.757, 0.586, 0.0],
                         [-0.757, 0.586, 0.0],
                         [0.0, 0.0, 0.0]])

water.calc = EMT()

opt = BFGS(water, logfile=None)
opt.run(fmax=0.01)

print("Optimized positions:")
for atom in water:
    print(f"  {atom.symbol}: {atom.position}")

vib = Vibrations(water)
vib.run()
vib.summary()

print("\n--- Vibrational Modes ---")
print(f"{'Mode':>6} {'Frequency (cm^-1)':>20} {'Energy (eV)':>15} {'Type':>10}")
print("-" * 55)

energies = vib.get_energies()
frequencies = vib.get_frequencies()

for i, (freq, energy) in enumerate(zip(frequencies, energies)):
    freq_real = freq.real
    energy_real = energy.real
    mode_type = "imaginary" if freq.imag > 0 else "real"
    if freq.imag > 0:
        freq_display = f"{freq.imag:.2f}i"
    else:
        freq_display = f"{freq_real:.2f}"
    print(f"  {i:>4}  {freq_display:>20} {energy_real:>15.6f}  {mode_type:>10}")

print("\n--- Non-zero Vibrational Modes (last 3) ---")
print(f"{'Mode':>6} {'Frequency (cm^-1)':>20} {'Energy (meV)':>15}")
print("-" * 45)
for i in range(len(frequencies) - 3, len(frequencies)):
    freq = frequencies[i]
    energy = energies[i]
    freq_val = freq.real if freq.imag == 0 else freq.imag
    energy_mev = energy.real * 1000
    print(f"  {i:>4}  {freq_val:>20.2f} {energy_mev:>15.4f} meV")

vib.clean()
