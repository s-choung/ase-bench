from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase import units

# Convert 10 GPa to eV/Ang^3
P_GPa = 10.0
P_eVA3 = P_GPa / 160.2176634

# Build 2x2x2 FCC Al supercell
atoms = bulk('Al', 'fcc', a=4.05, cubic=True) * (2, 2, 2)
atoms.calc = EMT()

print(f"Initial volume: {atoms.get_volume():.4f} Ang^3")

# Setup NPT Berendsen MD
md = NPTBerendsen(
    atoms,
    timestep=5 * units.fs,
    temperature=500,             # K
    pressure=P_eVA3,             # eV/Ang^3
    taut=500 * units.fs,         # Temperature coupling time
    taup=5000 * units.fs,        # Pressure coupling time
    compressibility=0.013        # Approx compressibility of Al in GPa^-1
)

# Run MD
md.run(steps=100)

print(f"Final volume: {atoms.get_volume():.4f} Ang^3")
