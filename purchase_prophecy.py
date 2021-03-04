import pandas as pd
from fbprophet import Prophet
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from fbprophet.plot import plot_plotly, plot_components_plotly


outlet_number = 2

purchase_xls = pd.ExcelFile('Master Data (Purchase).xlsx')
purchase_data_raw = pd.read_excel(purchase_xls, 'Purchase - Outlet {}'.format(outlet_number))
raw_materials_sku_list = purchase_data_raw['SKU'].unique()
# print("raw_materials_sku_list: ", raw_materials_sku_list)

for chosen_raw_material_sku in raw_materials_sku_list:
    df = purchase_data_raw[purchase_data_raw['SKU'] == chosen_raw_material_sku].rename(columns = {'Quantity of Order Placed': 'y', 'Date of Purchase': 'ds'})

    material_count = len(df)
    split = round(0.7*material_count)

    train=df[:split]
    test=df[split+1:]

    m = Prophet(seasonality_mode='multiplicative')
    m.fit(train)

    future = m.make_future_dataframe(periods=365*2)

    forecast = m.predict(future)
    forecast.to_csv('purchase forecast datasets/outlet{}_{}_predicted.csv'.format(outlet_number, chosen_raw_material_sku), index = False)
    test.to_csv('purchase forecast datasets/outlet{}_{}_test.csv'.format(outlet_number, chosen_raw_material_sku), index = False)
