def plot_nan_colls(df):
    nan_columns = df.columns[df.isna().any()].to_list()
    sum_nuns = df.isna().sum().to_list()
    nan_columns_values = [i for i in sum_nuns if i > 0]
    plt.bar(nan_columns, nan_columns_values)


def remove_legend_heading(fig):
    fig.update_layout(legend={'title_text':''})
