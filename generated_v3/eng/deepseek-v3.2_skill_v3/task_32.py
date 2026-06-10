from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

# Build water molecule
atoms = Atoms('OH2', positions=[[0, 0, 0], [0.957, 0, -0.25], [-0.957, 0, -0.25]])
atoms.calc = EMT()

# Optimize geometry first
opt = BFGS(atoms, trajectory='opt.traj')
opt.run(fmax=0.01)

# Calculate vibrations
vib = Vibrations(atoms, name='water_vib')
vib.run()

# Get frequencies and energies
freqs = vib.get_frequencies()
energies = vib.get_energies()

# Print results
for i, (freq, energy) in enumerate(zip(freqs[-3:], energies[-3:])):
    if freq > 0:
        print(f"Mode {i+1}: {freq:.2f} cm^-1, {energy:.4f} eV")

vib.clean()
