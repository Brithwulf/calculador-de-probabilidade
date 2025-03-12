import copy
import random

class Hat:
    def __init__(self, **kwargs):
        contents = [key for key, value in kwargs.items() for _ in range(value)]
        self.contents = contents
        if not kwargs:
            raise ValueError("It's necessary to give at least one attribute")
        for key, value in kwargs.items():
            setattr(self, key, value)
    
    def draw(self, num):
        list_of_strings = []
        if num > len(self.contents):
            drawn_items = self.contents[:]
            self.contents.clear()
            return drawn_items
        for _ in range(num):
            rand = random.randrange(len(self.contents))
            i = self.contents[rand]
            list_of_strings.append(i)
            self.contents.remove(i)
        return list_of_strings

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success = 0

    for _ in range(num_experiments):
        copied_hat = copy.deepcopy(hat)
        drawn_balls = copied_hat.draw(num_balls_drawn)
        some_dict = {}

        for ball in drawn_balls:
            if ball in some_dict:
                some_dict[ball] += 1
            else:
                some_dict[ball] = 1

        is_success = True
        
        for color, count in expected_balls.items():
            if some_dict.get(color, 0) < count:
                is_success = False
                break
        if is_success:
            success += 1
    
    probability = success / num_experiments
    return probability

hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                  expected_balls={'red':2,'green':1},
                  num_balls_drawn=5,
                  num_experiments=2000)
print(probability)