from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import plotly.offline as opy
import plotly.graph_objs as go
import sys
sys.path.append(sys.path[0] + "\\analytics")
from analytics.models import EndOfDayDataTable
import pickle

def toolspage(request):
	return render(request, 'tools/tools.html', {})

def load_obj(name ):
    with open(name + '.pkl', 'rb') as f:
        return pickle.load(f)

class Graph:
    def __init__(self):
        pass
    def parse_query(self, query_set):
        query_date = query_set.order_by('date')
        date = []
        open = [] 
        high = []
        low = []
        close = []
        for item in query_date:
            date.append(item.date)
            open.append(item.open)
            high.append(item.high)
            low.append(item.low)
            close.append(item.close)
        return date, open, high, low, close

    def get_end_of_day_data(self, query_set):
        axis = self.parse_query(query_set)
        trace1 = go.Scatter(x=axis[0], y=axis[1], marker={'color': 'blue', 'symbol': 104, 'size': "10"},
                            mode="lines",  name='1st Trace')

        company = query_set[0].symbol 
        data=go.Data([trace1])
        layout=go.Layout(title="End of Day Data for " + str(company), xaxis={'title':'Date'}, yaxis={'title':'USD'})
        figure=go.Figure(data=data,layout=layout)
        div = opy.plot(figure, auto_open=False, output_type='div')

        context = div
        return context
    def get_end_of_data_candlestick(self, query_set):
        axis = self.parse_query(query_set)
        trace = go.Candlestick(x = axis[0],
                       open = axis[1],
                       high = axis[2],
                       low = axis[3],
                       close = axis[4])
        company = query_set[0].symbol 
        data = go.Data([trace])
        layout=go.Layout(title="End of Day Data for "+ company, xaxis={'title':'Date'}, yaxis={'title':'USD'})
        figure=go.Figure(data=data,layout=layout)
        div = opy.plot(figure, auto_open=False, output_type='div')

        context = div
        return context

@login_required
def graph_search(request):
    ad_params = ['', 'co', 'inc', 'corp', 'co.', 'inc.', 'corp.'] 
    if request.method == 'GET':
        company_names = load_obj(sys.path[0]+'\\tools\\constituents')
        graph_object = Graph()
        graph_string = []
        req = request.GET.get('search_box', None)
        initial_req = req
        data_model = EndOfDayDataTable.objects.filter(symbol__search=req)
        if(len(data_model) > 0):
            graph_string.append(graph_object.get_end_of_data_candlestick(data_model))
            graph_string.append(graph_object.get_end_of_day_data(data_model))
            return render(request, "tools/graph.html", {"graph": graph_string})
        else:
            for item in ad_params:
                req = initial_req.strip() + " " + item;
                print("now testing:", req)
                try:
                    data_point = company_names[req.strip().title()]
                    data_model = EndOfDayDataTable.objects.filter(symbol__search=company_names[req.strip().title()][0])
                    if(len(data_model) > 0):
                        graph_string.append(graph_object.get_end_of_data_candlestick(data_model))
                        graph_string.append(graph_object.get_end_of_day_data(data_model))
                        return render(request, "tools/graph.html", {"graph": graph_string})
                except:
                    continue
    else:
        print("It's a get request!\n")
    return render(request, "tools/graph.html")
