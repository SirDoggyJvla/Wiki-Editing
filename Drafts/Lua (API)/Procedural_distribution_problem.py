import random
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

plt.rcParams.update({
    "text.usetex": True,
    "font.family": "Computer Modern Roman",
    "font.size": 12,
    #"font.weight":"normal",
    #"axes.labelweight":"normal"
})


def populate_gaussian(N_entries, mean, stddev, item_list = None, disable=True):
    item_list = [] if item_list is None else item_list
    if not disable:
        print("Poulating gaussian distribution")
    for _ in tqdm(range(N_entries), desc="Populating Gaussian Distribution", disable=disable):
        item = round(random.gauss(mean, stddev), 2)
        # item['chance'] = round(random.gauss(mean, stddev), 2)
        if item > 0:
            item_list.append(item)
    return item_list

def populate_uniform(N_entries, min, max, item_list = None, disable=True):
    item_list = [] if item_list is None else item_list
    if not disable:
        print("Poulating uniform distribution")
    for _ in tqdm(range(N_entries), desc="Populating Uniform Distribution", disable=disable):
        item = round(random.uniform(min, max), 2)
        # item['chance'] = round(random.uniform(min, max), 2)
        if item > 0:
            item_list.append(item)
    return item_list

def generate_container(item_list, roll):
    N_items_generated = 0
    for item in item_list:
        for i in range(1, roll+1):
            chance = random.uniform(0, 100)
            if chance <= item:
                N_items_generated += 1
                break

    return N_items_generated


def get_mean_item_number(item_list, rolls, disable=True, tests=10000):
    if not disable:
        print("Getting mean item number")
    amounts = []
    for _ in tqdm(range(1, tests), desc="Calculating Mean Item Number", disable=disable):
        N_items_generated = generate_container(item_list, rolls)
        amounts.append(N_items_generated)
    # print("Mean item number: ", len(item_list), np.mean(amounts))

    return np.mean(amounts)

def get_chance_distribution(item_list):
    # print("Getting chance distribution")
    chances = {}
    for chance in item_list:
        if chance not in chances:
            chances[chance] = 0
        chances[chance] += 1
    return dict(sorted(chances.items()))

def set_list(dist, N_entries):
    return random.choices(list(dist.keys()), weights=list(dist.values()), k=N_entries)





# chance: weight
dist = {
    0.01: 10,
    1: 20,
    5: 50,
    10: 100,
    20: 200,
}

mean, std = 5, 2
min_chance, max_chance = 0.01, 20

min_rolls, max_rolls = 1, 5
min_amount, max_amount, step = 1, 10, 2

###
### Distribution
###

N_entries = 1000
# list = populate_gaussian(N_entries, mean, std)
# item_lists = populate_uniform(N_entries, min_chance, max_chance)
item_lists = set_list(dist, N_entries)
dist = get_chance_distribution(item_lists)

fig, axs = plt.subplots(2, 1, figsize=(10, 6))
ax = axs[0]
ax.bar(dist.keys(), dist.values(), width=0.1, color='blue', alpha=1)
ax.set_xlabel('Chance')
ax.set_ylabel('Items')
ax.set_title(f"Distribution for {N_entries} entries")
ax.grid(True)


###
### Mean amount generated
###

entries = np.arange(min_amount, max_amount+step, step)
rolls = np.arange(min_rolls, max_rolls+1, 1)
amount_generated = np.zeros((len(entries), len(rolls)))
for i, N_entries in enumerate(tqdm(entries, desc="Calculating Mean Amount Generated")):
    # item_lists = populate_uniform(N_entries, min_chance, max_chance)
    item_lists = set_list(dist, N_entries)
    for j, roll in enumerate(tqdm(rolls, desc="Calculating Mean Amount Generated", leave=False)):
        mean = get_mean_item_number(item_lists, roll)

        amount_generated[i,j] = mean

ax = axs[1]
for j, roll in enumerate(rolls):
    ax.plot(entries, amount_generated[:, j], label=f'Rolls: {roll}')
ax.set_xlabel('Number of Entries in container distribution')
ax.set_ylabel('Mean amount of spawned items')
ax.set_title(f"Impact of the number of entries in a container distribution on the mean amount of spawned items")
ax.legend()
ax.grid(True)


plt.tight_layout()
plt.show()
