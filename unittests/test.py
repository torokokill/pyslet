#! /usr/bin/env python

"""Runs unit tests on all pyslet modules"""

import unittest

import test_imscpv1p2
import test_imsqtiv1p2p1
import test_imsqtiv2p1
import test_iso8601
import test_rfc2234
import test_rfc2616
import test_rfc4287
import test_rfc5023
import test_unicode5
import test_xml20081126

def suite():
	s=unittest.TestSuite()
	s.addTest(test_imscpv1p2.suite())
	s.addTest(test_imsqtiv1p2p1.suite())
	s.addTest(test_imsqtiv2p1.suite())
	s.addTest(test_iso8601.suite())
	s.addTest(test_rfc2234.suite())
	s.addTest(test_rfc2616.suite())
	s.addTest(test_rfc4287.suite())
	s.addTest(test_rfc5023.suite())
	s.addTest(test_unicode5.suite())
	s.addTest(test_xml20081126.suite())
	return s
	
if __name__ == "__main__":
	runner=unittest.TextTestRunner()
	runner.run(suite())