from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize.precon import PreconLBFGS

# Build Ni FCC conventional unit cell and create 3x3x3 supercell
ni_bulk = bulk('Ni', 'fcc', a=3.52, cubic=True) * (3, 3, 3)

# Set up calculator with precon='auto'
calc = EMT(precon='auto')
ni_bulk.calc = calc

# Optimize structure
opt = PreconLBFGS(ni_bulk, logfile='opt.log')
opt.run(fmax=0.01)

# Extract results
nsteps = opt.get_number_of_steps()
energy = ni_bulk.get_potential_energy()
cell = ni_bulk.cell.cellpar()

print(f"Number of steps: {nsteps}")
print(f"Final energy: {energy:.4f} eV")
print(f"Cell parameters: a={cell[0]:.3f} Å, b={cell[1]:.3f} Å, c={cell[2]:.3f} Å, "
      f"α={cell[3]:.1f}°, β={cell[4]:.1f}°, γ={cell[5]:.1f}°")
