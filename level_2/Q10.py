"""
10. We are making n stone piles! The first pile has n stones. If n is
    even, then all piles have an even number of stones. If n is odd, all
    piles have an odd number of stones. Each pile must have more
    stones than the previous pile but as few as possible. Write a
    Python program to find the number of stones in each pile.
        
        ??????????
        MAYBE THE GIVEN INPUT OUTPUT IS WRONG 
        OR MAYBE I AM NOT UNDERSTANDING THE QUESTION
        ??????????
        Sample Input: n = 7
        Sample Output: Stones in a single pile = [2, 4, 6]
"""


def stone_piles(num: int):

    piles = []
    current_stones = num

    for i in range(num):
        piles.append(current_stones)
        current_stones += 2

    return piles


if __name__ == "__main__":
    try:
        user_input = int(input())

        result = stone_piles(user_input)
        print(f"{result}")

    except Exception as e:
        print(f"An error occured: {e}")
