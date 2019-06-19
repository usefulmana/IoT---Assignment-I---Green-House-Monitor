from json_parser import Parser


class Checker:

    @staticmethod
    def check_data(temperature, humidity):
        data = Parser()

        if temperature < data.MIN_TEMPERATURE:
            status = 'BAD'
            report = '{}*C below minimum temperature.'.format(data.MIN_TEMPERATURE - temperature)
            return status + ': ' + report
        if temperature > data.MAX_TEMPERATURE:
            status = 'BAD'
            report = '{}*C above maximum temperature.'.format(temperature -  data.MAX_TEMPERATURE)
            return status + ': ' + report
        if humidity < data.MIN_HUMIDITY:
            status = 'BAD'
            report = '{}*% below minimum humidity.'.format(data.MIN_HUMIDITY - humidity)
            return status + ': ' + report
        if humidity > data.MAX_HUMIDITY:
            status = 'BAD'
            report = '{}*% above maximum humidity.'.format(humidity -  data.MAX_HUMIDITY)
            return status + ': ' + report

        return 'OK'
