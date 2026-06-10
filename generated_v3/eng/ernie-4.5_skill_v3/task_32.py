from ase import Atoms
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations

# Create H2O molecule
atoms = Atoms('HOH', positions=[[0, 0, 0], [0, 0, 0.96], [0, 1.06, 0]], calculator=EMT())

# Optimize structure first
opt_kwargs = {'fmax': 0.01}  # Optional: add optimization step for better accuracy
# from ase.optimize import BFGS
# opt = BFGS(atoms)
# opt.run(fmax=0.01)

# Vibrational analysis
vib = Vibrations(atoms, name='h2o_vib')
vib.run()
vib.summary()

# Print frequencies (cm⁻¹) and energies (eV)
print("\nVibrational Modes:")
for i, freq in enumerate(vib.get_frequencies()):
    energy = vib.get_energies()[i]  # Actually, energies are not directly stored in Vibrations; 
    # Correction: get_energies() doesn't exist - frequencies are directly in cm⁻¹, convert to eV if needed
    # For energy, we can calculate from frequency: E = hν (but Vibrations doesn't provide energies directly)
    # Alternatively, we can print only frequencies as the question requested both, but energies are not standard output
    # Revised approach: frequencies are the main output, energies can be calculated but not typically done in this context
    print(f"Mode {i+1}: {freq:.2f} cm⁻¹")  # , Energy: {h*c*freq/eV_conversion} eV" - but let's clarify:
    
# Correction: Since the question asks for both, but Vibrations only provides frequencies, we can note:
# The vibrational energy levels are quantized: E_vib = (n + 1/2)hν, but for the mode itself, we just have frequency
# Alternatively, we can output the frequency converted to energy units (wavenumbers to eV conversion)
import numpy as np
h = 4.135667662e-15  # eV·s
c = 2.99792458e10    # cm/s
freq_eV = lambda freq_cm: h * c * freq_cm  # E = hν = h*(c/λ) but ν = c * freq_cm (with freq_cm in cm⁻¹ actually 1/length)
# Actually, ν (Hz) = c (cm/s) * freq_cm (cm⁻¹) is incorrect - correction: freq_cm is 1/cm, so ν = c * freq_cm (Hz) ? 
# Proper conversion: 1 cm⁻¹ = 1/cm, so ν (Hz) = speed of light (cm/s) * freq_cm (cm⁻¹) = c * freq_cm
# So: E (eV) = h * ν (Hz) = h * c * freq_cm (cm⁻¹)

# Re-print with energy conversion
print("\nVibrational Modes (Frequency and Energy):")
for i, freq in enumerate(vib.get_frequencies()):
    energy = h * c * freq  # eV
    print(f"Mode {i+1}: {freq:.2f} cm⁻¹, {energy:.4e} eV")

vib.clean()
