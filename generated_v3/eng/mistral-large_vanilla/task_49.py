from ase.build import bulk, fcc111
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
from ase.optimize import BFGS
from ase.constraints import FixAtoms

# Find equilibrium lattice constant
cu_bulk = bulk('Cu', 'fcc', a=3.6, cubic=True)
cu_bulk.calc = EMT()
cell = cu_bulk.get_cell()
volumes, energies = [], []
for x in [0.95, 0.97, 0.99, 1.0, 1.01, 1.03, 1.05]:
    cu = cu_bulk.copy()
    cu.set_cell(cell * x, scale_atoms=True)
    cu.calc = EMT()
    energies.append(cu.get_potential_energy())
    volumes.append(cu.get_volume())
eos = EquationOfState(volumes, energies)
v0, e0, B = eos.fit()
a0 = (4 * v0)**(1/3)

# Create slab and relax
slab = fcc111('Cu', a=a0, size=(1, 1, 4), vacuum=10)
slab.calc = EMT()
fix = FixAtoms(indices=[a.index for a in slab if a.tag in [3, 4]])
slab.set_constraint(fix)
opt = BFGS(slab)
opt.run(fmax=0.01)

# Print results
print(f"Final energy: {slab.get_potential_energy():.3f} eV")
for tag in range(1, 5):
    z = [a.z for a in slab if a.tag == tag]
    print(f"Layer {tag} avg z: {sum(z)/len(z):.3f} Å")
