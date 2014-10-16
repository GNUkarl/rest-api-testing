#!/usr/bin/python
#
# Karl G Chavarria
# 10/12/2014
#
# Test1: Purchase function
# - test sufficient and unsufficient balance purchases
# - test cost argument: string, negative integer, more than 2 decimal places
# - test item argument: string, negative integer, more than 2 decimal places, empty input

import urllib2, json, unittest, time, sys
from testprep import create_users, get_users, params_check


user_start_bal = 10 # Starting user balance (in hundreds)
test_item_cost = ((user_start_bal*100)+100) # Test item cost. This is always 100 more than the user's starting balance
expected_results = "500" # Expected HTTP Error code for invalid input tests

params_check() #Checks arguments are in proper format, or exits and prints usage statement
test_host = sys.argv[1]


class PurchaseFunctionTest(unittest.TestCase):


	def setUp(self): # This is run before each test

		# Create one test user with a 1000 starting balance
		create_users(1,user_start_bal,user_start_bal)


        def tearDown(self): # This is run after each test

		# Inserting a smalls sleep between tests to avoid IO contention in the Database		
                time.sleep(.5)  # sleep time in seconds


        def test01_bal_suff(self): # Test purchase functionality with a sufficient balance

                current_user_id = get_users()
                test_url = "{0}/users/purchase?id={1}&cost=900&item=32".format(test_host,current_user_id)
                response = urllib2.urlopen(test_url)
                results = str(json.load(response))

                expected_results = "{u'new_balance': 100.0, u'original_balance': 1000.0}"

                # Actual PyUnit logic to compare JSON results and expected results
                self.assertEqual(results, expected_results)


        def test02_bal_insuff(self): # Test purchase functionality with an insufficient balance
		
		current_user_id = get_users()
                test_url = "{0}/users/purchase?id={1}&cost={2}&item=32".format(test_host,current_user_id,test_item_cost)

		results = "null" # Setting results var to null to fail the PYunit test, in case transaction actually goes through

		try: urllib2.urlopen(test_url)
		except urllib2.URLError as e:
			results = str(e.code)

		# Actual PyUnit logic to compare JSON results and expected results
		self.assertEqual(results, expected_results)


        def test03_cost_string(self): # Test gives string input for cost and tests for proper HTTP 500 error

                test_object = "a" # Testing a string

                current_user_id = get_users()
                test_url = "{0}/users/purchase?id={1}&cost={2}&item=32".format(test_host,current_user_id,test_object)

                results = "null" # Setting results var to null to fail the PYunit test, in case transaction actually goes through

                try: urllib2.urlopen(test_url)
                except urllib2.URLError as e:
                        results = str(e.code)

                # Actual PyUnit logic to compare JSON results and expected results
                self.assertEqual(results, expected_results)


        def test04_cost_neg_int(self): # Test gives negative integer input for cost and tests for proper HTTP 500 error

                test_object = -1 # Testing a negative integer

                current_user_id = get_users()
                test_url = "{0}/users/purchase?id={1}&cost={2}&item=32".format(test_host,current_user_id,test_object)

                results = "null" # Setting results var to null to fail the PYunit test, in case transaction actually goes through

                try: urllib2.urlopen(test_url)
                except urllib2.URLError as e:
                        results = str(e.code)

                # Actual PyUnit logic to compare JSON results and expected results
                self.assertEqual(results, expected_results)


        def test05_cost_decimal(self): # Test gives integer with more than 2 decimal places for cost and tests for proper HTTP 500 error

                test_object = 1.12345 # Testing an integer with more than 2 decimal places

                current_user_id = get_users()
                test_url = "{0}/users/purchase?id={1}&cost={2}&item=32".format(test_host,current_user_id,test_object)

                results = "null" # Setting results var to null to fail the PYunit test, in case transaction actually goes through

                try: urllib2.urlopen(test_url)
                except urllib2.URLError as e:
                        results = str(e.code)

                # Actual PyUnit logic to compare JSON results and expected results
                self.assertEqual(results, expected_results)


        def test06_cost_empty(self): # Test gives empty input for cost and tests for proper HTTP 500 error

                test_object = "" # Testing empty input

                current_user_id = get_users()
                test_url = "{0}/users/purchase?id={1}&cost={2}&item=32".format(test_host,current_user_id,test_object)

                results = "null" # Setting results var to null to fail the PYunit test, in case transaction actually goes through

                try: urllib2.urlopen(test_url)
                except urllib2.URLError as e:
                        results = str(e.code)

                # Actual PyUnit logic to compare JSON results and expected results
                self.assertEqual(results, expected_results)


	def test07_item_string(self): # Test gives string input for item and tests for proper HTTP 500 error

                test_object = "a" # Testing a string

                current_user_id = get_users()
                test_url = "{0}/users/purchase?id={1}&cost=100&item={2}".format(test_host,current_user_id,test_object)

                results = "null" # Setting results var to null to fail the PYunit test, in case transaction actually goes through

                try: urllib2.urlopen(test_url)
                except urllib2.URLError as e:
                        results = str(e.code)

                # Actual PyUnit logic to compare JSON results and expected results
                self.assertEqual(results, expected_results)


        def test08_item_neg_int(self): # Test gives negative integer input for item and tests for proper HTTP 500 error

                test_object = -1 # Testing a negative integer

                current_user_id = get_users()
                test_url = "{0}/users/purchase?id={1}&cost=100&item={2}".format(test_host,current_user_id,test_object)

                results = "null" # Setting results var to null to fail the PYunit test, in case transaction actually goes through

                try: urllib2.urlopen(test_url)
                except urllib2.URLError as e:
                        results = str(e.code)

                # Actual PyUnit logic to compare JSON results and expected results
                self.assertEqual(results, expected_results)


        def test09_item_decimal(self): # Test gives integer with more than 2 decimal places for item and tests for proper HTTP 500 error

                test_object = 1.12345 # Testing an integer with more than 2 decimal places

                current_user_id = get_users()
                test_url = "{0}/users/purchase?id={1}&cost=100&item={2}".format(test_host,current_user_id,test_object)

                results = "null" # Setting results var to null to fail the PYunit test, in case transaction actually goes through

                try: urllib2.urlopen(test_url)
                except urllib2.URLError as e:
                        results = str(e.code)

                # Actual PyUnit logic to compare JSON results and expected results
                self.assertEqual(results, expected_results)


        def test10_item_empty(self): # Test give empty input for item and tests for proper HTTP 500 error

                test_object = "" # Testing empty input

                current_user_id = get_users()
                test_url = "{0}/users/purchase?id={1}&cost=100&item={2}".format(test_host,current_user_id,test_object)

                results = "null" # Setting results var to null to fail the PYunit test, in case transaction actually goes through

                try: urllib2.urlopen(test_url)
                except urllib2.URLError as e:
                        results = str(e.code)

                # Actual PyUnit logic to compare JSON results and expected results
                self.assertEqual(results, expected_results)


if __name__ == "__main__":
        suite = unittest.TestLoader().loadTestsFromTestCase(PurchaseFunctionTest)
        unittest.TextTestRunner(verbosity=2).run(suite)

