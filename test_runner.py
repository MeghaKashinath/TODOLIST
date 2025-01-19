import os
import sys
from behave.__main__ import main


def run_behave_tests():
    if len(sys.argv) > 1:
        feature_file = sys.argv[1]  # Get the feature file from the command line
        options = [
            '--format', 'pretty',
            feature_file
        ]
    else:
        # Default to running all feature files in the 'features' folder
        feature_folder = os.path.join(os.getcwd(), 'features')
        options = [
            '--format', 'pretty',
            feature_folder
        ]

    # Directly pass the options as command line arguments
    sys.argv = ['behave'] + options  # Simulate the command line args
    main()  # Execute Behave with the arguments


if __name__ == "__main__":
    run_behave_tests()
