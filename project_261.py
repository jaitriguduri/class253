import requests
equation = input()
result = 'https://newton.now.sh/api/v2//simplify/' + equation
data = requests.get(result).json()
print('Operation for the given equation : ', data['operation'])
print('Expression for given equation : ', data['expression'])
print('Result for given equation : ', data['result'])