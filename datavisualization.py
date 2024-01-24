from data_cleaning import data_cleaning
import plotly.express as px
from PIL import Image
import plotly.figure_factory as ff
import numpy as np

def data_vis():
    data = data_cleaning()
    print(data)

    categ = []
    numer = []
    
    for col in data.columns:
        if data.dtypes[col] == object:
            categ.append(col)
        else:
            numer.append(col)

    print("categorical--------------------",categ)
    print("numerical---------------", numer)

    #remove outliers using IQR method
    outliers_present = ['PAYMENTS', 'PURCHASES', 'PURCHASES_TRX', 'ONEOFF_PURCHASES_FREQUENCY', 'MINIMUM_PAYMENTS', 'INSTALLMENTS_PURCHASES', 'CREDIT_LIMIT', 'CASH_ADVANCE_TRX', 'CASH_ADVANCE', 'BALANCE', 'BALANCE_FREQUENCY']
    for value in outliers_present:
        percentile25 = data[value].quantile(0.25)
        percentile75 = data[value].quantile(0.75)
        iqr = percentile75 - percentile25
        upper_limit = percentile75 + 1.5 * iqr
        lower_limit = percentile25 - 1.5 * iqr
        data[value] = np.where(
            data[value] > upper_limit,
            upper_limit,
            np.where(
                data[value] < lower_limit,
                lower_limit,
                data[value]
            ))

    for i in numer:
        fig = px.histogram(data, y=i)
        fig.update_layout(template='plotly_dark')
        fig.update_xaxes(showgrid=False, zeroline=False)
        fig.update_yaxes(showgrid=False, zeroline=False)
        # fig.show()
        fig.write_image(f"{i}_hist.jpg")
        # a.append(fig)


    for i in numer:
        fig = px.box(data, y=i)
        fig.update_layout(template='plotly_dark')
        #fig.update_layout(plot_bgcolor = "plotly_dark")
        fig.update_xaxes(showgrid=False,zeroline=False)
        fig.update_yaxes(showgrid=False,zeroline=False)
        # fig.show()
        fig.write_image(f"{i}_box.jpg")

    y=data.corr().columns.tolist()
    z=data.corr().values.tolist()
    z_text = np.around(z, decimals=4) # Only show rounded value (full value on hover)
    fig = ff.create_annotated_heatmap(z,x=y,y=y,annotation_text=z_text,colorscale=px.colors.sequential.Cividis_r,showscale=True)
    fig.update_layout(template='plotly_dark', width=1500, height=1000)
    # fig.show()
    fig.write_image("img.jpg")

    return data
data_vis()
