import random

'''
Q.以下のプログラムを分割せよ
'''
# print('(1) rock\n(2) paper\n(3) scissors')
# human_choice = options[int(input('Choose your option: ')) - 1]
# print(f'You chose: {human_choice}')
# computer_choice = random.choice(options)
# if human_choice == 'rock':
#     if computer_choice == 'paper':
#         print("computer win")
#     elif computer_choice == 'scissors':
#         print("You win")
#     else:
#         print('引き分け')
# elif human_choice == 'paper':
#     if computer_choice == 'rock':
#         print("You win")
#     elif computer_choice == 'scissors':
#         print("computer win")
#     else:
#         print('引き分け')
# elif human_choice == 'scissors':
#     if computer_choice == 'rock':
#         print("computer win")
#     elif computer_choice == 'paper':
#         print("You win")
#     else:
#         print('引き分け')

'''
解答例1
'''
# def human_choice():
#     return int(input('Choose your option: '))

# def computer_choice():
#     return random.choice(list(options.keys()))    
        
# def janken(human, computer):
#     result = (human - computer) % 3
#     if result == 0:
#         return print('引き分け')
#     elif result == 1:
#         return print('computer win')
#     else:
#         return print('You win')

# if __name__ == '__main__':
#     options = {0:"rock", 1:"scissors", 2:"paper"}

#     print(random.choice(list(options.keys())))
#     print('(0) rock\n(1) scissors\n(2) paper')

#     human = human_choice()
#     print(f'You chose: {human} {options[human]}')

#     computer = computer_choice()
#     print(f'Computer chose: {computer} {options[computer]}')

#     janken(human, computer)

'''
解答例2
'''
OPTIONS = ['グー', 'チョキ', 'パー']

def get_human_choice():
    choice_number = int(input('「グー」か「チョキ」か「パー」を番号で選んでください: '))
    return OPTIONS[choice_number - 1]

def get_computer_choice():
    return random.choice(OPTIONS)

def print_options():
    print('\n'.join(f'({i}) {option.title()}' for i, option in enumerate(OPTIONS, start=1)))

def print_choices(human_choice, computer_choice):
    print(f'あなたの選択: {human_choice}')
    print(f'コンピュータの選択: {computer_choice}')

def print_win_lose(human_choice, computer_choice, human_beats, human_loses_to):
    if computer_choice == human_loses_to:
        print(f'残念でした．「{computer_choice}」の勝ちです．')
    elif computer_choice == human_beats:
        print(f'おめでとうございます．「{human_choice}」の勝ちです．')

def print_result(human_choice, computer_choice):
    if human_choice == computer_choice:
        print('引き分けです．')
    
    if human_choice == 'グー':
        print_win_lose(human_choice, computer_choice, 'チョキ', 'パー')
    elif human_choice == 'パー':
        print_win_lose(human_choice, computer_choice, 'グー', 'チョキ')
    elif human_choice == 'チョキ':
        print_win_lose(human_choice, computer_choice, 'パー', 'グー')

print_options()
human_choice = get_human_choice()
computer_choice = get_computer_choice()
print_choices(human_choice, computer_choice)
print_result(human_choice, computer_choice)