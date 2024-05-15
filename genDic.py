import argparse
import os
import uuid

def main(args):
    # appeler leet.py avec les bons arguments
    file_name = f"output_{uuid.uuid4().hex}.txt"
    file_path = os.path.join('.', file_name)
    
    content="blablabla"

    with open(file_path, 'w') as file:
            # Write the content to the file
            file.write(content)
    print(f"Content successfully written to '{file_path}'.")
    
    print("text") 

if __name__ == "__main__":
    # Create argument parser
    parser = argparse.ArgumentParser(description="Description of your script.")

    # Add arguments to the parser
    parser.add_argument('arg1', type=str, default='none', help='Leet (-l [none,basic,complex], default none)')
    parser.add_argument('--option1', type=int, default=0, help='Description of option 1')

    # Parse the command-line arguments
    args = parser.parse_args()

    # Call the main function with parsed arguments
    main(args)
