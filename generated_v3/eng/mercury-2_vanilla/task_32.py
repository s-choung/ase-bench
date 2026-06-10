from ase import Atoms
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations

# H2O geometry (Å)
atoms = Atoms('H2O',
              positions=[(0.0, 0.0, 0.0),          # O
                         (0.757, 0.586, 0.0),      # H
                         (-0.757, 0.586, 0.0)],    # H
              calculator=EMT())

# finite‑displacement vibrational analysis
vib = Vibrations(atoms, delta=0.01)   # Å
vib.run()
freq_thz = vib.get_frequencies()      # THz (3 N values)

# constants
THZ_TO_CM1 = 33.35641                # 1 THz = 33.35641 cm⁻¹
CM1_TO_EV = 1.239841984e-4           # hc in eV·cm

print("Mode  Frequency (cm⁻¹)   Energy (eV)")
for i, f in enumerate(freq_thz):
    if f < 1e-3:          # ignore near‑zero (trans/rot) modes
        continue
    cm1 = f * THZ_TO_CM1
    ev = cm1 * CM1_TO_EV
    print(f"{i+1:>4}  {cm1:>13.2f}  {ev:>10.4f}")

vib.clean()
