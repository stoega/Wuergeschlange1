import argparse
import math
import multiprocessing

def sum_of_fractions(start: int, end: int) -> float:
    return sum(1 / k for k in range(start, end + 1))

def euler_mascheroni_approximation(num_processes, num_terms):
    chunk_size = math.ceil(num_terms / num_processes)
    pool = multiprocessing.Pool(processes=num_processes)

    arguments = [(i * chunk_size + 1, min((i + 1) * chunk_size, num_terms)) for i in range(num_processes)]

    partial_sums = pool.starmap(sum_of_fractions, arguments)
    total_sum = sum(partial_sums)

    gamma_approximation = total_sum - math.log(num_terms)
    # print(f"Euler-Mascheroni constant approximation ({num_terms} terms): {gamma_approximation:.9f}")
    return gamma_approximation

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Approximate the Euler–Mascheroni constant.")
    parser.add_argument("--processes", "-p", type=int, default=1, help="Number of processes.")
    parser.add_argument("--terms", "-n", type=int, default=1000, help="Number of terms in the sum.")
    args = parser.parse_args()

    gamma_approximation = euler_mascheroni_approximation(args.processes, args.terms)

    print(f"Euler-Mascheroni constant approximation ({args.terms} terms): {gamma_approximation:.9f}")