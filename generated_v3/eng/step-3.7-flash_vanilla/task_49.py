from ase.build import bulk, fcc111
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
from ase.optimize import BFGS
from ase.constraints import FixAtoms

# Calculate equilibrium FCC Cu lattice constant via EOS
a_scan = [3.3 + 0.05 * i for i in range(15)]
V, E = [], []
for a in a_scan:
    cu_bulk = bulk('Cu', 'fcc', a=a)
    cu_bulk.calc = EMT()
    V.append(cu_bulk.get_volume())
    E.append(cu_bulk.get_potential_energy())
a_eq = EquationOfState(V, E).fit()[0] ** (1/3)

# Build and relax (111) 4-layer slab
slab = fcc111('Cu', size=(1,1,4), a=a_eq, vacuum=10.0)
slab.sort('z')
n_fixed = len(slab) // 2
slab.set_constraint(FixAtoms(mask=[True]*n_fixed + [False]*(len(slab)-n_fixed)))
slab.calc = EMT()
BFGS(slab).run(fmax=0.05)

# Output results
print(f"Final slab energy: {slab.get_potential_energy():.4f} eV")
print("Average z-coordinate per layer (Å):")
for i in range(4):
    layer = slab[i*(len(slab)//4) : (i+1)*(len(slab)//4)]
    print(f"Layer {i+1}: {layer.positions[:,2].mean():.4f}")
