from ase.build import molecule
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations

atoms = molecule('H2O')
atoms.calc = EMT()
vib = Vibrations(atoms)
vib.run()

freqs = vib.get_frequencies()
energies = vib.get_energies()

for i, (f, e) in enumerate(zip(freqs, energies), 1):
    print(f"Mode {i}: {f:.1f} cm⁻¹, {e:.4f} eV")
