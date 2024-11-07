import random


class lottocreator:
    def __init__(self, start, end, times, limit):
        self.start = start
        self.end = end
        self.times = times
        self.limit = limit

    def run_lotto_picks(self):
        lottos = []
       

        for __ in range(self.limit):
            lotto = []
            
            while len(lotto) < self.times:
                number = random.randint(self.start, self.end)
                if number not in lotto:
                    lotto.append(number)

            lottos.append(lotto)

        return lottos
            



kimeunho = lottocreator(1, 45, 5, 9)
print(kimeunho.run_lotto_picks())






