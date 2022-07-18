import logging

# class LogGen():
#
#     @staticmethod
#     def loggen():
#         logging.basicConfig(filename=r"C:\Users\davud\PycharmProjects\hybrod_framework\Logs\automation.log",
#                             format='%(asctime)s: %(levelname)s: %(message)s',
#                             datefmt='%Y-%m-%d,%H:%M:%S'     # datefmt='%d/%m\%Y %I:%M:%S %p'
#                             )
#
#         # logging.Formatter(
#         #
#         #     fmt='%(asctime)s.%(msecs)03d',
#         #     datefmt='%Y-%m-%d,%H:%M:%S'
#         # )
#
#         logger = logging.getLogger()
#         logger.setLevel(logging.INFO)
#         return logger


# Youtube com 1
# logger = logging.getLogger()
# fhandler = logging.FileHandler(filename='mylog.log', mode='a')
# formatter = logging.Formatter(''%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
# fhandler.setFormatter(formatter)
# logger.addHandler(fhandler)





# Youtube com 2
class LogGen:
        @staticmethod
        def loggen():
            logger = logging.getLogger()
            fhandler = logging.FileHandler(filename=r'C:\Users\davud\PycharmProjects\hybrod_framework\Logs\automation.log', mode='a')
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            fhandler.setFormatter(formatter)
            logger.addHandler(fhandler)
            logger.setLevel(logging.INFO)
            return logger
