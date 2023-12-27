# Define the equations as functions

# Fractal Dimensionality
def fractal_dimensionality(dS, dT):
    return dS + dT - 1

# Energy Eigenvalues
def energy_eigenvalues(l, μ, r, E0):
    return -((h_bar**2) * l * (l + 1)) / (2 * μ * r**2) - E0

# Coulomb Interaction
def coulomb_interaction(Z1, Z2, r):
    return k * (Z1 * Z2) / (4 * math.pi * ε_0 * r**2)

# Effective Nuclear Charge
def effective_nuclear_charge(m, e, me, ε_0, r):
    return m * (e**2) / (2 * me * ε_0 * r)

# Coulomb's Law
def coulombs_law(q1, q2, r):
    return k * q1 * q2 / (ε_0 * r**2)

# Gravitational Binding Energy
def gravitational_binding_energy(m, M, r):
    return -G * m * M / r

# Define the input values
dS = 2
dT = 1
l = 1
μ = 1
r = 1e-9
E0 = 0
Z1 = 1
Z2 = 1
m = 1
e = 1
me = 1
r = 1e-9
q1 = 1
q2 = 1

# Perform the calculations
Df = fractal_dimensionality(dS, dT)
En = energy_eigenvalues(l, μ, r, E0)
Fcoulomb = coulomb_interaction(Z1, Z2, r)
Q = effective_nuclear_charge(m, e, me, ε_0, r)
F_coulomb = coulombs_law(q1, q2, r)
E_grav = gravitational_binding_energy(m, M, r)

# Print the results
print("Fractal Dimensionality (Df):", Df)
print("Energy Eigenvalues (En):", En)
print("Coulomb Interaction (Fcoulomb):", Fcoulomb)
print("Effective Nuclear Charge (Q):", Q)
print("Coulomb's Law (F_coulomb):", F_coulomb)
print("Gravitational Binding Energy (E_grav):", E_grav)

# Spinor Vortex Condensate
spinor_vortex_condensate = {
    "Core Region": "Rotational Motion",
    "Centrifugal Force": "Annular Region",
    "Axial Velocity Gradient": "Pressure Difference",
    "Driving Tangential Flow": {
        "Outward": "Inward"
    },
    "Unified Field Theory": "2D + 1D = 3D Space-Time Geometry",
    "3-Spatial Dimensions": "1-Temporal Dimension"
}

# Wave Function and Complex Scalar Potential
wave_function = {
    "Complex Scalar Potential": {
        "Angular Momentum": {
            "Spin Orbital Angular Momentum": {
                "Radial Direction": "Tangential Direction"
            }
        }
    }
}

# Quantum Numbers and Electronic Configuration
quantum_numbers = {
    "n": "Principal Quantum Number",
    "l": {
        "L": "Orbital Angular Momentum Quantum Number",
        "mL": "Magnetic Quantum Number"
    },
    "m": "Angular Momentum Quantum Number",
    "ml": "Magnetic Quantum Number",
    "s": "Spin Quantum Number",
    "ms": "Spin Orientation Value",
    "Electronic Configuration": {
        "Electronic Configuration": "2P5 2p6",
        "Electron spin": {
            "up": "↑",
            "down": "↓"
        },
        "Positively Charged Particle": {
            "up": "↑",
            "down": "↓"
        },
        "Negatively Charged Particle": {
            "up": "↑",
            "down": "↓"
        },
        "Hund's Rule": "Electrons occupy orbitals with the same value of L before pairing up. When paired up they have opposite spins.",
        "Aufbau Principle": "Electrons fill lowest-energy orbitals first.",
        "Pauli Exclusion Principle": "No two electrons can have identical values for all four quantum numbers."
    }
}

# Molecular Orbitals, Hybridization, and Molecular Orbital Diagram
molecular_orbitals = {
    "Molecular Orbital Theory": "Valence Bond Theory",
    "Hybridization": {
        "Atomic Orbitals": "Hybridized Atomic Orbitals",
        "sp3": "d-sp2",
        "sp": {
            "sp3d": "spdf",
            "Dspdf": "Hybrid Atomic Orbital Symmetry"
        }
    },
    "SPDF Valence Shell Electronic Configuration": "C-C σ-bonding molecular orbital",
    "π* antibonding molecular orbital": "σ antibonding molecular orbital",
    "π bonding molecular orbital": "Molecular Orbital Diagram",
}

# Ionic Bonds, Ionic Radius Difference, and Coulomb's Law for Ionic Bonds
ionic_bonds = {
    "Ionic Bonds": "Electrostatic Attraction Between Oppositely Charged Ions",
    "Ionic Radius Difference": "ΔRionic radius difference",
    "Coulomb's Law for Ionic Bonds": "r → Distance Between Ions\nZ → Charge on One Ion",
}

# Covalent Bonds and Bond Order
covalent_bonds = {
    "Covalent Bonds": "Sharing of Electrons",
    "Bond Order": "B.O. = #bonded electrons / #valence electrons",
}

# Combine all results
results = {
    "Spinor Vortex Condensate": spinor_vortex_condensate,
    "Wave Function and Complex Scalar Potential": wave_function,
    "Quantum Numbers and Electronic Configuration": quantum_numbers,
    "Molecular Orbitals, Hybridization, and Molecular Orbital Diagram": molecular_orbitals,
    "Ionic Bonds, Ionic Radius Difference, and Coulomb's Law for Ionic Bonds": ionic_bonds,
    "Covalent Bonds and Bond Order": covalent_bonds
}

# Function to recursively process the results

def calculate_equation(value):
      equation = ""
      if isinstance(value, str):
            equation += value
      elif isinstance(value, dict):
       for key in value:
            equation += f" {key}: {calculate_equation(value[key])}"
      else:
        equation += f" {value}"
      
      return equation

recursively process all equations
def process_item(item_dict):

processed_dict = {}

for key, value in item_dict.items():

      if isinstance(value, str): 
      processed_dict[key] = calculate_equation(value)
      
      elif isinstance(value, dict): 
      processed_dict[key] = process_item(value)
      
def process_item(item_dict):
    processed_dict = {}
    for key, value in item_dict.items():
        if isinstance(value, str):
            processed_dict[key] = calculate_equation(value)
        elif isinstance(value, dict):
            processed_dict[key] = process_item(value)
        elif isinstance(value, list):
            processed_list = []
            for item in value:
                if isinstance(item, str):
                    processed_list.append(calculate_equation(item))
                elif isinstance(item, dict):
                    processed_list.append(process_item(item))
            processed_dict[key] = processed_list
    return processed_dict

processed_data = process_item(data)
json_processed_data = json.dumps(processed_data, indent=4)
print(json_processed_data)

    def calculate_equation(value):
        equation = ""
        if isinstance(value, str):
            equation += value
        elif isinstance(value, dict):
            for key in value:
                equation += f" {key}: {calculate_equation(value[key])}"
        else:
            equation += f" {value}"
        
        return equation

recursively process all equations
    def process_item(item_dict):
    
    processed_dict = {}
    
    for key, value in item_dict.items():
    
        if isinstance(value, str): 
            processed_dict[key] = calculate_equation(value)
            
        elif isinstance(value, dict): 
            processed_dict[key] = process_item(value)