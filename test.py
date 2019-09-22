from backpropagation import BackPropagation
from util import Util

input_training_string = [
    '..##......#......#.....#.#....#.#...#####..#...#..#...#.###.###',
    '...#......#......#.....#.#....#.#...#####..#...#..#...#..#...#.',
    '...#......#.....#.#....#.#...#...#..#####.#.....##.....###...##',
    '######..#....#.#....#.#....#.#####..#....#.#....#.#....#######.',
    '######.#.....##.....##.....#######.#.....##.....##.....#######.',
    '######..#....#.#....#.#####..#....#.#....#.#....#.#....#######.',
    '..#####.#....##......#......#......#......#.......#....#..####.',
    '..###...#...#.#.....##......#......#......#.....#.#...#...###..',
    '..###.#.#...###.....##......#......#......#.....#.#...#...###..',
    '#####...#...#..#....#.#....#.#....#.#....#.#....#.#...#.#####..',
    '#####..#....#.#.....##.....##.....##.....##.....##....#.#####..',
    '#####...#...#..#....#.#....#.#....#.#....#.#....#.#...#.#####..',
    '#######.#....#.#......#.#....###....#.#....#......#....########',
    '########......#......#......#####..#......#......#......#######',
    '#######.#....#.#..#...####...#..#...#......#......#....########',
    '...####.....#......#......#......#......#..#...#..#...#...###..',
    '.....#......#......#......#......#......#..#...#..#...#...###..',
    '....###.....#......#......#......#......#......#..#...#...###..',
    '###..##.#..#...#.#....##.....##.....#.#....#..#...#...#.###..##',
    '#....#.#...#..#..#...#.#....##.....#.#....#..#...#...#..#....#.',
    '###..##.#...#..#..#...#.#....##.....#.#....#..#...#...#.###..##'
]

output_training_string = [
    [
        '#......',
        '#......',
        '#......'
    ],
    [
        '.#.....',
        '.#.....',
        '.#.....'
    ],
    [
        '..#....',
        '..#....',
        '..#....'
    ],
    [
        '...#...',
        '...#...',
        '...#...'
    ],
    [
        '....#..',
        '....#..',
        '....#..'
    ],
    [
        '.....#.',
        '.....#.',
        '.....#.'
    ],
    [
        '......#',
        '......#',
        '......#'
    ]
]

letters = ['a', 'b', 'c', 'd', 'e', 'j', 'k']

input_training = []
output_training = []

for i, value in enumerate(input_training_string):
    input_training.append(Util.convert(value))

bp = BackPropagation()
nn = bp.load()

result = bp.test(nn, input_training[1])
print(result)

for i, out in enumerate(output_training_string):
    for j in out:
        print('-----------------------')
        r = [round(x, 0) for x in result]
        print(r)
        print(Util.convert(j))