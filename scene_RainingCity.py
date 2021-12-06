# coding=utf-8
import airsim

if __name__ == '__main__':
    # 连接到AirSim
    client = airsim.VehicleClient()
    client.confirmConnection()

    # 设置打开天气控制
    client.simEnableWeather(True)

    # 下雨，范围为0到1，1表示最强
    client.simSetWeatherParameter(airsim.WeatherParameter.Rain, 1)

    # 地面潮湿，范围为0到1，1表示最强
    client.simSetWeatherParameter(airsim.WeatherParameter.Roadwetness, 1)

    # 雾，范围为0到1，1表示最强
    client.simSetWeatherParameter(airsim.WeatherParameter.Fog, 0.5)
