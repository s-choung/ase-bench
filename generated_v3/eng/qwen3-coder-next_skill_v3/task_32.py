from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

# Create water molecule
atoms = Atoms('H2O', positions=[[0.75, 0.0, 0.0], [-0.75, 0.0, 0.0], [0.0, 0.0, 0.0]])
atoms.calc = EMT()

# Optimize geometry
BFGS(atoms).run(fmax=0.01)

# Calculate vibrations
vib = Vibrations(atoms, name='h2o_vib')
vib.run()

# Print frequencies and energies
for mode, (freq, energy) in enumerate(zip(vib.get_frequencies(), vib.get_energies())):
    print(f"Mode {mode+1}: {freq:.2f} cm^-1, {energy:.6f} eV")

vib.clean()
