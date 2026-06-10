import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
from ase.units import kJ

# List of metals
metals = ['Cu', 'Ag', 'Au']
results = {}

for metal in metals:
    # Create FCC bulk structure
    atoms = bulk(metal, crystalstructure='fcc', a=4.0, cubic=True)
    atoms.calc = EMT()
    
    # Generate lattice constants around expected equilibrium
    if metal == 'Cu':
        a_values = np.linspace(3.5, 4.0, 10)
    elif metal == 'Ag':
        a_values = np.linspace(3.8, 4.3, 10)
    else:  # Au
        a_values = np.linspace(3.8, 4.3, 10)
    
    volumes = []
    energies = []
    
    for a in a_values:
        atoms.set_cell([a, a, a], scale_atoms=True)
        volumes.append(atoms.get_volume())
        energies.append(atoms.get_potential_energy())
    
    # Fit equation of state
    eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
    v0, e0, B = eos.fit()
    
    # Calculate lattice constant from equilibrium volume (FCC: V = a³ for conventional cell)
    a0 = v0**(1/3)
    # Convert bulk modulus from eV/Å³ to GPa
    B_GPa = B * 160.21766208
    
    results[metal] = (a0, B_GPa)

# Print comparison table
print("Metal  Equilibrium a (Å)  Bulk Modulus (GPa)")
print("---------------------------------------------")
for metal in metals:
    a0, B = results[metal]
    print(f"{metal:4s}  {a0:.3f}               {B:.1f}")
