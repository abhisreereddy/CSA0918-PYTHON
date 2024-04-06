def find_msd_lsd(number):
    number_str = str(number)
    msd = number_str[0]
    lsd = number_str[-1]
    return msd, lsd
number = input("Enter number: ")
msd, lsd = find_msd_lsd(number)
print("MSD:", msd)
print("LSD:", lsd)
