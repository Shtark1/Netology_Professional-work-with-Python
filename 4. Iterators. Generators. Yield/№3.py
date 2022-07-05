#          итератор обрабатывающий списки с любым уровнем вложенности
number_three = [
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


class FlatIterator1:

    def __init__(self, multi_list):
        self.multi_list = multi_list

    def __iter__(self):
        self.iterators_queue = []
        self.current_iterator = iter(self.multi_list)
        return self

    def __next__(self):
        while True:
            try:
                self.current_element = next(self.current_iterator)
            except StopIteration:
                if not self.iterators_queue:
                    raise StopIteration
                else:
                    self.current_iterator = self.iterators_queue.pop()
                    continue
            if isinstance(self.current_element, list):
                self.iterators_queue.append(self.current_iterator)
                self.current_iterator = iter(self.current_element)
            else:
                return self.current_element


if __name__ == '__main__':
    for item in FlatIterator1(number_three):
        print(item)

    flat_list = [item for item in FlatIterator1(number_three)]
    print("\n\n", flat_list)
