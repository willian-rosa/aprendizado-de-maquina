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
    '#......',
    '#......',
    '#......',
    '.#.....',
    '.#.....',
    '.#.....',
    '..#....',
    '..#....',
    '..#....',
    '...#...',
    '...#...',
    '...#...',
    '....#..',
    '....#..',
    '....#..',
    '.....#.',
    '.....#.',
    '.....#.',
    '......#',
    '......#',
    '......#'
]


convert = {
    '#':  1,
    '.': -1
}

input_training = []
output_training = []

for i , value in enumerate(input_training_string):
    input_training.append(Util.convert(value, convert))
    output_training.append(Util.convert(output_training_string[i], convert))

bp = BackPropagation()

nn = bp.create_ann([3, 2])

print("=========================== mock ===================")

nn = [
    [
        [0.1, 0, 0.1],
        [0.3, 0.1, 0.9],
        [0.5, 0.4, 1]
    ],
    [
        [0.6, 0.3],
        [0.5, 0.8],
        [0.1, 0.3]
    ]
]

input_training = [
    [1, 1, 0],
    [1, 0, 0],
    [0, 0, 1],
]

output_training = [
    [1, 1],
    [1, 1],
    [0, 1]
]

bp.run(input_training, output_training, nn)


