from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen

# Create Al FCC 2x2x2 supercell
atoms = bulk('Al', 'fcc', a=4.05) * (2, 2, 2)
atoms.calc = EMT()

# Conversion: 1 GPa = 1e9 Pa = 1e9 N/m^2
# 1 eV/Ang^3 = 1.60218e-19 J / 1e-30 m^3 = 1.60218e11 Pa = 160.218 GPa
# p_ext = 10 GPa = 10 / 160.218 eV/Ang^3
p_ext = 10 / 160.218  # eV/Ang^3

# NPT Berendsen dynamics
dyn = NPTBerendsen(atoms, timestep=1.0 * units.fs,
                   temperature_K=500,
                   externalstress=p_ext,
                   nsteps=100)

# Print initial cell volume
print(f"Initial volume: {atoms.get_volume():.4f} Ang^3")

# Run dynamics
dyn.run()

# Print final cell volume
print(f"Final volume: {atoms.get_volume():.4f} Ang^3")
