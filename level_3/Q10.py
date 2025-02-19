def count_walkaways(total_computers: int, S:str):

    computers = [False] * total_computers
    walkaways = 0
    customer_status = {}

    for customer in S:

        if customer not in customer_status:
            occupied = False

            for i in range(total_computers):
                if not computers[i]:
                    computers[i] = True
                    customer_status[customer] = i
                    occupied = True
                    break
            
            if not occupied:
                walkaways += 1
                customer_status[customer] = -1
        elif customer_status[customer] != -1:
            computers[customer_status[customer]] = False
            customer_status[customer] = -1

            del customer_status[customer]

    return walkaways



if __name__ == '__main__':
    try:
        user_input = int(input())
        visiting_customers = input()
        
        print(count_walkaways(user_input, visiting_customers))

    except ValueError:
        print("Please enter a valid number")
