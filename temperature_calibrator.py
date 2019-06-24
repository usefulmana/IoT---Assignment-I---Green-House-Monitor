import os


class Calibrator:
    """This class will approximate the real room temperature from the sense hat data"""
    _instance = None
    @staticmethod
    def get_instance():
        if Calibrator._instance is None:
            Calibrator()
        return Calibrator._instance

    def __init__(self):
        if Calibrator._instance is not None:
            raise Exception("This class is a singleton")
        else:
            Calibrator._instance = self

    @staticmethod
    def get_cpu_temp():
        """Getting Pi's CPU Temp"""
        res = os.popen("vcgencmd measure_temp").readline()
        t = float(res.replace("temp=", "").replace("'C\n", ""))
        return t

    @staticmethod
    def calibrate_temperature(temperature):
        return round(temperature - (Calibrator.get_cpu_temp() - temperature) / 1.5, 2)
