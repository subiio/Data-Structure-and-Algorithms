import random

class ArrayQueue:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.array = [None] * capacity
        self.front = 0
        self.rear = 0

    def isEmpty(self):
        return self.front == self.rear

    def isFull(self):
        return self.front == (self.rear + 1) % self.capacity

    def enqueue(self, element):
        if not self.isFull():
            self.rear = (self.rear + 1) % self.capacity  # 수정됨
            self.array[self.rear] = element
        else:
            pass

    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front + 1) % self.capacity
            return self.array[self.front]
        else:
            pass

    def peek(self):
        if not self.isEmpty():
            return self.array[(self.front + 1) % self.capacity]
        else:
            pass
  



def bank_simulation(simul_time,customer_rate, service_time):
    customer = ArrayQueue(100)
    remaining_service_time = 0
    total_wait_time =  0
    customer_number = 0
    
    for currentTime in range(simul_time):
        if random.random() < customer_rate:
            serviceTime = random.randint(1, service_time)
            customer.enqueue((currentTime, serviceTime))
        if remaining_service_time > 0:
            remaining_service_time -= 1
        elif not customer.isEmpty():
            arrivalTime, serviceTime = customer.dequeue()
            total_wait_time += currentTime - arrivalTime
            remaining_service_time = serviceTime - 1
            customer_number += 1
    if customer_number == 0:
        return 0
    else:
        total_wait_time/customer_rate
    
    



# 2.1은행 시뮬레이션
def bank_simulation(simulTime,arrivalRate,maxServiceTime):
    totalWaitTime = 0
    remainingServiceTime = 0
    customer = ArrayQueue(100)
    customerNumber = 0
    for currentTime in range(simulTime):
        if random.random() < arrivalRate:
            serviceTime = random.randint(1,maxServiceTime)
            customer.enqueue((currentTime, serviceTime))
        elif remainingServiceTime > 0 :
            remainingServiceTime -= 1
        elif not customer.isEmpty():
            arrivalTime, serviceTime = customer.dequeue() 
            totalWaitTime = currentTime - arrivalTime
            remainingServiceTime = serviceTime - 1
            customerNumber += 1
    if customerNumber == 0:
        return 0
    else:
        return totalWaitTime/customerNumber        
            

def bankSimulation(maxTime,arrivalRate,maxServiceTime):
    customer = ArrayQueue(100)
    customerNumber = 0
    remainingServiceTime = 0
    totalWaitTime = 0
    for currentTime in range(maxTime):
        if random.random() < arrivalRate:
            serviceTime = random.randint(1,maxServiceTime)
            customer.enqueue(currentTime, serviceTime)
        elif remainingServiceTime > 0 :
            remainingServiceTime -= 1
        elif not customer.isEmpty():
            arrivalTime, serviceTime = customer.dequeue()
            totalWaitTime = currentTime - arrivalTime
            remainingServiceTime = serviceTime - 1
            customerNumber += 1
    if customerNumber == 0:
        return 0
    else:
        return totalWaitTime/customerNumber

maxTime = 10  # 최대 시간
arrivalRate = 0.5  # 단위시간당 도착하는 고객 수
maxServiceTime = 5  # 한 고객에 대한 최대 서비스 시간

# 시뮬레이션 실행 및 결과 출력
averageWaitTime = bank_simulation(maxTime, arrivalRate, maxServiceTime)
print(f"고객들의 평균 대기시간: {averageWaitTime:.2f} 단위시간")

# def bank_simulation(simul_time,customer_rate,service_time):
#     total_wait_time = 0
#     remaining_service_time = 0
#     number_customer = 0
#     customer = ArrayQueue(100)
#     for currentTime in range(simul_time):
        
#         if random.random() < customer_rate:
#             serviceTime = random.randint(1,service_time)
#             customer.enqueue((currentTime, serviceTime))
#         elif remaining_service_time > 0 :
#             remaining_service_time -= 1
#         elif not customer.isEmpty():
#             arrivalTime, serviceTime = customer.dequeue()
#             total_wait_time = currentTime - arrivalTime
#             remaining_service_time = serviceTime - 1
#             number_customer += 1
#     if number_customer == 0:
#         return 0
#     else:
#         return total_wait_time/number_customer
            
            
        
        
