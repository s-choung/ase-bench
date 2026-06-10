from ase import molecule
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations

atoms = molecule('H2O')
atoms.calc = EMT()
atoms = atoms.repeat((2, 2, 2))  # workaround to avoid zero-frequency translational/rotational modes in small cells

vib = Vibrations(atoms)
vib.run()
freqs = vib.get_frequencies()
vib.energies  # eV

for mode_idx, (freq, energy) in enumerate(zip(freqs, vib.energies)):
    print(f'Mode {mode_idx}: frequency={freq:.2f} cm-1, energy={energy:.6f} eV')
