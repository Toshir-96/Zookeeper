score = int(input())
Max = int(input())

if (Max / score * 100) and (score >= 90) and (score < 100):
    print('A')
elif (Max / score * 100) and (score >= 80) and (score < 90):
    print('B')
elif (Max / score * 100) and (score >= 70) and (score < 80):
    print('C')
elif (Max / score * 100) and (score >= 60) and (score < 70):
    print('D')
else:
    print('F')
