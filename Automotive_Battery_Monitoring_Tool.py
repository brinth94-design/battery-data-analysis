import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("battery_data.csv")

plt.plot(data["time"], data["voltage"])
plt.xlabel("Time")
plt.ylabel("Voltage")
plt.title("Battery Voltage Over Time")

plt.savefig("battery_plot.png", dpi=100, bbox_inches='tight')
print("Plot gespeichert als: battery_plot.png")