from ase.build import molecule
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations

atoms = molecule('H2O')
atoms.set_calculator(EMT())

vib = Vibrations(atoms, delta=0.01, nfree=2)
vib.run()
vib.summary()

eV_to_cm = 8065.5
freqs_eV = vib.get_frequencies()

print("\nVibrational mode frequencies:")
for i, f in enumerate(freqs_eV):
    print(f"Mode {i+1}: {f * eV_to_cm:.2f} cm⁻¹  {f:.4f} eV")
