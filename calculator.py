#addition

qns = input('Enter your question')
splitVals = qns.split('+')
splitVals = list(map(int, splitVals))
print(sum(splitVals))
