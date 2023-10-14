import numpy as np

def random_predict(number:int=1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """

    count = 0
    x1, x2 = 1, 101
    predict_number = np.random.randint(1, 101)
    while True:
        count += 1
        if predict_number > number:
          x1, x2 = x1, predict_number
          predict_number = np.random.randint(x1, x2) # предполагаемое число
        elif predict_number < number:
          x1, x2 = predict_number, x2
          predict_number = np.random.randint(x1, x2) 
        elif number == predict_number:
            break # выход из цикла, если угадали  
    return(count)
print(f'Количество попыток: {random_predict()}')

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел
    
    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

# RUN
#score_game(random_predict)
if __name__ == '__main__':
    score_game(random_predict)