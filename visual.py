import os
import matplotlib.pyplot as plt
import pandas as pd

# Directory containing the runtime files
directory = 'runtimes'

# Initialize a dictionary to store the runtimes
runtimes = {
    'Platform': [],
    'Model': [],
    'Runtime (seconds)': []
}

# Iterate over each file in the directory
for filename in os.listdir(directory):
    if filename.endswith('.txt'):
        # Extract platform and model from the filename
        parts = filename.split('-')
        platform = parts[0]
        model = parts[1].replace('.txt', '')

        # Read the runtime from the file
        with open(os.path.join(directory, filename), 'r') as file:
            line = file.readline().strip()
            runtime = float(line.split(': ')[1].split(' ')[0])

        # Append the data to the dictionary
        runtimes['Platform'].append(platform)
        runtimes['Model'].append(model)
        runtimes['Runtime (seconds)'].append(runtime)

# Convert the dictionary to a DataFrame
df = pd.DataFrame(runtimes)

# Plot the data
plt.figure(figsize=(10, 6))
for model in df['Model'].unique():
    subset = df[df['Model'] == model]
    plt.bar(subset['Platform'], subset['Runtime (seconds)'], label=model)

plt.title('Model Runtime Comparison Across Platforms')
plt.xlabel('Platform')
plt.ylabel('Runtime (seconds)')
plt.legend(title='Model')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
