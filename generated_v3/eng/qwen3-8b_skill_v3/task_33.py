from ase import molecule, EMT, BFGS, Vibrations

atoms = molecule('CH4')
atoms.calc = EMT()
BFGS(atoms).run(fmax=0.01)
vib = Vibrations(atoms)
vib.run()
freqs = vib.get_frequencies()
print("Real vibrational frequencies (cm⁻¹):", freqs.real)
