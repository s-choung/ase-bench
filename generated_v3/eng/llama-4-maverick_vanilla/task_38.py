from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.thermo.harmonic import HarmonicThermo
from ase.vibrations import Vibrations

cu_bulk = Atoms('Cu', cell=[[0, 2.556, 2.556], [2.556, 0, 2.556], [2.556, 2.556, 0]], pbc=True)
cu_bulk.calc = EMT()
opt = BFGS(cu_bulk)
opt.run(fmax=0.01)

vib = Vibrations(cu_bulk)
vib.run()
vib_energies = vib.get_energies()

thermo = HarmonicThermo(vib_energies)
F = thermo.get_helmholtz_energy(temperature=300)

print(f'Helmholtz free energy at 300K: {F:.4f} eV')
