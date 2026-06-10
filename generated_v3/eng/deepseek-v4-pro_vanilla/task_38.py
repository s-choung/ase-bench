from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.constraints import ExpCellFilter
from ase.vibrations import Vibrations
from ase.thermochemistry import HarmonicThermo

# Set up and relax a primitive copper cell
prim = bulk('Cu', 'fcc', a=3.6)
prim.calc = EMT()
opt = BFGS(ExpCellFilter(prim))
opt.run(fmax=0.01)

# Build a 2x2x2 supercell for vibrational analysis
atoms = prim * (2, 2, 2)
atoms.calc = EMT()

# Compute vibrational energies via finite differences
vib = Vibrations(atoms, name='vib', delta=0.01)
vib.run()
all_energies = vib.get_energies()

# Filter out acoustic (near-zero) modes
vib_energies = all_energies[all_energies > 1e-5]

# Get the static potential energy of the relaxed supercell
potential_energy = atoms.get_potential_energy()

# Helmholtz free energy at 300 K
thermo = HarmonicThermo(vib_energies=vib_energies,
                        potentialenergy=potential_energy)
F = thermo.get_helmholtz_energy(300.0)

print(f"Helmholtz free energy at 300 K: {F:.6f} eV")
