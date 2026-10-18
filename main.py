"""Display a second-by-second terminal countdown."""

import time


def main():
    try:
        seconds = int(input("Seconds to count down: "))
        if seconds < 1:
            raise ValueError
    except ValueError:
        print("Enter a positive whole number.")
        return
    for remaining in range(seconds, 0, -1):
        print(f"{remaining} second(s) remaining", end="\r", flush=True)
        time.sleep(1)
    print("Time is up!" + " " * 20)


if __name__ == "__main__":
    main()
