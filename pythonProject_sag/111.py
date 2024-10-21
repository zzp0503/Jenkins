# heavy_cpu_task.py
import time


def find_primes(n):
    primes = []
    for num in range(2, n):
        is_prime = True
        for i in range(2, num):
            if (num % i) == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes


if __name__ == "__main__":
    start_time = time.time()
    print(find_primes(10 ** 7))  # 试着调整这个数值以改变CPU占用
    print("Execution time: ", time.time() - start_time)
