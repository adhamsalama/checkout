from matplotlib import pyplot as plt
import io
import urllib, base64
import operator

def plot_barchart(data, title, xlabel, ylabel="Money Spent", xmin=0, highlight=None, highest_value=None):
    """Input: dictionary that contains the data
        Output: a uri (image) of a barchart"""
    plt.style.use("seaborn")
    plt.figure(figsize=(10, 4))
    barlist = plt.bar(data.keys(), data.values()) # bar(*zip(*data.items())) also works
    if highlight:
        barlist[highlight].set_color("g")
    if highest_value:
        barlist[highest_value].set_color("r")
    #for index, value in enumerate(list(data.values())): # supposed to show values on bars
    #    plt.text(value, index, str(value))
    plt.xlim(xmin=xmin)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(range(len(data)), list(data.keys()))
    fig = plt.gcf()
    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = 'data:image/png;base64,' + urllib.parse.quote(string)
    plt.clf()
    return uri
    

def dict_max_value_index(m):
    max_ = -1
    i = 0
    index = -1
    for value in m.values():
        if value > max_:
            max_ = value
            index = i
        i += 1
    return index