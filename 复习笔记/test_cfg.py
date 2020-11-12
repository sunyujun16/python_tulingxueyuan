import configparser

# 第一步，生成相应的configparser的实例
cfg = configparser.ConfigParser()

# 生成实例之后需要读取相应的配置文件

cfg.read('test_config.cfg')

sp_name = cfg.get('SmallPlane', 'name')
print(sp_name)

sp_width = cfg.getint('SmallPlane', 'width')
print(sp_width)