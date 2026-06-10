from ase.build import bulk
from ase.eos import EquationOfState

# Build Cu fcc bulk with a guess lattice constant
cu = bulk('Cu', 'fcc', a=3.6)          # a is in Å

# Fit the lattice constant around the guess
c = EquationOfState(
    [],                               # initial volume array
    [],                               # initial energy array
    p0=[3.6],                         # initial guess for the lattice constant
    min_atoms=0,
    pressures=np.linspace(0.95, 1.05, 9) * 3.6**3  # dof in Å³? depend on potential implementation
)
