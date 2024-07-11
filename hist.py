# # # import pandas as pd
# # # import matplotlib.pyplot as plt

# # # # Load the Excel file
# # # file_path = 'Modification_ENDDATE REMOVAL.xlsx'
# # # data = pd.read_excel(file_path)

# # # # Function to convert columns to numeric and handle errors
# # # def convert_to_numeric(column):
# # #     return pd.to_numeric(data[column], errors='coerce')

# # # # Define custom bins for 0 to 100 with bin width of 5
# # # custom_bins = range(0, 101, 5)
# # # custom_labels = [f'{bin_start}-{bin_start + 5}' for bin_start in custom_bins[:-1]]

# # # # Create histogram for 'verification LLM accuracy'
# # # column_name = 'verification LLM accuracy'

# # # if column_name in data.columns:
# # #     values = convert_to_numeric(column_name).dropna()  # Convert to numeric and drop missing values
    
# # #     plt.hist(values, bins=custom_bins, edgecolor='black')
# # #     plt.title('Histogram of Verification LLM Accuracy')
# # #     plt.xlabel('Accuracy')
# # #     plt.ylabel('Frequency')
# # #     plt.xticks(custom_bins, labels=custom_labels, rotation=45)  # Set custom bin labels and rotate them for better visibility
# # #     plt.grid(True)
# # #     plt.show()
# # # else:
# # #     print(f"Column '{column_name}' not found in the data.")

# # # # Create histogram for 'percentage difference'
# # # column_name = 'percentage difference'

# # # if column_name in data.columns:
# # #     values = convert_to_numeric(column_name).dropna()  # Convert to numeric and drop missing values
    
# # #     plt.hist(values, bins=custom_bins, edgecolor='black')
# # #     plt.title('Histogram of Percentage Difference')
# # #     plt.xlabel('Percentage Difference')
# # #     plt.ylabel('Frequency')
# # #     plt.xticks(custom_bins, labels=custom_labels, rotation=45)  # Set custom bin labels and rotate them for better visibility
# # #     plt.grid(True)
# # #     plt.show()
# # # else:
# # #     print(f"Column '{column_name}' not found in the data.")

# import pandas as pd
# import matplotlib.pyplot as plt

# # Load the Excel file
# file_path = 'Modification_ENDDATE REMOVAL.xlsx'
# data = pd.read_excel(file_path)

# # Function to convert columns to numeric and handle errors
# def convert_to_numeric(column):
#     return pd.to_numeric(data[column], errors='coerce')

# # Define custom bins for 0 to 100 with bin width of 5
# custom_bins = range(0, 101, 5)
# custom_labels = [f'{bin_start}-{bin_start + 5}' for bin_start in custom_bins]

# # Create histogram for 'verification LLM accuracy'
# column_name = 'verification LLM accuracy'

# if column_name in data.columns:
#     values = convert_to_numeric(column_name).dropna()  # Convert to numeric and drop missing values
    
#     plt.hist(values, bins=custom_bins, edgecolor='black')
#     plt.title('Histogram of Verification LLM Accuracy')
#     plt.xlabel('Accuracy')
#     plt.ylabel('Frequency')
#     plt.xticks(custom_bins, labels=custom_labels, rotation=45)  # Set custom bin labels and rotate them for better visibility
#     plt.grid(True)
#     plt.show()
# else:
#     print(f"Column '{column_name}' not found in the data.")

# # Create histogram for 'percentage difference'
# column_name = 'percentage difference'

# if column_name in data.columns:
#     values = convert_to_numeric(column_name).dropna()  # Convert to numeric and drop missing values
    
#     plt.hist(values, bins=custom_bins, edgecolor='black')
#     plt.title('Histogram of Percentage Difference')
#     plt.xlabel('Percentage Difference')
#     plt.ylabel('Frequency')
#     plt.xticks(custom_bins, labels=custom_labels, rotation=45)  # Set custom bin labels and rotate them for better visibility
#     plt.grid(True)
#     plt.show()
# else:
#     print(f"Column '{column_name}' not found in the data.")


import pandas as pd
import matplotlib.pyplot as plt

# Load the Excel file
file_path = 'Modification_ENDDATE REMOVAL.xlsx'
data = pd.read_excel(file_path)

# Function to convert columns to numeric and handle errors
def convert_to_numeric(column):
    return pd.to_numeric(data[column], errors='coerce')

# Define custom bins for 0 to 100 with bin width of 5
custom_bins = range(0, 101, 5)
custom_labels = [f'{bin_start}-{bin_start + 5}' for bin_start in custom_bins]

# Function to plot histogram with frequency values on bins
def plot_histogram_with_frequency(data, column_name, bins, labels):
    if column_name in data.columns:
        values = convert_to_numeric(column_name).dropna()  # Convert to numeric and drop missing values

        # Plot histogram
        plt.hist(values, bins=bins, edgecolor='black')
        plt.title(f' {column_name}')
        plt.xlabel('Percentages')
        plt.ylabel('No.of.Files')
        plt.xticks(bins, labels=labels, rotation=45)  # Set custom bin labels and rotate them for better visibility
        plt.grid(True)

        # Annotate each bin with its frequency
        for i, bin in enumerate(bins[:-1]):
            count = ((values >= bin) & (values < bins[i + 1])).sum()
            plt.text(bin + (bins[i + 1] - bin) / 2, count, str(count), ha='center', va='bottom')

        plt.show()
    else:
        print(f"Column '{column_name}' not found in the data.")

# Plot histograms with frequency values
plot_histogram_with_frequency(data, 'verification LLM accuracy', custom_bins, custom_labels)
plot_histogram_with_frequency(data, 'percentage difference', custom_bins, custom_labels)