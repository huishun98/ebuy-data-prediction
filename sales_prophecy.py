import pandas as pd
from fbprophet import Prophet
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from fbprophet.plot import plot_plotly, plot_components_plotly


outlet_number = 1

purchase_xls = pd.ExcelFile('Master Data (Purchase).xlsx')
purchase_data_raw = pd.read_excel(purchase_xls, 'Purchase - Outlet {}'.format(outlet_number))
raw_materials_sku_list = purchase_data_raw['SKU'].unique()
# print("raw_materials_sku_list: ", raw_materials_sku_list)

for chosen_raw_material_sku in raw_materials_sku_list:
    df = pd.read_csv('./churned datasets/outlet{}_{}.csv'.format(outlet_number, chosen_raw_material_sku))
    # df['ds']= pd.to_datetime(df['ds'])

    m = Prophet()
    m.fit(df)

    future = m.make_future_dataframe(periods=7)
    # print("head: ", future.head())
    # print("tail: ", future.tail()) 

    forecast = m.predict(future)
    filtered_forecast = forecast[(forecast['ds'] >= '2020-12-01') & (forecast['ds'] <= '2020-12-31')][['ds', 'yhat']]

    print("filtered_forecast: ", filtered_forecast)
    filtered_forecast.to_csv('prediction datasets/outlet{}_{}.csv'.format(outlet_number, chosen_raw_material_sku), index = False)



    # PLOTS

    fig1 = m.plot(forecast)
    fig2 = m.plot_components(forecast)

    plot_plotly(m, forecast)
    plot_components_plotly(m, forecast)

    plt.show()
