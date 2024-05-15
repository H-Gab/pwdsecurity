import argparse

def main(args):
    # Your main logic goes here based on the parsed arguments
    print(f"Received arguments: {args}")

if __name__ == "__main__":
    # Create argument parser
    parser = argparse.ArgumentParser(description="Description of your script.")

    # Add arguments to the parser
    parser.add_argument('arg1', type=str, help='Description of argument 1')
    parser.add_argument('--option1', type=int, default=0, help='Description of option 1')

    # Parse the command-line arguments
    args = parser.parse_args()

    # Call the main function with parsed arguments
    main(args)
