#
# Karl G Chavarria
# 10/12/2014
#
# This python file is for holding test prep functions to be referenced from within actual tests

import sys, random, urllib2, json, re

# create_users() is used to quickly create test users on the fly as a precondition for a test.
# It requires 3 parameters: n, x, and y. n is the total number of test users desired,
# x (minimum balance *in hundreds*) and y (maximum balance *in hundreds*) are used to specify a
# range of starting balances that will randomly populate starting balance of the test users.
# If x and y are identical values, then all users will be statically assigned that value.

def create_users(n,x,y):

	create_amt = n
	min_bal = x
	max_bal = y
        current_user_id = (get_users()+1)
	upper_range = current_user_id+create_amt

	# Creates as many test users as desired, sequentially named "Test UserX", where X is the current loop iteration
	for x in range (current_user_id, upper_range):

		# If x and y are identical test user balance will be statically set to that value, otherwise the balance is
		# set to a random value between x and y

		if (min_bal == max_bal):
	        	# Statically set test user balance to whatever max_bal is
			fill_balance = max_bal * 100
		else:
			# Create a random value between x and y for test user balance
	               	fill_balance = (random.randrange(min_bal,max_bal))*100

		# Creates a test user named "Test UserX" where X is the current loop iteration
		url1 = "http://localhost:8000/users/add_user?name=Test%20User%20{0}".format(x)
		url2 = "&balance={0}".format(fill_balance)
		url = url1 + url2

		# Sends actual HTTP request to create test user
		response = urllib2.urlopen(url)



# get_users() is used to keep track of the current amount of users existing in the database.
# It does not accept parameters, it simply returns an integer when called.

def get_users():

	# Queries userlist API
	url = "http://localhost:8000/users/list"
	response = urllib2.urlopen(url)

	# Counts total occurrences of "user.id" in returned json to determine user total
	user_amount = str(json.loads(response.read()))
	user_total = user_amount.count("user.id")

	# Function returns the current user total
	return user_total



# usage() prints a basic usage statement of how to supply the hostname argument to the script

def usage():

        print "\n\nUsage:\n"
        print sys.argv[0],"http://hostname_or_ip:8000\n\n"
	exit()



# params_check checks that a command line argument exists and validates that it's in proper URL format

def params_check():
	
	if len(sys.argv) < 2: # If there are no arguments print usage, else validate argument
	        usage()
	else:
	        if re.match(r'^http.//.*:8000$', sys.argv[1]): # If argument matches URL regex proceed, else print usage
        	        test_host = ""
	        else:
        	        usage()



# test_runner() is used to simplify boundary testing of REST API key/value pairs
# The function takes 3 arguments:
#
# example_url: an actual example URL of what's being tested, ex: http://localhost:8000/users/purchase?id=3&cost=900&item=32
# the actual site (in this case, localhost) does not matter as it's discarded. You *can* just input
# "/users/purchase?id=3&cost=900&item=32"(no quotes) for example_url if you want to.
#
# test_key: name of key argument that is under test, ex: id
#
# test_value: content that you're actually using to test the test_key, ex: -1, "string", ""(empty input)

def test_runner(example_url,test_key,test_value):


        # If key under test is "id", don't auto-set the id value from get_users()
        # If key under test is not "id", then get a user id from get_users() and run test with that

        if test_key == "id":
                test_url = re.sub(r"%s=\d*" % re.escape(test_key), "%s=%s" % (test_key,test_value), example_url)
        else:
                current_user_id = get_users()
                test_url = re.sub(r"%s=\d*" % re.escape(test_key), "%s=%s" % (test_key,test_value), example_url)
                test_url = re.sub(r"id=\d*", "id=%s" % (current_user_id), test_url)

        # Actually try and open the test_url and make this function return the HTTP error code if one is returned
        # from the web request, or make this function return "null" to force the test to fail

        try:
                results = "null" # Setting results var to null to fail the PYunit test, in case transaction actually goes through
                urllib2.urlopen(test_url)
        except urllib2.URLError as e:
                results = str(e.code)

        return results


