from ase import Atoms
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
import numpy as np

metals = ['Cu', 'Ag', 'Au']
results = []

for metal in metals:
    # Create FCC bulk structure
    a = 3.6  # approximate lattice constant
    atoms = Atoms(metal, cell=[[0, a/2, a/2], [a/2, 0, a/2], [a/2, a/2, 0]], 
                  pbc=True)
    atoms.calc = EMT()
    
    # Generate volume variations
    volumes = []
    energies = []
    for i in range(9):
        scale = 0.9 + 0.1 * i
        atoms.set_cell(atoms.get_cell() * scale, scale_atoms=True)
        volumes.append(atoms.get_volume())
        energies.append(atoms.get_potential_energy())
    
    # Fit EOS using Murnaghan equation
    eos = EquationOfState(volumes, energies, equation='murnaghan')
    try:
        eos.fit()
        vol_eq = eos.vol_eq
        B = eos.B_eq  # in eV/Å³
        a_eq = (vol_eq * 4) ** (1/3)  # FCC unit cell volume = 4 * (a/2)^3 = a^3/4
        
        # Convert bulk modulus to GPa (1 eV/Å³ = 160.21766208 GPa)
        B_GPa = B * 160.21766208
        
        results.append([metal, a_eq, B_GPa])
    except:
        results.append([metal, np.nan, np.nan])

# Print results table
print("=" * 50)
print(f"{'Metal':<8} {'a (Å)':<12} {'B (GPa)':<12}")
print("=" * 50)
for result in results:
    if np.isnan(result[1]):
        print(f"{result[0]:<8} {'---':<12} {'---':<12}")
    else:
        print(f"{result[0]:<8} {result[1]:<12.3f} {result[2]:<12.1f}")
print("=" * 50)
