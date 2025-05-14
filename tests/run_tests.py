
import unittest

def run_all_tests():
    # Discover and run all tests in the unit_tests folder
    unit_test_suite = unittest.defaultTestLoader.discover('./unit_tests', pattern='test_*.py')
    print("Running Unit Tests...")
    unittest.TextTestRunner(verbosity=2).run(unit_test_suite)

    # Discover and run all tests in the integration_tests folder
    integration_test_suite = unittest.defaultTestLoader.discover('./integration_tests', pattern='test_*.py')
    print("\nRunning Integration Tests...")
    unittest.TextTestRunner(verbosity=2).run(integration_test_suite)

if __name__ == "__main__":
    run_all_tests()