import os

def process_file(input_file_path, output_file_path):
    unique_integers = set()

    with open(input_file_path, 'r') as input_file:
        for line in input_file:
            # Strip whitespaces and split the line
            line = line.strip()
            # Skip empty lines
            if not line:
                continue
            # Try to parse the line as an integer
            try:
                # Skip if there are multiple integers in one line
                if len(line.split()) != 1:
                    continue
                num = int(line)
                unique_integers.add(num)
            except ValueError:
                # Skip lines that do not contain a valid integer
                continue
    
    # Sort the unique integers
    sorted_integers = sorted(unique_integers)
    
    # Write the results to the output file
    with open(output_file_path, 'w') as output_file:
        for integer in sorted_integers:
            output_file.write(f"{integer}\n")

def process_directory(input_dir, output_dir):
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    for file_name in os.listdir(input_dir):
        if file_name.endswith(".txt"):
            input_file_path = os.path.join(input_dir, file_name)
            output_file_path = os.path.join(output_dir, f"{file_name}_results.txt")
            process_file(input_file_path, output_file_path)

if __name__ == "__main__":
    input_dir = "/dsa/hw01/sample_inputs/"
    output_dir = "/dsa/hw01/sample_results/"
    
    process_directory(input_dir, output_dir)
