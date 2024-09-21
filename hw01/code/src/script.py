import os

# Function to process a single file and create an output file with unique sorted integers
def process_file(input_file_path, output_file_path):
    unique_integers = set()  # Create a set to hold unique integers

    # Open the input file for reading
    with open(input_file_path, 'r') as input_file:
        for line in input_file:
            # Return a copy of the string with leading and trailing whitespace removed
            line = line.strip()
            if not line:  # Skip empty lines
                continue
            try:
                # Skip if there are multiple integers in one line
                if len(line.split()) != 1:
                    continue
                num = int(line)  # Convert the string to an integer
                unique_integers.add(num)  # Add the integer to the set
            except ValueError:
                # Skips the line if the value is not valid
                continue
    
    sorted_integers = sorted(unique_integers)  # Sort the unique integers
    
    # Write the results to the output file
    with open(output_file_path, 'w') as output_file:  # Open in write mode represented by 'w'
        for integer in sorted_integers:
            output_file.write(f"{integer}\n")  # Write each integer on a new line

# Function to automate the process of handling multiple input files and generating corresponding output files
def process_directory(input_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)  # Create the output directory if it doesn't exist
    
    for file_name in os.listdir(input_dir):
        if file_name.endswith(".txt"):  # Only process .txt files
            input_file_path = os.path.join(input_dir, file_name)
            output_file_path = os.path.join(output_dir, f"{file_name}_results.txt")
            process_file(input_file_path, output_file_path)  # Process each file

if __name__ == "__main__":
    # Define input and output directories
    input_dir = "/dsa/hw01/sample_inputs/"
    output_dir = "/dsa/hw01/sample_results/"
    
    process_directory(input_dir, output_dir)  # Process all files in the input directory
