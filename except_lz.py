
import pandas as pd
from pandas.errors import EmptyDataError

class Processing:

    def __init__(self, examples, empty, absence): 
        self.examples = examples
        self.empty = empty
        self.absence = absence
     
    def data(self): #Отсутствие
        try:
            pd.read_csv(self.absence)
        except FileNotFoundError as e:
            print(f"возникла следующая ошибка:{e}")

    def open(self): #Пустота
        try:
            pd.read_csv(self.empty)
        except EmptyDataError:
            print(f"Возникла сдующая ошибка: Датафрейм {self.empty} пуст")

    def false(self):
        df1 = pd.read_csv('var6.csv')
        df2 = pd.read_csv('var7.csv')
        example = list(df1.columns)
        mistake = list(df2.columns)


        if example == mistake:
            print("Чтение датафрейма завершено успешно.") 
        else:
            print(f"Структура датафрейма var7.csv не соответствует ожидаемой Структуре var6.csv:")

            try:
                example == mistake
            except:
                print(f"- Названия столбцов не совпадают")
                print(f"Необходимые:{example}")
                print(f"Фактические:{mistake}")
            
            common_columns = df1.columns.intersection(df2.columns) #Определение необходиой структуры

            for col in common_columns:
                dtype1 = df1[col].dtype
                dtype2 = df2[col].dtype
                print(f"- В столбце {col} тип данных не соответствует ожидаемому.")
                print(f"Необходимый: {dtype1}, Фактически: {dtype2}")

            print("Чтение датафрейма завершено успешно.")    

def main():
    processor = Processing("var6.csv", "empty.csv", "absence.csv")
    processor.data()
    processor.open()
    processor.false()

if __name__ == "__main__":
    main()