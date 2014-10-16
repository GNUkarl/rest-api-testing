#!/usr/bin/python
#
# Karl G Chavarria
# 10/12/2014
#
# Test3: List Users function
# - tests list users functionality
# - tests list users, limiting count of displayed users functionality

import urllib2, json, unittest, time, sys
from testprep import create_users, params_check


test_amt_users = 5

params_check() #Checks arguments are in proper format, or exits and prints usage statement
test_host = sys.argv[1]


class ListFunctionTest(unittest.TestCase):


        def tearDown(self): # This is run after each test

                # Inserting a smalls sleep between tests to avoid IO contention in the Database
                time.sleep(.5)  # sleep time in seconds
		

        def test01_list_users(self): # Test lists users function and verifies proper user amount is displayed


		def get_users(): # I'm "rebuilding" get_users inside of this test, to totally remove potential
				 # contamination of the test scenario by anything botched in testprep.py's get_users()

		        # Queries userlist API
			url = "%s/users/list" % test_host
		        response = urllib2.urlopen(url)

		        # Counts total occurrences of "user.id" in returned json to determine user total
		        user_amount = str(json.loads(response.read()))
		        user_total = user_amount.count("user.id")

		        # Function returns the current user total
		        return user_total

		pre_exist_users = get_users() # Variable to document starting amount of users in db

		# Create test users with a 1000 starting balance		
                create_users(test_amt_users,10,10)
		
		current_users = get_users() # Variable to document current amount of users after user creation

		test_url = "http://localhost:8000/users/list"
		response = urllib2.urlopen(test_url)

		results = (current_users - pre_exist_users)
		expected_results = test_amt_users

		# Actual PyUnit logic to compare JSON results and expected results
		self.assertEqual(results, expected_results)


        def test02_limited_users(self): # Test limited view of list functinoality and verifies proper number is displayed


                def limit_users(n):

                        # Queries userlist API
    			url = "{0}/users/list?count={1}".format(test_host,n)
	                response = urllib2.urlopen(url)

                        # Counts total occurrences of "user.id" in returned json to determine user total
                        user_amount = str(json.loads(response.read()))
                        user_total = user_amount.count("user.id")

                        # Function returns the current user total
                        return user_total

                lim_view_users = limit_users(test_amt_users) # Variable to document starting amount of users in db

                results = (lim_view_users)
                expected_results = test_amt_users

                # Actual PyUnit logic to compare JSON results and expected results
                self.assertEqual(results, expected_results)


if __name__ == "__main__":
        suite = unittest.TestLoader().loadTestsFromTestCase(ListFunctionTest)
        unittest.TextTestRunner(verbosity=2).run(suite)

