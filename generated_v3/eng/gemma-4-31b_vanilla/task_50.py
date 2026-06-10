import numpy as np
from ase.build import bulk
from ase.eos import EquationOfState
from ase.calculators.emt import EMT

metals = {'Cu': 3.61, 'Ag': 4.09, 'Au': 4.08}
results = []

for symbol, a_ref in metals.items():
    volumes = []
    energies = []
    
    # Sample volumes around the reference lattice constant (approx +/- 10%)
    for scale in np.linspace(0.9, 1.1, 7):
        atoms = bulk(symbol, 'fcc', a=a_ref * scale)
        atoms.set_calculator(EMT())
        volumes.append(atoms.get_volume())
        energies.append(atoms.get_potential_energy())

    eos = EquationOfState(volumes, energies)
    a0 = eos.a0**(1/3) # Correcting for volume to length
    # ASE EquationOfState returns a0 as the equilibrium volume V0
    v0 = eos.a0
    B0 = eos.B0
    a_eq = v0**(1/3) * (1.0) # Since it's 1 atom per unit cell in bulk() usually, but let's be precise:
    # For FCC bulk(symbol, 'fcc'), the cell contains 4 atoms.
    # Volume of FCC cell = 4 * atomic volume.
    a_eq = (v0 / 1)**(1/3) # bulk('Cu', 'fcc') returns 1 atom cell by default if not specified
    # Re-calculating a_eq based on volume of the specific cell used
    # Let's use the EOS a0 as the equilibrium volume of the simulation cell.
    # If atoms = bulk('Cu', 'fcc'), atoms.get_volume() is for a cell with 1 atom.
    a_eq = v0**(1/3) 
    
    results.append((symbol, a_eq, B0))

print(f"{'Metal':<6} | {'a0 (Å)':<10} | {'B0 (eV/Å³)':<12}")
print("-" * 32)
for res in results:
    print(f"{res[0]:<6} | {res[1]:<10.4f} | {res[2]:<12.4f}")
