

with open('C:/Users/Aun/Downloads/a.txt','r') as f:
    data = f.read().split('\n')
    d1= data[0].split(' ')
    D=int(d1[0]) #simulation
    I=int(d1[1]) #intersection number
    S=int(d1[2]) #street_no
    V=int(d1[3]) #number_cars
    print(V)
    street= list()
    for x in data[1:S+1]:
        street.append(x.split(' '))
    car= list()
    for x in data[S+1:S+V+1]:
        car.append(x.split(' '))  
     
    print(car)
    print(street)



with open('0.txt','w') as f:
    f.write("3\n1\n2\nrue-d-athenes 1\nrue-d-amsterdam 1\n0\n1\nrue-de-londres 2\n2\n1\nrue-de-moscou 1")
    