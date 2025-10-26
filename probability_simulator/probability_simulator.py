import random
import numpy as np
import matplotlib.pyplot as plt 

class probability_simulator():
    def __init__(self):
        pass

    def coin_flip (self, n_trials):
        heads_Count = 0
        tails_Count = 0
        for trial in range(n_trials):
            outcome = random.choice([0,1])
            if outcome == 0:
                heads_Count += 1
            elif outcome == 1:
                tails_Count += 1

        return (heads_Count, tails_Count)
    
    def dice_roll(self, n_trials, n_dice = 1):
        results = []
        for trial in range(n_trials):
            dice_values = []
            for dice in range(n_dice): 
                dice_values.append(random.randint(1, 6))
            trial_sum = sum(dice_values)
            results.append(trial_sum)

        return results

    def calculate_probability(self, outcomes, target):
        count = 0
        for outcome in outcomes:
            if outcome == target:
                count += 1
        
        probability = count / len(outcomes)

        return probability

    def visualize_distribution(self, data, title='Probabiliy Distribution'):
        plt.hist(data, bins = 5)
        plt.xlabel('Unique value')
        plt.ylabel('Frequency')
        plt.title(title)
        plt.show()

    def central_limit_theorem_demo( self, n_samples =10000, sample_size =30):
        means = []
        for sample in range(n_samples):
            mean = np.mean(self.dice_roll(sample_size, n_dice =1 ))
            means.append(mean)

        self.visualize_distribution(means, 'central')


simulator = probability_simulator()
simulator.central_limit_theorem_demo()





