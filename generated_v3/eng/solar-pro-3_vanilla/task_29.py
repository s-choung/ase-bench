import ase
from ase.calculators.emt import EMT
from ase.calculators.lj import LennardJones
from ase.md.velocitydistribution import velocitydistribution
from ase.md.verlet import VelocityVerlet
from ase.md import MDAnalysisWriter

# Build FCC 2x2x2 Pd supercell
a, Z = 3.9, 4      # conventional FCC lattice constant (Å) and atoms per cell
N = 4 * (2**3)    # 16 Pd atoms
atoms = ase.build.bulk('Pd', 'fcc', a=a)
atoms *= (2, 2, 2)          # supercell
atoms.set_cell(atoms.cell.array, scale_atoms=True)

# Set initial velocities for T = 500 K
atoms.center(vacuum=10.0, axis=2)
velocitydistribution(atoms, 500.0, 'Maxwell')

# Use EMT calculator (built‑in)
atoms.set_calculator(EMT())

# Compute analytical forces once
atoms.get_forces()

# NVE Velocity Verlet integrator
dyn = VelocityVerlet(atoms, 2.0)   # timestep = 2 fs
energies = []
for i in range(200):
    dyn.run(1)
    E = atoms.get_potential_energy() + atoms.get_kinetic_energy()
    energies.append(E)

# Energy conservation
deltaE = energies[-1] - energies[0]
print(f'ΔE = {deltaE:.6f} eV   (relative = {deltaE/energies[0]:.6e})')
