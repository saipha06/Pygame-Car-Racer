# class Singleton:
#     __instance = None
#     __bool = True
#     @staticmethod 
#     def getInstance():
#         """ Static access method. """
#         if Singleton.__instance == None:
#             Singleton()
#         return Singleton.__instance
#     def __init__(self):
#         """ Virtually private constructor. """
#         if Singleton.__instance != None:
#             print('Cannot Create')
#         else:
#             Singleton.__instance = self
#     def add(self):
#         print('here')

# s = Singleton.getInstance()
# s.add()
# y = Singleton

class Singleton(object):
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(
                                cls, *args, **kwargs)
        return cls._instance
