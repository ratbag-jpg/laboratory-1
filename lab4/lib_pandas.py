import pandas as pd
def use_pandas():
    df = pd.DataFrame({"Ім'я": ["Анна", "Олег"], "Вік": [20, 22]})
    print(f"pandas:\n{df}")