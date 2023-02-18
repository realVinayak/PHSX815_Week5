import math
import numpy as np
import matplotlib.pyplot as plt
from histogram_utils import get_histogram_data
from file_list_utils import write_list


N_SAMPLE = 1000000


def rejection_sample_uniform(base_pdf, N_samples, x_min, x_max):
    samples = []
    while len(samples) < N_samples:
        x_to_probe = x_min + (x_max - x_min) * np.random.random()
        uniform_rv = np.random.random()
        function_value = base_pdf(x_to_probe)
        if uniform_rv > function_value:
            continue
        samples.append(x_to_probe)
    return samples


def driver():
    sin_scaled = lambda x: (math.pi / 2) * math.sin(x * math.pi)
    samples_drawn = rejection_sample_uniform(sin_scaled, N_SAMPLE, 0, 1)
    write_list(samples_drawn, './outputs/samples.txt')
    probs, bins = get_histogram_data(samples_drawn, N_SAMPLE + 1)
    plt.plot(bins, probs, alpha=0.5, linewidth=0.4)
    plt.savefig('./outputs/sin_hist.png')
    plt.show()


if __name__ == "__main__":
    driver()
