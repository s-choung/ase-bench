from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

# N2 molecule
atoms = Atoms('N2', [(0,0,0), (0,0,1.1)] * Atoms.unitcell, pbc=False)
atoms.calc = EMT()

# Optimize geometry
BFGS(atoms).run(fmax=0.05)

# Harmonic vibrations (must use a fully optimized structure)
vib = Vibrations(atoms, name='vib')
vib.run()
# frequencies are returned in cm⁻¹
print("Vibrational frequencies (cm⁻¹):", vib.frequencies())
