from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, Http404,JsonResponse
from openpyxl import load_workbook
from django.conf import settings
import xlrd

import json 

# Create your views here.


class HomePage(View):


    def costomerDetails(self,book):


        wsNames = ['Customer 1','Customer 2','Customer 3','Customer 4', ]
        theHolyGrail =  {}

        for customer in wsNames:
            ws = book[customer]
            #personal information
            personalDescription = []
            for cell in ws.iter_rows(min_row=1, max_row=3, min_col=2, max_col=2, values_only=True):
                # x = type(cell)
                # ('Martyn' ,'3, Covent Garden, London', 'XXXXXXXXX' )
                for x in cell: 
                    personalDescription.append(x)


        
            # consuumption details 
            consumptionDetails = []

            for cell in ws.iter_rows(min_row=6, max_row=8, min_col=2, max_col=3, values_only=True):
                for x in cell: 
                    consumptionDetails.append(x)

        

      
            theHolyGrail[customer] = {'personal' :personalDescription, 'consumption':  consumptionDetails}
        return theHolyGrail
    

    def get(self, request):
        # iterating over rows
        #create a workbook with the provided file
        book = load_workbook(settings.EX_FILE)
        #create a worksheet, its auotimcally start at 0
 
        context = {'data': self.costomerDetails(book)}

        # print(context)

        # return HttpResponse(context)
        return render(request, "Core/index.html", context)

    def post(self):
        raise Http404

################################################################

class MaxValue(View):
    # max value function 
    #get max value of category 
    def maxValue (self, book):
        wsNames = ['Calculations']
        holyG_2 = {}
        

        for customer in wsNames:
            ws = book[customer]

            #header
            headere = []
            for cell in ws.iter_rows(min_row=1, max_row=1, min_col=1, max_col=4, values_only=True):
                for x in cell:
                    headere.append(x)
             # data
            data = []
            for cell in ws.iter_rows(min_row=2, max_row=4, min_col=1, max_col=4, values_only=True):
                for x in cell:
                    data.append(x)
        # print (firstReading)
            holyG_2[customer] = {'header': header, 'data': data}
        return JsonResponse(holyG_2, safe=False)
    def get(self, request):
        #return a json response 
        book = load_workbook(settings.EX_FILE)
        #create a worksheet, its auotimcally start at 0
 
        context = {'data': self.maxValue(book)}

#         Rate Name	Price (£/kWh)
        # Day Rate	0.0732
        # Night Rate	0.055
        # Weekend Rate	0.063
        # Weekend Day Rate	0.067
        # Weekend Night Rate	0.063


        # print(context)

        # return HttpResponse(context)
        # return render(request, "Core/index.html", context)



        print (context )
        print("HHHHHHHHHHHHHHhhh")
        return render(request, "Core/index.html", context)


    def post(self):
        raise Http404
   

    
        
    


