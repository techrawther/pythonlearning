import random

N=5
res = ''.join(random.choice("asdadasdsad09232"))
print(res)
res = ''.join(random.choices("asdadasdsad09232", k = N))
print(res)
res = random.choices("asdadasdsad09232", k=N)
print(res)
res =random.randint(2,9)
print(res)