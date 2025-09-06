# 定义父类 Phone
class Phone:
    producer = 'HM' 

    def __init__(self, version, price):
        self.version = version
        self.price = price
    
    def call_by_4g(self):
        print('4G call')

# 定义父类 NFCReader
class NFCReader:
    nfc_type = 4 # 第四代

    def read_card(self):
        print('读取NFC卡')
        

class RemoteControl:
    RC_type = '红外遥控器'

# 定义子类 MyPhone，继承父类 Phone
class MyPhone(Phone):
    def call_by_5g(self):
        print('5G call')

# 定义子类 NewMyPhone，多继承
class NewMyPhone(MyPhone, NFCReader, RemoteControl):
    pass

# 实例化子类，并尝试单继承的类
phone = MyPhone('A2', 2000)
print(phone.producer)
print(phone.version)
print(phone.price)
phone.call_by_4g()

# 尝试多继承的类
new_phone = NewMyPhone('A3', 3000)
print(new_phone.nfc_type)
print(new_phone.RC_type)


