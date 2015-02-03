class SampleClass(object):
    def __init__(self):
        self._stored_value = 'value at init'

    def set_value(self, value):
        self._stored_value = value

    def get_value(self):
        return self._stored_value

    def __str__(self):
        return self._stored_value
