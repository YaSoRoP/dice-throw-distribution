import seaborn as sns
import matplotlib.pyplot as plt
from cube import Cube
from os import system


def main():
    
    cube = Cube()
    quantity = int(input('Введите количество подкидываний игральной кости: '))
    data: dict = cube.roll_dice(quantity)
    
    sns.barplot(x=list(data.keys()), y=list(data.values()))
    plt.title(f'Статистика подбрасываний = {quantity}')
    plt.xlabel('Грань куба')
    plt.ylabel('Ков-во')
    plt.show()
    

if __name__ == '__main__':
    system('cls')
    main()