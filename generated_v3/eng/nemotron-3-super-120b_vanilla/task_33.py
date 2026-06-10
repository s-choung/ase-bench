from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

# Build methane molecule (tetrahedral geometry)
atoms = Atoms('CH4',
              positions=[[0.0, 0.0, 0.0],   # C
                         [0.63, 0.63, 0.63],  # H1
                         [-0.63, -0.63, 0.63], # H2
                         [-0.63, 0.63, -0.63], # H3
                         [0.63, -0.63, -0.63]]) # H4

# Attach EMT calculator
atoms.calc = EMT()

# Optimize geometry
opt = BFGS(atoms)
opt.run(fmax=0.01)  # converge forces to 0.01 eV/Å

# Vibrational analysis
vib = Vibrations(atoms)
vib.run()
freqs = vib.get_frequencies()

# Print only real (positive) frequencies in cm^-1
real_freqs = sorted(f for f in freqs if f > 0)
for f in real_freqs:
    print(f'{f:.2f} cm^-1')
