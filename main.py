import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

# Temperature range
x_temp = np.arange(0, 101, 1)

# Fuzzy membership functions
cold = fuzz.trimf(x_temp, [0, 0, 15])  # Cold: 0-15 degrees
chilly = fuzz.trimf(x_temp, [10, 15, 20])  # Chilly: 10-20 degrees
warm = fuzz.trimf(x_temp, [15, 25, 35])  # Warm: 15-35 degrees
hot = fuzz.trimf(x_temp, [30, 60, 100])  # Hot: 30-100 degrees

# Input Temperature
input_temp = 18 

# Calculate fuzzy membership values
cold_degree = fuzz.interp_membership(x_temp, cold, input_temp)
chilly_degree = fuzz.interp_membership(x_temp, chilly, input_temp)
warm_degree = fuzz.interp_membership(x_temp, warm, input_temp)
hot_degree = fuzz.interp_membership(x_temp, hot, input_temp)

# Fuzzy rules - simple example
# Rule: If input is warm and not much chilly, then more towards warm
active_rule = np.fmin(warm_degree, 1 - chilly_degree)  # Example rule

# Defuzzification using centroid method
aggregated = np.fmax(active_rule, np.zeros_like(x_temp))  # Combine the rules
output_temp = fuzz.defuzz(x_temp, aggregated, 'centroid')  # Centroid defuzzification

# Visualization
plt.figure(figsize=(8, 6))

plt.plot(x_temp, cold, 'b', linewidth=1.5, label='Cold')
plt.plot(x_temp, chilly, 'g', linewidth=1.5, label='Chilly')
plt.plot(x_temp, warm, 'r', linewidth=1.5, label='Warm')
plt.plot(x_temp, hot, 'y', linewidth=1.5, label='Hot')

plt.fill_between(x_temp, np.zeros_like(aggregated), aggregated, facecolor='Orange', alpha=0.7)
plt.plot([output_temp, output_temp], [0, fuzz.interp_membership(x_temp, aggregated, output_temp)], 'k', linewidth=1.5, linestyle='--')
plt.title(f'Temperature Categorization with Input = {input_temp}°')
plt.xlabel('Temperature (Degrees)')
plt.ylabel('Membership')
plt.legend()

plt.show()

# Output
# print(f"Defuzzified Output Temperature Category: {output_temp}")
