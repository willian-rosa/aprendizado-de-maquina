

class Util:

    @staticmethod
    def convert(text, convert):

        map = []

        for char in text:
            try:
                if convert[char]:
                    map.append(convert[char])
            except ValueError:
                map.append(0)

        return map

