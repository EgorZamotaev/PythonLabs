import matplotlib.pyplot as plt
import random


def floating_average(dataset):
    smootheddata = [dataset[0]]
    for i in range(1, 4):
        smootheddata.append(sum(dataset[:i+1]) /(i+1))

    for i in range(4, 50):
        smootheddata.append(sum(dataset[i-3:i+1]) / 4)

    return smootheddata


def weighted_average(dataset):
    smootheddata = [dataset[0]]
    smootheddata.append((dataset[1]+0.75*dataset[0])/1.75)
    smootheddata.append((dataset[2] + 0.75 * dataset[1]+0.5 * dataset[0]) / 2.25)
    for i in range(3, 50):
        x = 0
        k = 1
        j = i
        while k != 0:
            x += dataset[j]*k
            k -= 0.25
            j -= 1

        smootheddata.append(x/2.5)
    return smootheddata


def exponential_average(dataset):
    smootgeddata = [dataset[0]]
    alpha = 0.2
    for i in range(1, 50):
        smootgeddata.append(dataset[i]*alpha+(1-alpha)*smootgeddata[i-1])
    return smootgeddata


def linear(dataset):
    smootgeddata = []
    for i in range(2):
        smootgeddata.append(sum(dataset[i-i:i+2])/3+i)

    for i in range(2, 50):
        smootgeddata.append(sum(dataset[i-2:i+2])/5)
    return smootgeddata


def main():
    data = [random.uniform(0, 40) for i in range(50)]
    newdata1 = linear(data)
    newdata2 = floating_average(data)
    newdata3 = exponential_average(data)
    newdata4 = weighted_average(data)

    x = [i for i in range(50)]
    print(data[0:6])
    print(newdata1[0:6])
    line1, line2, line3, line4, line5 = plt.plot(x, data, x, newdata1, x, newdata2, x, newdata3, x, newdata4)
    plt.legend((line1, line2, line3, line4, line5), (u'data', u'linear', u'floating average', u'exponential average',
                                                     u'weighted average'), loc='best')
    plt.show()


if __name__ == '__main__':
    main()
