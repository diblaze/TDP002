#!/usr/bin/env python

"""
Test utilities.

Various utilities for handling and reports of tests.  The test
primitives are silent on success but signals failure by throwing and
catching test exceptions.
"""

import sys
import os
import imp
import traceback

failureError = AssertionError

def fail(msg=None):
    """Fail immediately with the given message."""
    raise failureError("[Fail] " + msg)

def assert_false(expr, msg=""):
    """Succeeds if the expression is false."""
    if expr: raise failureError("[AssertFailse] " + str(msg))

def assert_true(expr, msg=""):
    """Succeeds if the test expression is true."""
    if not expr: raise(failureError("[AssertTrue] " + str(msg)))

def assert_equal(first, second, msg=""):
    """Succeeds if the two objects are equal, uses the '==' operator."""
    if not first == second:
        raise failureError('[{} != {}] '.format((first, second) + str(msg)))

def assert_not_equal(first, second, msg=""):
    """Succeeds if the two objects are not equal, uses the '==' operator."""
    if first == second:
        raise failureError('[{} == {}] '.format((first, second) + str(msg)))

def run_tests(test_functions):
    """
    Executes the given list of parameter-free test functions. 

    Success is silent, failure gives reports. The session is summarized at the end. 
    The tests signals test failure using failureException wich is
    """
    no_failures = 0
    no_exceptions = 0
    no_tests = 0
    for fn in test_functions:
        try:
            fn()
        except failureError as err:
            print("Failure in {}: {}".format(fn.__name__, err.args))
            no_failures += 1
        except:
            print("Exception in {}: {}".format(fn.__name__, sys.exc_info()[1]))
            print("\n*** Begin traceback")
            traceback.print_exc()
            print("*** End traceback\n")
            no_exceptions += 1
            
        no_tests += 1
    print("{} tests run (Exceptions: {}, Failures: {})".format(no_tests, no_exceptions, no_failures))


