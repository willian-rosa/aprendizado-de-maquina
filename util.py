

class Util:

    @staticmethod
    def convert(text):

        map = []

        hashtag = 1
        dot = 0

        for char in text:
            if char == '#':
                map.append(hashtag)
            elif char == '.':
                map.append(dot)
            else:
                map.append(0)

        return map

