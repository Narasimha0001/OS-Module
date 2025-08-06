import os

# Step 1: Check/Create data_input directory
input_folder = 'data_input'
output_folder = 'data_output'

if not os.path.exists(input_folder):
    os.makedirs(input_folder)
    print(f"'{input_folder}' folder created. Please add .txt files to it and run again.")
    exit()

# Step 2: Create data_output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

summary_lines = []

# Step 3: Process each .txt file in data_input
for filename in os.listdir(input_folder):
    if filename.endswith('.txt'):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        line_count = 0
        word_count = 0
        modified_lines = []

        with open(input_path, 'r', encoding='utf-8') as infile:
            for line in infile:
                if line.strip().startswith('#'):
                    continue  # Ignore comment lines
                line_count += 1
                word_count += len(line.split())
                modified_line = line.replace('temp', 'permanent')
                modified_lines.append(modified_line)

        with open(output_path, 'w', encoding='utf-8') as outfile:
            outfile.writelines(modified_lines)

        summary_lines.append(f"{filename}\tLines: {line_count}\tWords: {word_count}")

# Step 4: Write summary.txt
summary_path = os.path.join(output_folder, 'summary.txt')
with open(summary_path, 'w', encoding='utf-8') as summary_file:
    summary_file.write("Summary of Processed Files:\n")
    summary_file.write("\n".join(summary_lines))

print("Processing complete. Modified files and summary.txt saved in 'data_output'.")
