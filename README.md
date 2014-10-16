OVERVIEW:

The included Python scripts test the Purchase, Add, and List functions of the REST API.

Breakdown of what is included is below:

Test1.py:
- Test01: Purchase function - sufficient balance purchase
- Test02: Purchase function - unsufficient balance purchase
- Test03: Purchase function - cost = string
- Test04: Purchase function - cost = negative integer
- Test05: Purchase function - cost = more than 2 decimal places integer
- Test06: Purchase function - cost = empty input
- Test07: Purchase function - item = string
- Test08: Purchase function - item = negative integer
- Test09: Purchase function - item = more than 2 decimal places integer
- Test10: Purchase function - item = empty input

Test2.py:
- Test01: Add User function - balance = string
- Test02: Add User function - balance = negative integer
- Test03: Add User function - balance = more than 2 decimal places integer
- Test04: Add User function - balance = empty input
- Test05: Add User function - name = empty input

Test3.py:
- Test01: List Users function - list users
- Test02: List Users function - list users, limiting count of displayed users

testprep.py:
- Not an actual test, includes functions referenced by the above scripts




SYSTEM REQUIREMENTS:

- Python 2.7.x

- urllib2 (pip install urllib2).  

- random, json, unittest, time, sys, & re are also used, but these should be native Python 2.7.x modules

- These Python scripts must be run in the same directory as testprep.py, as a great deal of functions are referenced from it.

- Running App Server.  These scripts rely on an already-running test server as a pre-condition.



USAGE:

Python tests can be started like so:

	./Test3.py http://hostname_or_ip:8000

The hostname or IP address of the server under test is required as an argument for these scripts




OUTPUT:

These tests use the standard Python unittest module for their test logic.  Example output is below:

	[test@localhost dev]$ ./Test3.py http://localhost:8000
	test01_list_users (__main__.ListFunctionTest) ... ok
	test02_limited_users (__main__.ListFunctionTest) ... FAIL
	
	======================================================================
	FAIL: test02_limited_users (__main__.ListFunctionTest)
	----------------------------------------------------------------------
	Traceback (most recent call last):
	  File "./Test3.py", line 85, in test02_limited_users
	    self.assertEqual(results, expected_results)
	AssertionError: 4 != 5
	
	----------------------------------------------------------------------
	Ran 2 tests in 1.165s

The names of the tests run, as well as their result (ok/FAIL) will be printed to the screen as they 
are run.  The numeric names of each test run, as well as their descriptions and locations are in the 
overview section of this doc.
