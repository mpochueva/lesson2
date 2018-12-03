def get_sum(num_one, num_two):
    try:
        summ = int(num_one) + int(num_two)
        return summ
    except ValueError:
        return 'Please check the data'


a = get_sum("5", 2)
print(a)

