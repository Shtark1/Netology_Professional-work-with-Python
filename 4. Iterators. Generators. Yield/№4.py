#                        4.* генератор обрабатывающий списки с любым уровнем вложенности
number_four = [
    ['aada', 'bjiljil', 'cbvnbn',
     ["drtyt", "polka",
      ["all",
       ["lol", 0,
        ["abu",
         [114214, "ada",
          [11031, "ad"], "adad"], 131]
        ]
       ]
      ]
     ],
    ['dcvx', 'exvcxv', 'fxvv', 'hp/o/', False],
    [17897, 24353, None],
    ]

def FlatIterator4(lists):
    for liste in lists:
        yield liste


def check(check_items):
    if isinstance(check_items, list):
        for items in FlatIterator4(check_items):
            check(items)
    else:
        print(check_items)


if __name__ == "__main__":
    for item in FlatIterator4(number_four):
        check(item)
