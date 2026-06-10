from ase.build import bulk
from ase.eos import EquationOfState
from ase import atoms
import numpy as np

# EMT calculator
calc = EMT()

# Metals to study
metals = {
    "Cu": {"symbol": "Cu", "tag": "Copper"},
    "Ag": {"symbol": "Ag", "tag": "Silver"},
    "Au": {"symbol": "Au", "tag": "Gold"},
}

# Parameters
box_factor = 1.05   # 5% expansion beyond ideal cell
num_samples = 7
eos_type = "birchmurnaghan"

for sym, meta in metals.items():
    # Create bulk, set calculator, identical cell
    bulk_all = bulk(meta["symbol"], "fcc", cubic=True)
    bulk_all.calc = calc
    bulk_all.set_cell_sc()  # unit cell

    # collect data
    volumes = []
    energies = []
    tags = []
    for scale in np.linspace(0.95, box_factor, num_samples):
        a = bulk_all.copy()
        a.set_cell(bulk_all.get_cell() * scale, scale_atoms=True)
        a.calc = calc
        volumes.append(a.get_volume())
        energies.append(a.get_potential_energy())
        tags.append(a.get_tags()[0])   # store original cell tag

    # fit EOS
    eos = EquationOfState(volumes, energies, eos=eos_type)

    # equilibrium volume / lattice constant
    vol0 = eos.volume0
    # reconstructed lattice constant at zero pressure
    vol9 = eos.volumes[9]   # linear interpolation yields ~ r=0.9 ≈ original a
    a9 = vol9 ** (1/3)
    # bulk modulus at equilibrium (slope ~ B0)
    bdef = np.array(eos.bmatrix[:, 0])   # fractional volume change matrix
    b = np.abs(np.gradient(eos.b0, vol0))   # integer volume change

    # extract original tag
    orig_tag = tags[0]

    print("\n===", meta["tag"], "===")
    print(f"   a (Å): {a9:.4f}")
    print(f"   B0 (eV/Å³): {b/units.Å**3:.2f}")
    print(f"   B0 (GPa):   {b * 4.39e-9/units.Å**3:.0f}")   # 1 GPa = 4.39e-9 eV/Å³
    print(f"   \u03b2 (Grimme): {bdef[2]:.3f}")
