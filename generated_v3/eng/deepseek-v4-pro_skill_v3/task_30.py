import numpy as np
from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary, ZeroRotation
from ase.constraints import FixAtoms

def pressure_bar(atoms):
    """Convert stress tensor to hydrostatic pressure in bar."""
    stress = atoms.get_stress()  # 3x3 or 6-component array in eV/Å³
    if stress is None:
        return None
    # Hydrostatic pressure = -trace/3
    p = -np.trace(stress.reshape(3, 3)) / 3
    # 1 eV/Å³ ≈ 1.602e6 bar
    return p * 1.602176634e6

# Build Cu fcc 3x3x3 supercell
a = 3.6  # lattice constant in Å
cu = bulk('Cu', 'fcc', a=a, cubic=True) * (3, 3, 3)
cu.calc = EMT()

# Initial velocities for 300 K
MaxwellBoltzmannDistribution(cu, temperature_K=300)
Stationary(cu)      # remove center-of-mass translation
ZeroRotation(cu)

# NPT parameters
comp = 1.0 / (140 * units.GPa)  # compressibility (Cu bulk modulus ~140 GPa)
npt = NPTBerendsen(cu,
                   timestep=5 * units.fs,
                   temperature_K=300,
                   taut=100 * units.fs,
                   taup=1000 * units.fs,
                   pressure=1 * units.bar,
                   compressibility=comp)

# Print initial state
vol0 = cu.get_volume()
p0 = pressure_bar(cu)
print(f"Initial volume: {vol0:.3f} Å³, pressure: {p0:.2f} bar")

# Run 200 steps
npt.run(200)

# Print final state
vol1 = cu.get_volume()
p1 = pressure_bar(cu)
print(f"Final volume:   {vol1:.3f} Å³, pressure: {p1:.2f} bar")
