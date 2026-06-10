from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

# Create CH4 molecule
atoms = Atoms('CH4', positions=[(0, 0, 0),
                                (0.628, 0.628, 0.628),
                                (-0.628, -0.628, 0.628),
                                (-0.628, 0.628, -0.628),
                                (0.628, -0.628, -0.628)])

# Set calculator
atoms.calc = EMT()

# Optimize geometry
opt = BFGS(atoms, trajectory='opt.traj')
opt.run(fmax=0.01)

# Calculate vibrations
vib = Vibrations(atoms, name='vib')
vib.run()
vib_energies = vib.get_energies()

# Print only real frequencies
real_frequencies = [freq for freq in vib_energies if freq > 0]
print("Real vibrational frequencies (meV):", sorted(real_frequencies))
