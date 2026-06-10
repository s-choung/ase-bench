import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase import units

# Build 3x3x3 Cu FCC supercell
atoms = bulk('Cu', 'fcc', a=3.615) * (3, 3, 3)
atoms.calc = EMT()

# Target pressure in eV/Å³ (1 bar ≈ 6.2415e-7 eV/Å³)
pressure_eV_A3 = 1.0 * 6.2415e-7

# Print initial state
def get_pressure(atoms):
    """Convert virial stress to pressure (3D average)."""
    stress = atoms.get_stress()  # [xx, yy, zz, yz, xz, xy]
    return -np.mean(stress[:3])  # -trace/3 in eV/Å³

init_vol = atoms.get_volume()
init_press = get_pressure(atoms)
print(f"Initial cell volume: {init_vol:.4f} Å³")
print(f"Initial pressure: {init_press / 6.2415e-7:.2f} bar")

# Run NPT MD
dyn = NPTBerendsen(
    atoms,
    timestep=5 * units.fs,
    temperature_K=300,
    pressure_ambient=pressure_eV_A3,
    taut=100 * units.fs,
    taup=1000 * units.fs,
)
dyn.run(steps=200)

# Print final state
final_vol = atoms.get_volume()
final_press = get_pressure(atoms)
print(f"Final cell volume: {final_vol:.4f} Å³")
print(f"Final pressure: {final_press / 6.2415e-7:.2f} bar")
