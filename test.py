import pandas as pd
import matplotlib.pyplot as plt
import os
def get_data(data_set_name):
    path = f'{os.getcwd()}/files/{data_set_name}.csv'
    try:
        dataFrame = pd.read_csv(path)
        result = pd.DataFrame({
            "Date": list(dataFrame.Date),
            "Close": list(dataFrame.Close)
        }).to_json(orient='values')
    except:
        result = "Name not found"

    return {'date': eval(result)}
# # df = pd.DataFrame({'Name':['Tom', 'nick', 'krish', 'jack'], 'Age':[20, 21, 19, 18]})
#
# # x = np.linspace(0, 10, 100)
# plt.plot('Date', 'Close', data=df)
# plt.legend()
# plt.show()
