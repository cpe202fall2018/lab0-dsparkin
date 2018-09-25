def weight_on_planets():
    # write your code here
    wt_earth = float(input("What do you weigh on earth? "))
    print("\nOn Mars you would weigh {0:.2f} pounds.\nOn Jupiter you would weigh {1:.2f} pounds.".format(wt_earth*0.38,wt_earth*2.34))

if __name__ == '__main__':
    weight_on_planets()