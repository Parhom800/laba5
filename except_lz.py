
import pandas as pd
from pandas.errors import EmptyDataError

class Window:

    def __init__(self, examples, empty, absence): 
        self.examples = examples
        self.empty = empty
        self.absence = absence
     
    def data(self):  # отсутствующий файл
        try:
            pd.read_csv(self.absence)
        except FileNotFoundError as e:
            print(f"Возникла следующая ошибка: {e}")

    def open(self):  # пустой файл
        try:
            pd.read_csv(self.empty)
        except EmptyDataError:
            print(f"Возникла следующая ошибка: Датафрейм {self.empty} пуст")

    def false(self):  # структура и тип данных
        df1 = pd.read_csv(self.examples)
        df2 = pd.read_csv("var7.csv")
        
        example_cols = list(df1.columns)
        mistake_cols = list(df2.columns)

        if example_cols == mistake_cols:
            print("Чтение датафрейма завершено успешно.")
        else:
            print("Структура датафрейма var7.csv не соответствует ожидаемой структуре var6.csv:")
            print(f"- Названия столбцов не совпадают")
            print(f"Ожидаемые: {example_cols}")
            print(f"Фактические: {mistake_cols}")
            
            common_columns = df1.columns.intersection(df2.columns)

            for col in common_columns:
                dtype1 = df1[col].dtype
                dtype2 = df2[col].dtype
                if dtype1 != dtype2:
                    print(f"- В столбце '{col}' тип данных не соответствует ожидаемому:")
                    print(f"  Ожидаемый: {dtype1}, фактически: {dtype2}")

def main():
    glass = Window("var6.csv", "empty.csv", "absence.csv")
    glass.data()
    glass.open()
    glass.false()

if __name__ == "__main__":
    main()
    processor.open()
    processor.false()

if __name__ == "__main__":
    main()
