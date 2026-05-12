# AND-NOT using McCulloch-Pitts Neuron
def mc_pitts_and_not(A, B):
    w1 = 1    # weight for A 
    w2 = -1   # weight for B 
    theta = 1 # threshold

    net = w1 * A + w2 * B

    if net >= theta:
        return 1
    else:
        return 0

print("A B AND-NOT")
print("---------")
for A in [0, 1]:
    for B in [0, 1]:
        output = mc_pitts_and_not(A, B)
        print(A, B, " ", output)