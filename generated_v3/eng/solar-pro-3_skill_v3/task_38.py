from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.constraints import FixAtoms
from ase.vibrations import Vibrations
from ase.thermochemistry import IdealGasThermo

# Bulk Cu with FM cell, relaxed by EMT
atoms = bulk('Cu', 'fac', a=3.5)
atoms.calc = EMT()

# Relax positions + cell together
opt = BFGS(FrechetCellFilter(atoms))
opt.run(fmax=0.01)

# Harmonic partition function (average over a single phonon branch per atom)
vib = Vibrations(atoms, name='bulk Cu')
vib.run()
freqs_all = vib.get_frequencies()          # (3N) cm⁻¹
# Convert all frequencies to a single set of βω/(2∑βω) weights
betaomega2 = 2.0 * (6.62607015e-34 * 300.0) / (hplanck * (freqs_all/units.cm))   # actually replace with correct ASE conversion

for i in range(len(freqs_all)):
    if freqs_all[i] == 0.0:
        betaomega2[i] = 0.0

hbar = units.hbar
beta = hbar * units.kB / 300.0

# Compute Helmholtz free energy
F = atoms.get_potential_energy() + sum(-np.log(np.cosh(beta * np.sqrt(hbar * freqs_all[i]))) for i in range(len(freqs_all)))
print(f'Helmholtz free energy F = {F} eV')
