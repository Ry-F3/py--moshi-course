# def match_and_reduce(a, b):
#     # Initial totals of a and b
#     total_a_initial = sum(a)
#     total_b_initial = sum(b)
    
#     print(f"Initial total of a: {total_a_initial}")
#     print(f"Initial total of b: {total_b_initial}\n")
    
#     a_copy = a[:]  # Copy of list a
#     b_copy = b[:]  # Copy of list b

#     i = 0  # Pointer for `a`
#     while i < len(a_copy) and b_copy:
#         # Subtract the first element of b_copy from a_copy[i]
#         if a_copy[i] >= b_copy[0]:
#             a_copy[i] -= b_copy[0]
#             b_copy.pop(0)  # No need to append 0 here

#         else:
#             b_copy[0] -= a_copy[i]
#             a_copy[i] = 0
        
#         # Move to the next element in a if current is reduced to 0
#         if a_copy[i] == 0:
#             i += 1
    
#     # Final totals of a and b
#     total_a_final = sum(a_copy)
#     total_b_final = sum(b_copy)
    
#     print("\nFinal state after reduction:")
#     print(f"Final reduced a: {a_copy}")
#     print(f"Final remaining b: {b_copy}")
#     print(f"\nFinal total of a: {total_a_final}")
#     print(f"Final total of b: {total_b_final}")

# # Example usage
# a = [5, 7, 8, 67, 3, 78, 35]
# b = [6, 7, 33, 5, 6, 7, 67, 7, 2, 3, 35]

# match_and_reduce(a, b)

def match_and_reduce(a, b):
    # Initial totals of a and b
    total_a_initial = sum(a)
    total_b_initial = sum(b)
    
    print(f"Initial total of a: {total_a_initial}")
    print(f"Initial total of b: {total_b_initial}\n")
    
    # Track the status of matching for each element in a
    a_status = [{'value': value, 'is_matched': False, 'partial_matched': False} for value in a]
    b_copy = b[:]  # Copy of list b

    i = 0  # Pointer for `a`
    while i < len(a_status) and b_copy:
        # Subtract the first element of b_copy from a_status[i]['value']
        if a_status[i]['value'] >= b_copy[0]:
            a_status[i]['value'] -= b_copy[0]
            b_copy.pop(0)
            
            if a_status[i]['value'] == 0:
                a_status[i]['is_matched'] = True
            else:
                a_status[i]['partial_matched'] = True
        else:
            b_copy[0] -= a_status[i]['value']
            a_status[i]['value'] = 0
            a_status[i]['is_matched'] = True
        
        # Move to the next element in a if current is reduced to 0
        if a_status[i]['value'] == 0:
            i += 1
    
    # Final totals of a and b
    total_a_final = sum([x['value'] for x in a_status])
    total_b_final = sum(b_copy)
    
    print("\nFinal state after reduction:")
    print(f"Final reduced a: {[x['value'] for x in a_status]}")
    print(f"Matching status of a: {a_status}")
    print(f"Final remaining b: {b_copy}")
    print(f"\nFinal total of a: {total_a_final}")
    print(f"Final total of b: {total_b_final}")

# Example usage
a = [5, 7, 8, 67, 3, 78, 35]
b = [6, 7, 33, 5, 6, 7, 67, 7, 2, 3, 35]

match_and_reduce(a, b)
