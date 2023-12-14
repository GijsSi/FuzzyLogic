
import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

# temp range
x_temp = np.arange(0, 101, 1)

# membership functies
cold = fuzz.trimf(x_temp, [0, 0, 15])  # Cold: 0-15 gradne
chilly = fuzz.trimf(x_temp, [10, 15, 20])  # Chilly: 10-20 graden
warm = fuzz.trimf(x_temp, [15, 25, 35])  # Warm: 15-35 graden
hot = fuzz.trimf(x_temp, [30, 60, 100])  # Hot: 30-100 graden



# inpuit temp
input_temp = 18 

# membership values berken
cold_degree = fuzz.interp_membership(x_temp, cold, input_temp)
chilly_degree = fuzz.interp_membership(x_temp, chilly, input_temp)
warm_degree = fuzz.interp_membership(x_temp, warm, input_temp)
hot_degree = fuzz.interp_membership(x_temp, hot, input_temp)



#  Als input warm is en niet veel chilly, dan meer naar warm
active_rule = np.fmin(warm_degree, 1 - chilly_degree)  

# Defuzzification centroid methode
aggregated = np.fmax(active_rule, np.zeros_like(x_temp))  # regels samen
output_temp = fuzz.defuzz(x_temp, aggregated, 'centroid')  # centroid 



plt.figure(figsize=(8, 6))

plt.plot(x_temp, cold, 'b', linewidth=1.5, label='Cold')
plt.plot(x_temp, chilly, 'g', linewidth=1.5, label='Chilly')
plt.plot(x_temp, warm, 'r', linewidth=1.5, label='Warm')
plt.plot(x_temp, hot, 'y', linewidth=1.5, label='Hot')

plt.fill_between(x_temp, np.zeros_like(aggregated), aggregated, facecolor='Orange', alpha=0.7)
plt.plot([output_temp, output_temp], [0, fuzz.interp_membership(x_temp, aggregated, output_temp)], 'k', linewidth=1.5, linestyle='--')
plt.title(f'Temperature categorie = {input_temp}°')
plt.xlabel('Temperature (Degrees)')
plt.ylabel('Membership')
plt.legend()

plt.show()



# Output
print(f"Defuzzified Output : {output_temp}")



