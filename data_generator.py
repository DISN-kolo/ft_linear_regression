#!venv/bin/python

import numpy as np
import pandas as pd

def noiser(N, fine_std, coarse_shift, region_width, n_regions):
    fine_noise = np.random.normal(0, fine_std, N)
    coarse_noise = np.zeros(N)

    region_size = int(region_width * N)
    starts = []
    while len(starts) < n_regions:
        candidate = np.random.randint(0, N - region_size)
        starts.append(candidate)

    for start in starts:
        end = start + region_size
        effect = np.random.choice(["shift", "thin"])
        if effect == "shift":
            coarse_noise[start:end] += coarse_shift + np.random.normal(
                    0, fine_std * 0.5, region_size)
        elif effect == "thin":
            mask = np.random.rand(region_size) < 0.3
            coarse_noise[start:end] += np.where(mask, np.random.normal(
                0, fine_std * 3, region_size), 0)
    return fine_noise, coarse_noise


if __name__ == "__main__":
    N = 1000
    slope = -0.25
    intercept = 80000.0
    fine_std = 15000.0
    coarse_shift = 6500.0
    region_width = 0.02
    n_regions = 40

    xs = np.linspace(4000, 300000, N)
    ys = slope * xs + intercept

    fine_noise, coarse_noise = noiser(
            N, fine_std, coarse_shift, region_width, n_regions)
    ys = ys + fine_noise + coarse_noise
    fine_noise, coarse_noise = noiser(
            N, fine_std/2, coarse_shift*2, region_width/2, n_regions)
    xs = xs + fine_noise + coarse_noise

    df = pd.DataFrame({"km": xs, "price": ys})
    df = df[df["price"] > 500]
    df = df[df["km"] > 0]
    df.to_csv("gen_data.csv", index=False)
