from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import plotly.offline as opy
import plotly.graph_objs as go
import sys
sys.path.append(sys.path[0] + "\\analytics")
from analytics.models import EndOfDayDataTable

def toolspage(request):
	return render(request, 'tools/tools.html', {})

class Graph:
    def __init__(self):
        pass
    def parse_query(self, query_set):
        query_date = query_set.order_by('date')
        x = []
        y = [] 
        for item in query_date:
            x.append(item.date)
            y.append(item.open)
        return x, y

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

def graph_search(request):
	if request.method == 'GET':
		graph_object = Graph()
		graph_string = ""
		req = request.GET.get('search_box', None)
		data_model = EndOfDayDataTable.objects.filter(symbol__search=req)
		if(len(data_model) > 0):
			graph_string = graph_object.get_end_of_day_data(data_model)
			return render(request, "tools/graph.html", {"graph": graph_string})
			##run the candlelight stuff
			print(data_model)
		else:
			return render(request, "tools/graph.html")
	else:
		print("It's a get request!\n")
	return render(request, "tools/graph.html")