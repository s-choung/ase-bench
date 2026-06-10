from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import FIRE
from ase.vibrations import Vibrations
from ase.thermochemistry import IdealGasThermo

# N2 molecule initialization
n2 = Atoms('N2', positions=[[0, 0, 0], [1.1, 0, 0]])
n2.calc = EMT()

# Structure optimization
FIRE(n2).run(fmax=1e-6)

# Vibrational frequency calculation
vib = Vibrations(n2)
vib.run()
vib_freqs = vib.get_frequencies()

# Thermodynamic calculation
thermo = IdealGasThermo(
    energy=n2.get_potential_energy(),
    vib_frequencies=vib_freqs,
    geometry='linear',
    symmetrynumber=2,
    atoms=n2,
    temperature=298.15,
    pressure=101325
)

# Print Gibbs free energy
print(thermo.gibbs_free_energy())
