from ase import units
from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations
from ase.thermochemistry import IdealGasThermo

# Create N2 molecule
atoms = molecule('N2')
atoms.calc = EMT()

# Optimize geometry
BFGS(atoms).run(fmax=0.01)

# Run vibrational analysis
vib = Vibrations(atoms, name='vib_n2')
vib.run()
vib_energies = vib.get_energies()

# Compute Gibbs free energy
thermo = IdealGasThermo(vib_energies=vib_energies[:-5],  # Exclude 5 lowest modes (3 trans, 2 rot)
                        atoms=atoms,
                        geometry='linear',
                        symmetrynumber=2,
                        spin=0)
G = thermo.get_gibbs_energy(temperature=298.15, pressure=101325)
print(G)

# Clean up
vib.clean()
