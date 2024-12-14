# import time
# from tqdm import tqdm

# with tqdm(total=3, desc='level_1', position=0, leave=False) as pbar:
#     for i in tqdm(range(3)):
#         for j in tqdm(range(5), desc='level_2', position=0, leave=True):
#             time.sleep(0.1)
#         pbar.update()
import matplotlib.pyplot as plt
import numpy as np
import time

def update_plot(x, y, i,fig):
    plt.clf()  # Clear the entire figure
    plt.scatter(x, y, color='blue')  # Create a scatter plot with blue 
    plt.xlim(0, 10)  # Set x-axis limits
    plt.ylim(0, 10)  # Set y-axis limits
    plt.title(f"Real-time Data Plotting Iteration: {i}")  # Add a title
    plt.xlabel("X-axis")  # Label for x-axis
    plt.ylabel("Y-axis")  # Label for y-axis
    plt.grid(True)  # Enable grid for better visibility
    plt.pause(0.1)  # Pause for a brief moment to update the plot

# Example usage in a loop
x = []
y = []

fig=plt.figure()  # Open a figure once
plt.ion()  # Enable interactive mode

for i in range(100):
    x=[np.random.rand() * 10 for i in range(10)]  # Simulate new x data
    y=[np.random.rand() * 10 for i in range(10)]  # Simulate new y data
    print(x,y)
    update_plot(x, y, i,fig)  # Update the plot with new data
    time.sleep(0.5)  # Simulate delay for data collection

plt.ioff()  # Disable interactive mode when done
plt.show()  # Show the final plot