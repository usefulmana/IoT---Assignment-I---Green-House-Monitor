import os


class Calibrator:
    """This class will approximate the real room temperature from the sense hat data"""
    @staticmethod
    def get_cpu_temp():
        """Getting Pi's CPU Temp"""
        res = os.popen("vcgencmd measure_temp").readline()
        t = float(res.replace("temp=", "").replace("'C\n", ""))
        return t

    @staticmethod
    def calibrate_temperature(temperature):
        return round(temperature - (Calibrator.get_cpu_temp() - temperature) / 1.5, 2)
