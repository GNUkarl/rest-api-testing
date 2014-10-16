#!/usr/bin/python
#
# Karl G Chavarria
# 10/12/2014
#
# Test2: Add User function
# - test balance argument: string, negative integer, more than 2 decimal places, empty input
# - test name argument: empty input

import urllib2, json, unittest, time, sys
from testprep import create_users, get_users, params_check


expected_results = "500" # Expected HTTP Error code for invalid input tests

params_check() #Checks arguments are in proper format, or exits and prints usage statement
test_host = sys.argv[1]


class AddFunctionTest(unittest.TestCase):


        def tearDown(self): # This is run after each test

                # Inserting a smalls sleep between tests to avoid IO contention in the Database
                time.sleep(.5)  # sleep time in seconds


        def test01_bal_string(self): # Test gives string input for balance and tests for proper HTTP 500 error

		test_object = "a" # Testing string input

                current_user_id = get_users()

		test_url = "{0}/users/add_user?name=Test%20User%201&balance={1}".format(test_host,test_object)

                results = "null" # Setting results var to null to fail the PYunit test, in case transaction actually goes through

                try: urllib2.urlopen(test_url)
                except urllib2.URLError as e:
                        results = str(e.code)

                # Actual PyUnit logic to compare JSON results and expected results
                self.assertEqual(results, expected_results)


        def test02_bal_neg_int(self): # Test gives negative integer input for balance and tests for proper HTTP 500 error

                test_object = -1 # Testing negative integer input

                current_user_id = get_users()

                test_url = "{0}/users/add_user?name=Test%20User%202&balance={1}".format(test_host,test_object)

                results = "null" # Setting results var to null to fail the PYunit test, in case transaction actually goes through

                try: urllib2.urlopen(test_url)
                except urllib2.URLError as e:
                        results = str(e.code)

                # Actual PyUnit logic to compare JSON results and expected results
                self.assertEqual(results, expected_results)


        def test03_bal_decimal(self): # Test gives integer with more than 2 decimal places for balance and tests for proper HTTP 500 error

                test_object = 1.12345 # Testing more than 2 decimal places input

                current_user_id = get_users()

                test_url = "{0}/users/add_user?name=Test%20User%203&balance={1}".format(test_host,test_object)

                results = "null" # Setting results var to null to fail the PYunit test, in case transaction actually goes through

                try: urllib2.urlopen(test_url)
                except urllib2.URLError as e:
                        results = str(e.code)

                # Actual PyUnit logic to compare JSON results and expected results
                self.assertEqual(results, expected_results)


        def test04_bal_empty(self): # Test gives empty input for balance and tests for proper HTTP 500 error

                test_object = "" # Testing empty input

                current_user_id = get_users()

                test_url = "{0}/users/add_user?name=Test%20User%204&balance={1}".format(test_host,test_object)

                results = "null" # Setting results var to null to fail the PYunit test, in case transaction actually goes through

                try: urllib2.urlopen(test_url)
                except urllib2.URLError as e:
                        results = str(e.code)

                # Actual PyUnit logic to compare JSON results and expected results
                self.assertEqual(results, expected_results)


	def test05_name_empty(self): # Test gives empty input for user name and tests for proper HTTP 500 error

                test_object = "" # Testing empty input

                current_user_id = get_users()

                test_url = "{0}/users/add_user?name={1}&balance=1000".format(test_host,test_object)

                results = "null" # Setting results var to null to fail the PYunit test, in case transaction actually goes through

                try: urllib2.urlopen(test_url)
                except urllib2.URLError as e:
                        results = str(e.code)

                # Actual PyUnit logic to compare JSON results and expected results
                self.assertEqual(results, expected_results)


if __name__ == "__main__":
	suite = unittest.TestLoader().loadTestsFromTestCase(AddFunctionTest)
	unittest.TextTestRunner(verbosity=2).run(suite)
