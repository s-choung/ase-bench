import numpy as np
from ase import Atoms, units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen

# Build Cu FCC 3×3×3 supercell
a = 3.615  # Å, approximate lattice constant for Cu
atoms = bulk('Cu', 'fcc', a=a) * (3, 3, 3)

# Attach EMT calculator
atoms.set_calculator(EMT())

# Helper to compute pressure (GPa) from stress tensor (eV/Å³)
def pressure_gpa(atoms):
    stress = atoms.get_stress()               # eV/Å³
    return -np.trace(stress) / 3.0 * 160.21766208  # GPa

# Initial properties
V0 = atoms.get_volume()
P0 = pressure_gpa(atoms)
print(f"Initial volume: {V0:.3f} Å³, pressure: {P0:.3f} GPa")

# NPT Berendsen dynamics
dyn = NPTBerendsen(atoms,
                    timestep=5 * units.fs,
                    temperature_K=300,
                    pressure_St=1,
                    taut=100 * units.fs,
                    taup=1000 * units.fs)

# Run 200 steps
for _ in range(200):
    dyn.run(1)

# Final properties
Vf = atoms.get_volume()
Pf = pressure_gpa(atoms)
print(f"Final volume: {Vf:.3f} Å³, pressure: {Pf:.3f} GPa")
