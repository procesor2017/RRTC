import os.path
import tempfile


class RRTC:
    ROBOT_LISTENER_API_VERSION = 3

    def start_test(self, name, attrs):
        print(attrs)

    def end_test(self, data, test):
        print(data)
        print(test.status)
        print(test.elapsedtime)



