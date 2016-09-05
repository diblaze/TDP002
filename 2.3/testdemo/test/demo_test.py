#!/usr/bin/env python

"""
Test module for demo.py.

Runs various tests on the demo module. Simply run this module to test
the demo.py module.
"""

import test
import demo

def test_echo():
    print("In echo test")
    echo = demo.echo("hej")
    test.assert_equal("hej", echo)
    test.assert_not_equal(None, echo)

def test_add():
    print("In add test")
    added = demo.add("hej ", "hopp")
    test.assert_equal("hej hopp", added)
    test.assert_not_equal("hej", added)

def run_module_tests():
    test.run_tests([test_echo,
                   test_add])

if __name__ == "__main__":
    run_module_tests()
