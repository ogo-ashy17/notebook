names = ['ラリー', 'カーリー', 'モー']
message = '三ばか大将:'
for index, name in enumerate(names):
    if index > 0:
        message += 'に'
    if index == len(names) - 1:
        message += '，それから'
    message += name

print(message)


# def introduce(title, names):
#     message = f'{title}:'
#     for index, name in enumerate(names):
#         if index > 0:
#             message += 'に'
#         if index == len(names) - 1:
#             message += '，それから'
#         message += name
#     return message

# introduce('三ばか大将', ['ラリー', 'カーリー', 'モー'])


def join_names(names):
    name_string = ''
    for index, name in enumerate(names):
        if index > 0:
            name_string += 'に'
        if index == len(names) - 1:
            name_string += '，それから'
        name_string += name
    return name_string


def introduce(title, names):
    print(f'{title}:{join_names(names)}')

introduce('三ばか大将', ['ラリー', 'カーリー', 'モー'])