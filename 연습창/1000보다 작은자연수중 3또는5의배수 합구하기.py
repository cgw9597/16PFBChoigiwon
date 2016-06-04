#coding:utf8
#1000보다 작은 자연수중 3또는5의 배수 합 구하기
print(sum([i for i in range(1,1000) if i%3 ==0 or i%5 ==0]))