import pandas as pd

# Input and output file paths
input_file = "06152024_log_capture_widgetco.xlsx"   # or .csv
output_file = "widgetco_logs_clean.csv"

# Read Excel/CSV into DataFrame
if input_file.endswith(".xlsx"):
    df = pd.read_excel(input_file)
else:
    df = pd.read_csv(input_file)

# Show columns available
print("Columns found:", df.columns.tolist())

# Select useful fields
fields_of_interest = [
    "TimeCreated", "User", "LogType", "Action",
    "SrcIP", "DstIP", "DstHost", "Url",
    "ProcessName", "CommandLine", "FileName"
]

# Keep only those that exist in the file
selected_fields = [col for col in fields_of_interest if col in df.columns]
df_clean = df[selected_fields]

# Save to CSV for analysis
df_clean.to_csv(output_file, index=False)

print(f"Cleaned log exported to {output_file}")
