print("hello,Welcome to Aj's Question")

ans=input('Are u ready to play (yes/no): ')
score = 0
total_q = 4


if ans.lower() == 'yes':
    ans = input('1. What is the best pogramming language?')
    if ans.lower() == 'python':
        score += 1
        print('correct')
    else:
        print('Incorrect')


    ans =input('2. which country has most tallest statue in world?')
    if ans.lower() == 'india':
        score += 1
        print('correct')
    else:
        print('Incorrect')



    ans =input('3. What is better a 1050ti or a 1060 (graphical card)?')
    if ans == '1060':
        score += 1
        print('correct')
    else:
        print('Incorrect')

    ans =input('4. Which team won 2021 icc world cup?')
    if ans.lower() == 'australia':
        score += 1
        print('correct')
    else:
        print('Incorrect')

print('well played',score,'question correct.')
mark= (score/total_q)*100

print('mark:', str(mark) + '%')
print('thank u for playing')
