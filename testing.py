import unittest
import os
from led import LED
import time
from exceptions import ConnectionTimeoutExpired

class TestLed(unittest.TestCase):
    def setUp(self):
    	self.led = LED('/dev/robot/rgb/rgb1', 'rgb1')

    def test_exists(self):
        self.assertTrue(os.path.exists(self.led.device), "Device has not dev address or not exists")
    
    def test_connected(self):
        self.assertTrue(self.led.ping(), "Ping failed: Device has not connected")

    def test_timeout_refreshed(self):
        result = False
        try:
            self.led.ping()
            raise ConnectionTimeoutExpired("Connection break simulation")
        except ConnectionTimeoutExpired as e:
            time.sleep(1)
            try:
                result = self.led.ping()
            except ConnectionTimeoutExpired as ex:
                result = False
        self.assertEqual(True, result, "Connection timeout expired")

    def test_timeout_expired(self):
        result = False
        try:
            self.led.ping()
            raise Exception("Connection break simulation")
        except Exception as e:
            time.sleep(1)
            try:
                self.led.ping()
                raise ConnectionTimeoutExpired("Connection break simulation")
            except ConnectionTimeoutExpired:
                result = True
        self.assertTrue(result, "Connection timeout expired")


if __name__ == '__main__':
    unittest.main(verbosity=2)