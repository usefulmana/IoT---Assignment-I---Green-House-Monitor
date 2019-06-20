from json_parser import Parser


class Checker:

    @staticmethod
    def check_data(temperature, humidity):
        data = Parser()

        if temperature < data.MIN_TEMPERATURE:
            status = 'BAD'
            report = '{}*C below minimum temperature.'.format(round(data.MIN_TEMPERATURE - temperature, 2))
            return status + ': ' + report
        if temperature > data.MAX_TEMPERATURE:
            status = 'BAD'
            report = '{}*C above maximum temperature.'.format(round(temperature - data.MAX_TEMPERATURE, 2))
            return status + ': ' + report
        if humidity < data.MIN_HUMIDITY:
            status = 'BAD'
            report = '{}*% below minimum humidity.'.format(round(data.MIN_HUMIDITY - humidity, 2))
            return status + ': ' + report
        if humidity > data.MAX_HUMIDITY:
            status = 'BAD'
            report = '{}*% above maximum humidity.'.format(round(humidity - data.MAX_HUMIDITY, 2))
            return status + ': ' + report

        return 'OK'
