from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.filters import FrechetCellFilter
from ase.vibrations import Vibrations
from ase.thermochemistry import HarmonicThermo

atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()
opt = BFGS(FrechetCellFilter(atoms))
opt.run(fmax=0.01)

vib = Vibrations(atoms, name='cu_vib')
vib.run()
vib_energies = vib.get_energies()
vib.clean()

mask = vib_energies.real > 1e-5
thermo = HarmonicThermo(vib_energies[mask])
F_vib = thermo.get_helmholtz_energy(temperature=300)

F_total = atoms.get_potential_energy() + F_vib
print(f'Helmholtz free energy at 300 K: {F_total:.6f} eV')
