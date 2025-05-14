import unittest
import os

def run_all_tests():
    
    # Get the absolute paths for the test directories
    current_dir = os.path.dirname(os.path.abspath(__file__))
    unit_tests_dir = os.path.join(current_dir, 'unit_tests')
    integration_tests_dir = os.path.join(current_dir, 'integration_tests')
    
    # Discover and run all tests in the unit_tests folder
    unit_test_suite = unittest.defaultTestLoader.discover(unit_tests_dir, pattern='test_*.py')
    print("Running Unit Tests...")
    unittest.TextTestRunner(verbosity=2).run(unit_test_suite)

    # Discover and run all tests in the integration_tests folder
    integration_test_suite = unittest.defaultTestLoader.discover(integration_tests_dir, pattern='test_*.py')
    print("Running Integration Tests...")
    unittest.TextTestRunner(verbosity=2).run(integration_test_suite)

if __name__ == "__main__":
    run_all_tests()