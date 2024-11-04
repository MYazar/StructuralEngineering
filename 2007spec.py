import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd  # Pandas kütüphanesini ekliyoruz

# Local Soil Class Table (for 2007 Earthquake Regulation)
soil_classes = {
    'Z1': {'TA': 0.10, 'TB': 0.30},
    'Z2': {'TA': 0.15, 'TB': 0.40},
    'Z3': {'TA': 0.15, 'TB': 0.60},
    'Z4': {'TA': 0.20, 'TB': 0.90}
}

# Get soil class and A0 value from the user
soil_class = input("Enter soil class (Z1, Z2, Z3, Z4): ")
A0_input = input("Enter A0 value (will be set to 0.4 if left blank): ")
A0 = float(A0_input) if A0_input else 0.4

# Get I value from the user
I_input = input("Enter I value: ")
I = float(I_input)

# Determine TA and TB values based on the selected soil class
TA = soil_classes[soil_class]['TA']
TB = soil_classes[soil_class]['TB']

# T values
T1 = np.linspace(0, TA, 100)  # 0 < T < TA
T2 = np.linspace(TA, TB, 100)  # TA < T < TB
T3 = np.linspace(TB, 6, 100)  # TB < T

# Calculate S(T)
S_T1 = 1 + 1.5 * T1 / TA
S_T2 = np.full_like(T2, 2.5)
S_T3 = 2.5 * (TB / T3) ** 0.8

# Calculate Sae(T)
Sae_T1 = A0 * I * S_T1
Sae_T2 = A0 * I * S_T2
Sae_T3 = A0 * I * S_T3

# Plot S(T) and Sae(T)
plt.figure(figsize=(10, 6))
plt.plot(T1, S_T1, label='S(T) = 1 + 1.5T/TA', color='blue')
plt.plot(T2, S_T2, label='S(T) = 2.5', color='orange')
plt.plot(T3, S_T3, label='S(T) = 2.5*(TB/T)^0.8', color='green')

plt.plot(T1, Sae_T1, label='Sae(T) = A0 * I * S(T) (0 < T < TA)', linestyle='--', color='blue')
plt.plot(T2, Sae_T2, label='Sae(T) = A0 * I * S(T) (TA < T < TB)', linestyle='--', color='orange')
plt.plot(T3, Sae_T3, label='Sae(T) = A0 * I * S(T) (TB < T)', linestyle='--', color='green')

plt.title('T-S(T) and T-Sae(T)')
plt.xlabel('T (s)')
plt.ylabel('Acceleration (g)')
plt.xlim(0, 6)
plt.ylim(0, max(max(S_T1), max(S_T2), max(S_T3), max(Sae_T1), max(Sae_T2), max(Sae_T3)) * 1.1)
plt.legend()
plt.grid()
plt.show()

# Create a DataFrame to save T, S(T), and Sae(T) values
T_values = np.concatenate((T1, T2, T3))
S_T_values = np.concatenate((S_T1, S_T2, S_T3))
Sae_T_values = np.concatenate((Sae_T1, Sae_T2, Sae_T3))

# Create a DataFrame
data = pd.DataFrame({
    'T (s)': T_values,
    'S(T)': S_T_values,
    'Sae(T)': Sae_T_values
})

# Save to CSV
data.to_csv('T_S_T_and_Sae_T_values.csv', index=False)
print("CSV file 'T_S_T_and_Sae_T_values.csv' created successfully.")
