import logging

class Validator():

    def __init__(self) -> None:
        self._LOGGER = logging.getLogger(__name__)

    async def isValidIP(self, ip: str) -> bool:
        # check number of periods
        if ip.count('.') != 3:
         return False

        l = list(map(str, ip.split('.')))

        # check range of each number between periods
        for ele in l:
            if int(ele) < 0 or int(ele) > 255 or (ele[0] == '0' and len(ele) != 1):
                return False

        return True
