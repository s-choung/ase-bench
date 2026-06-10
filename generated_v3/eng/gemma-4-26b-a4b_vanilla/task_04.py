from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS

# Define H2O molecule (approximate geometry)
# Note: EMT is a metal potential, but requested per instructions
h2o = Atoms('H2O', 
            positions=[[0.0, 0.0, 0.0], 
                       [0.0, 0.75, 0.5], 
                       [0.0, -0.75, 0.5]])

h2o.calc = EMT()

energy_before = h2o.get_potential_energy()
print(f"Energy before optimization: {energy_before:.6f} eV")

# Optimize geometry using BFGS
opt = BFGS(h2o)
opt.run(fmax=0.01)

energy_after = h2o.get_potential_energy()
print(f"Energy after optimization: {energy_after:.6f} eV")
