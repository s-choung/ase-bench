from ase import Atoms
from ase.atom import Atom
from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS, FrechetCellFilter
from ase.vibrations import Vibrations

# build CH4 with appropriate input xyz file
ch4 = molecule('CH4')

# set EMT calculator (structure will be updated during optimization)
ch4.calc = EMT()

# optimize with cell filter
opt = BFGS(FrechetCellFilter(ch4))
opt.run(fmax=0.02)   # force convergence 0.02 eV/Å

# vibration analysis
vib = Vibrations(ch4, name='vib')
vib.run()

# extract real frequencies
all_freqs = vib.get_frequencies()          # array in cm⁻¹
real_freqs = all_freqs.real[all_freqs.imag == 0]

print('Real vibrational frequencies (cm⁻¹):')
print(real_freqs)
