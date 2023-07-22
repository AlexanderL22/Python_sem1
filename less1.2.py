for i in [[2, 3, 4, 5], [6, 7, 8, 9]]:
    if i != 0:
        print("")
    for k in range(2, 10):
        print('%s X %s = %s\t\t\t' % (i[0], k, i[0] * k if i[0] * k > 9 else ' ' + str(i[0] * k)),
              '%s X %s = %s\t\t\t' % (i[1], k, i[1] * k if i[1] * k > 9 else ' ' + str(i[1] * k)),
              '%s X %s = %s\t\t\t' % (i[2], k, i[2] * k if i[2] * k > 9 else ' ' + str(i[2] * k)),
              '%s X %s = %s\t\t\t' % (i[3], k, i[3] * k if i[3] * k > 9 else ' ' + str(i[3] * k)))