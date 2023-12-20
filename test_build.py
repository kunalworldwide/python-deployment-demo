# test_build.py

import unittest
import subprocess
import os

class BuildTestCase(unittest.TestCase):

    def test_app_starts(self):
        """ Test if the Flask app starts without errors. """

        # Command to start the app (adjust if necessary)
        start_cmd = "flask run --host=0.0.0.0 --port=8080"

        # Set necessary environment variables
        os.environ["FLASK_APP"] = "app.py"
        os.environ["FLASK_ENV"] = "development"

        # Start the app in a subprocess
        process = subprocess.Popen(start_cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # Wait for a short time to let the app initialize
        try:
            process.wait(timeout=10)  # Adjust the timeout as needed
        except subprocess.TimeoutExpired:
            # If the timeout expires, it's a good sign - the server is running
            process.kill()
            return

        # If the process exits before the timeout, it means an error occurred
        stdout, stderr = process.communicate()
        self.fail(f"Flask app failed to start. Output: {stderr.decode('utf-8')}")

if __name__ == '__main__':
    unittest.main()
