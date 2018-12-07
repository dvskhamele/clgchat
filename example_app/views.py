#sudo fuser -k 8000/tcp
import json
from django.views.generic.base import TemplateView
from django.views.generic import View
from django.http import JsonResponse
from chatterbot import ChatBot
from chatterbot.ext.django_chatterbot import settings
from example_app.chatbot_train import *
import requests
from socket import error as SocketError
import time
from . secondstep import *
from . thirdstep import *
from django.shortcuts import render
from . models import *
from chatterbot.ext import django_chatterbot
import googlemaps

import random

import gspread
from oauth2client.service_account import ServiceAccountCredentials

# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('example_app/client_secret.json', scope)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.


from django.views.decorators.csrf import ensure_csrf_cookie




class Feedback(View):
    def get(self, request, *args, **kwargs):
        sheet = client.open_by_url("https://docs.google.com/spreadsheets/d/1s55ue2sZWpGyKX4h5PdZ21ucFSBJRHUtKxUNOeanzms/edit?usp=sharing").sheet1

        print("sheet.col_values(1)",sheet.col_values(1))
        print("request.GET\n",request.GET)
        data_string = request.GET.get('data')
        data_dict = json.loads(data_string)
        print("data_string\n",data_string)
        print("data_dict\n",data_dict)
        if request.method == "GET":
                    name = data_dict['you']
                    nominee = data_dict['nominee_name']
                    relation = data_dict['relation']
        r=0
        print("name",name)
        print()        
        print()        
        if not name in sheet.col_values(1):
                    nth = len(sheet.col_values(1))+1
                    sheet.append_row([name,"-","-"])
                    print("col_values",sheet.col_values(1))

        for rv in sheet.col_values(1):
            r=r+1
            if rv == name:
                    sheet.update_cell(r, 3, nominee)
                    sheet.update_cell(r, 2, relation)
                    break


        response_data = {
        "name":name,"address":nominee,"contact":relation}

        return JsonResponse(response_data)



class Address(View):
    def get(self, request, *args, **kwargs):
        sheet = client.open_by_url("https://docs.google.com/spreadsheets/d/1_qQjUcfKLZDtmZKK8tF2n12rTbO3JTU90pTXN6WisnQ/edit#gid=0").sheet1

        print("sheet.col_values(1)",sheet.col_values(1))
        print("request.GET\n",request.GET)
        data_string = request.GET.get('data')
        data_dict = json.loads(data_string)
        print("data_string\n",data_string)
        print("data_dict\n",data_dict)
        if request.method == "GET":
                    name = data_dict['you']
                    nominee = data_dict['nominee_name']
                    relation = data_dict['relation']
        r=0
        print("name",name)
        print()        
        print()        
        if not name in sheet.col_values(1):
            response_data = {"name":"NotFound",}

            return JsonResponse(response_data)


        for rv in sheet.col_values(1):
            r=r+1
            if rv == name:
                    p_nominee = sheet.row_values(3)[r]
                    p_relation = sheet.row_values(4)[r]
                    sheet.update_cell(r, 3, nominee)
                    sheet.update_cell(r, 4, relation)
                    sheet.update_cell(r, 16, "No")
                    sheet.update_cell(r, 17, "Done By ChatInsure Bot")
                    sheet.update_cell(r, 18, random.choice(["Under Processing", "Under Verification", "Transaction"]))
                    break


        response_data = {"p_address":p_nominee, "p_contact":p_relation,
        "name":name,"address":nominee,"contact":relation}

        return JsonResponse(response_data)




class Nominee(View):
    def get(self, request, *args, **kwargs):
        client = gspread.authorize(creds)
        sheet = client.open_by_url("https://docs.google.com/spreadsheets/d/1_qQjUcfKLZDtmZKK8tF2n12rTbO3JTU90pTXN6WisnQ/edit#gid=0").sheet1

        print("sheet.col_values(1)",sheet.col_values(1))
        print("request.GET\n",request.GET)
        data_string = request.GET.get('data')
        data_dict = json.loads(data_string)
        print("data_string\n",data_string)
        print("data_dict\n",data_dict)
        if request.method == "GET":
                    name = data_dict['you']
                    nominee = data_dict['nominee_name']
                    relation = data_dict['relation']
        r=0
        print("name",name)
        print()        
        print()        
        if not name in sheet.col_values(1):
            response_data = {"name":"NotFound",}

            return JsonResponse(response_data)

        for rv in sheet.col_values(1):
            r=r+1
            if rv == name:
                    p_nominee = sheet.row_values(1)[r]
                    p_relation = sheet.row_values(1)[r]
                    sheet.update_cell(r, 5, nominee)
                    sheet.update_cell(r, 6, relation)
                    sheet.update_cell(r, 16, "No")
                    sheet.update_cell(r, 17, "Done By ChatInsure Bot")
                    sheet.update_cell(r, 18, random.choice(["Under Processing", "Under Verification", "Transaction"]))
                    break


        response_data = {"p_nominee":p_nominee, "p_relation":p_relation,
        "name":name,"nominee":nominee,"relation":relation}

        return JsonResponse(response_data)






class FileClaim(View):
    def get(self, request, *args, **kwargs):
        sheet = client.open_by_url("https://docs.google.com/spreadsheets/d/1_qQjUcfKLZDtmZKK8tF2n12rTbO3JTU90pTXN6WisnQ/edit#gid=0").sheet1

        print("sheet.col_values(1)",sheet.col_values(1))
        print("request.GET\n",request.GET)
        data_string = request.GET.get('data')
        data_dict = json.loads(data_string)
        print("data_string\n",data_string)
        print("data_dict\n",data_dict)
        if request.method == "GET":
                    name = data_dict['you']
        r=0
        print("name",name)
        print()        
        print()        

        if not name in sheet.col_values(1):
            response_data = {"name":"NotFound",}

            return JsonResponse(response_data)


        for rv in sheet.col_values(1):
            r=r+1
            if rv == name:
                    all_values = sheet.row_values(r)
                    print("all_values\n", all_values)
                    u_name = sheet.row_values(r)[1]
                    print("u_name\n", u_name)
                    u_bike = sheet.row_values(r)[9] + " " + sheet.row_values(r)[10]
                    print("u_bike\n", u_bike)

                    break


        response_data = {
        "u_name":u_name, "u_bike":u_bike}

        return JsonResponse(response_data)

class ChatterBotAppView(TemplateView):
    #print(django_chatterbot.models.Response.objects.filter(id__gt=350).delete())
    template_name = 'FIRSTCHATBOX.html'

class EveryStyle(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'style.css')



def get_html(url, headers, post_data, retry_count=0):
    try:
        
        photon_requests_session = requests.sessions.Session()
        photon_requests_session.verify = certifi.where()
        response = photon_requests_session.post(url, data= post_data ,verify=False, headers=headers)
        response = response
        print("Response: ",response)
        print()
        print()
        return response
    except SocketError as e:
        if retry_count == 5:
            raise e
        print("Waiting now")
        print(e)
        time.sleep(150)
        print("Waiting now")
        get_html(url=url, post_data=post_data, headers=headers, retry_count=retry_count + 1)


import certifi

"""
motor api - esbmotor
payment api - esbpayment
pdf generation api - esbgneric
"""

class ClearAll(View):
    """    
    API endpoint to interact with http://cldilbizapp01.cloudapp.net:9000/cerberus/connect/token
    """

    def get(self, request, *args, **kwargs):
        print(django_chatterbot.models.Response.objects.filter(id__gt=350).delete())
        response_data = {}
        return JsonResponse(response_data)

class Makes(View):

    def get(self, request, *args, **kwargs):
        make_list = Make.objects.all()
        makes = []
        for make in make_list:
            if make.exprice != 0:
                makes.append(make.name) 
        makes = list(set(makes))
        response_data = {"makes":makes}
        return JsonResponse(response_data)


class SetUp(View):

    def get(self, request, *args, **kwargs):
        RTO.objects.all().delete()
        from . import rto_files
        from . import pandas_files
        response_data = {"makes":"makes"}
        return JsonResponse(response_data)


class Models(View):

    def get(self, request, *args, **kwargs):
        make_list = Make.objects.all()
        models = []
        for make in make_list:
            if make.exprice != 0:
                models.append(make.model) 
        models = list(set(models))
        response_data = {"models":models}
        return JsonResponse(response_data)


class RTOs(View):

    def get(self, request, *args, **kwargs):
        make_list = RTO.objects.all()
        print(make_list)
        models = []
        for make in make_list:
            models.append(make.loct) 
        models = list(set(models))
        response_data = {"rtos":models}
        return JsonResponse(response_data)


class ExpriceOf(View):

    def get(self, request, *args, **kwargs):
        if request.method == "GET":
            data_string = request.GET.get('data')
            data_dict = json.loads(data_string)
            make = Make.objects.filter(model=data_dict["make"])[0]
            response_data = {"exprice":make.exprice,"makec":make.namec,"modelc":make.modelc,"model":make.model, "make":make.name}
            return JsonResponse(response_data)


class LoctCodeOf(View):

    def get(self, request, *args, **kwargs):
        if request.method == "GET":
            data_string = request.GET.get('data')
            data_dict = json.loads(data_string)
            make = RTO.objects.filter(loct=data_dict["make"])[0]
            response_data = {"loct_code":make.loct_code,"city_code":make.city_code,"state_code":make.state_code}
            print(response_data)
            return JsonResponse(response_data)

class DirectToNearest(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'schools_navigate.html')



def tosend(request):
    k = """<?xml version="1.0" encoding="UTF-8"?>
<cibil_indv_dedup><sourceappcode>LOS</sourceappcode><RqUID>"""+str(uuid.uuid4())+"""</RqUID><message_type_cd>KB015</message_type_cd><enquiry_purpose>00</enquiry_purpose><enquiry_amount>3900000</enquiry_amount>
<first_name>"""+ request.POST['full_name']+"""</first_name>
<middle_name>"""+ request.POST['middle_name']+"""</middle_name><last_name>"""+ request.POST['last_name']+"""</last_name>
<date_of_birth>"""+ request.POST['date']+"""</date_of_birth>
<gender>"""+ request.POST['gender']+"""</gender>
<addr1>"""+ request.POST['addr1']+"""</addr1>
<addr2>"""+ request.POST['addr2']+"""</addr2>
<addr3>"""+ request.POST['addr3']+"""</addr3>
<state>"""+ request.POST['state']+"""</state>
<pin_code>"""+ request.POST['pin_code']+"""</pin_code>
<res_phone_no>"""+ request.POST['number']+"""</res_phone_no>
<employer_name></employer_name><office_addr1></office_addr1>
<office_state></office_state><office_pin_code></office_pin_code>
<office_phone_no></office_phone_no>
<pan>"""+ request.POST['pan_detail']+"""</pan>
<passport_no></passport_no>
<credit_card_no></credit_card_no><account_no></account_no>
<scores_request>"""+ request.POST['score']+"""</scores_request>
</cibil_indv_dedup>"""  

    return k

def cibiltest():
    k = """<?xml version="1.0" encoding="UTF-8"?>
<cibil_indv_dedup><sourceappcode>LOS</sourceappcode><RqUID>"""+str(uuid.uuid4())+"""</RqUID><message_type_cd>KB015</message_type_cd><enquiry_purpose>00</enquiry_purpose><enquiry_amount>3900000</enquiry_amount><first_name>ANILKUMAR</first_name>
<middle_name>BALSHANKAR</middle_name><last_name>REDDY</last_name><date_of_birth>06-Jul-1979</date_of_birth><gender>2</gender><addr1>PRATIBHA APPT KHARI
KUI PASE</addr1><addr2>VILLAGE
KHRALU</addr2><addr3></addr3><state>24</state><pin_code>384325</pin_code>
<res_phone_no>9624335555</res_phone_no><employer_name></employer_name><office_addr1></office_addr1>
<office_state></office_state><office_pin_code></office_pin_code>
<office_phone_no></office_phone_no><pan>AJOPR1655F</pan><passport_no></passport_no>
<credit_card_no></credit_card_no><account_no></account_no>
<scores_request>04</scores_request></cibil_indv_dedup>"""  
    return k

post_data = cibiltest()
headers = {'Content-Type': 'application/x-www-form-urlencoded', 'Method':"POST"}
headers["Content-Type"] = 'application/xml'
url1 = 'https://apigwuat.kotak.com:8443/API/Cibil_enq'
response1 = get_html(url=url1, headers=headers,post_data=post_data)
print(response1.text)





"""
def tosend(request):
    OldPolicy = request.POST["old_policy"]
    k = {
            "IsNoPrevInsurance": "false",
            "BusinessType": "Roll Over",
            "DealId": "DL-3005/1483341",
            "CorrelationId":str(uuid.uuid4()),
            "FirstRegistrationDate": '10/10/2018',
            "GSTToState":str("MAHARASHTRA").upper(),
            "ExShowRoomPrice": request.POST["price"],
            "CustomerType":str(request.POST["radio"]).upper(),

            "RTOLocationCode": str(192),

            "NewDate": request.POST["new_date"],

            "VehicleMakeCode": str(31),
            "VehicleModelCode":str(380),
            "Tenure": "1",
           # "TPTenure" : "5",

            "ManufacturingYear": 'request.POST["manufacturing_year"]',
            "PolicyStartDate":request.POST["new_date"],
            "PolicyEndDate":request.POST["new_date"],

            "IsPACoverUnnamedPassenger":"true",
            "IsPACoverOwnerDriver":"true",
            "SIPACoverUnnamedPassenger":100000,
            "paCoverForOwnerDriver": 100000,
                }
    k["DeliveryOrRegistrationDate"] = k["FirstRegistrationDate"]
    k["ExShowRoomPrice"] = str(Make.objects.get(namec = k['VehicleModelCode']).exprice)
    print('k["ExShowRoomPrice"] \n', k["ExShowRoomPrice"])
    k["ManufacturingYear"] = k["PolicyEndDate"][-4:]
    
    k["PolicyEndYear"] = int(k["ManufacturingYear"]) + int(k["Tenure"])

    end_date = request.POST["new_date"][:-4], str(k["PolicyEndYear"])

    end_date = "".join(end_date)
    end_date = datetime.datetime.strptime(end_date, "%d/%m/%Y").date()
    print("end_date\n",end_date)
    end_date = str(end_date - datetime.timedelta(1))
    k["PolicyEndDate"] = end_date

    k["FirstRegistrationDate"] = k["PolicyStartDate"]
    print("end_date -1\n",end_date)

    del k["NewDate"]
    
    if OldPolicy == "false":
        k["BusinessType"] = "New Business"

    if OldPolicy == "true":
        k["BusinessType"] = "Roll Over"
    k["DeliveryOrRegistrationDate"]="2018-07-15"
    k["FirstRegistrationDate"]="2018-07-15"
    k["PolicyStartDate"]="2018-07-16"
    k["PolicyEndDate"]="2019-07-15"
    return k
"""





from django.http import HttpResponse

class Index(View):
    """    
    API endpoint to interact with http://cldilbizapp01.cloudapp.net:9000/cerberus/connect/token
    """

    def get(self, request, *args, **kwargs):

        post_data = tosend(request)
        headers = {'Content-type': 'application/x-www-form-urlencoded', 'Method':"POST"}
        headers["Content-type"] = 'application/json'
        url = 'https://apigwuat.kotak.com:8443/API/Cibil_enq'
        response = get_html(url=url, headers=headers,post_data=post_data)
        response = json.loads(response.text)
        print(response)
        return render(request, 'form.html', {'response' : json.loads(response.text)})

    def post(self, request, *args, **kwargs):
        """return render(request, 'form.html')
                        
                                def post(self, request, *args, **kwargs):"""
        post_data = {'username': 'Thefinsol', 'password':'t43f!n501', 'grant_type':'password',
        'scope':'esbmotor','client_id':'ro.Thefinsol','client_secret':'ro.t43f!n501',}
        """,'grant_type':'password',
        'scope':'esbgeneric','client_id':'ro.Thefinsol','client_secret':'ro.t43f!n501',"""
        headers = {'Content-type': 'application/x-www-form-urlencoded', 'Method':"POST"}
        url = 'https://cldilbizapp02.cloudapp.net:9001/cerberus/connect/token'
        print()
        print()
        print(url)
        print()
        print()
        response = get_html(url=url, headers=headers,post_data=post_data)
        try:
            response = json.loads(response.text)
        except:
            return HttpResponse(response.text)

        url = 'https://cldilbizapp02.cloudapp.net:9001/ILServices/Motor/v1/Proposal/TwoWheelerCalculatePremium'
        headers["Authorization"] = "Bearer "+response["access_token"]
        headers["Content-type"] = 'application/json'
        print()
        post_data["scope"] = "esbmotor"
        sent = tosend(request)
        to_send = { **post_data, **sent }
        print("to_send", to_send)
        response = get_html(url=url, headers=headers,post_data=str(to_send))

        try:
            response = json.loads(response.text)
        except:
            return HttpResponse(response.text)

        print()
        print("\n\n\n2 Last response: ", response)
        print("\n\n\n2 Last response: ", to_send )
        #response = {{ **json.loads(response.text), **to_send }}


        #Third_step
        """url = 'https://cldilbizapp02.cloudapp.net:9001/ILServices/Motor/v1/Proposal/TwoWheelerCreateProposal'
                                three_send = threesend(request)
                                to_send = { **post_data, **three_send }
                                print()
                                print()
                                print("3 send", to_send)
                                response = get_html(url=url, headers=headers,post_data=str(to_send))
                                print("3 Last response: ",response.text)"""
        return render(request, 'form.html', {'response' : response, 'requested':sent})

class ThirdStep(View):
    """    
    API endpoint to interact with http://cldilbizapp01.cloudapp.net:9000/cerberus/connect/token
    """
    def post(self, request, *args, **kwargs):

        """return render(request, 'form_proposal.html')
                        
                                def post(self, request, *args, **kwargs):"""
        post_data = {'username': 'Thefinsol', 'password':'t43f!n501', 'grant_type':'password',
        'scope':'esbmotor','client_id':'ro.Thefinsol','client_secret':'ro.t43f!n501',}
        """,'grant_type':'password',
        'scope':'esbgeneric','client_id':'ro.Thefinsol','client_secret':'ro.t43f!n501',"""
        headers = {'Content-type': 'application/x-www-form-urlencoded', 'Method':"POST"}
        url = 'https://cldilbizapp02.cloudapp.net:9001/cerberus/connect/token'
        response = get_html(url=url, headers=headers,post_data=post_data)
        response = json.loads(response.text)
        url = 'https://cldilbizapp02.cloudapp.net:9001/ILServices/Motor/v1/Proposal/TwoWheelerCalculatePremium'
        headers["Authorization"] = "Bearer "+response["access_token"]
        headers["Content-type"] = 'application/json'
        print("Befor Last response: ",headers)
        print()
        post_data["scope"] = "esbmotor"

        #Third_step
        url = 'https://cldilbizapp02.cloudapp.net:9001/ILServices/Motor/v1/Proposal/TwoWheelerCreateProposal'
        three_send = threesend(request)
        to_send = { **post_data, **three_send }
        print()
        print()
        print("3 send", to_send)
        response = get_html(url=url, headers=headers,post_data=str(to_send))
        print("3 Last response: ",response.text)
        return render(request, 'form.html', {'response' : json.loads(response.text),'requested':three_send})

class PolicyView(View):

    def get(self, request, *args, **kwargs):
        prod = Prod.objects.all()
        """idv="High",cover="-1"""
        print(prod)
        return JsonResponse({
                'text': [
                    str(prod)
                ]
            }, status=200)


CHATTERBOT = {
    'name': 'Tech Support Bot',
    'logic_adapters': [
        #'chatterbot.logic.MathematicalEvaluation',
        #'chatterbot.logic.TimeLogicAdapter',
        {
            'import_path': 'chatterbot.logic.BestMatch'
        },
        {
            'import_path': 'chatterbot.logic.LowConfidenceAdapter',
            'threshold': 0.60,
            'default_response': 'Sorry, I did not recognize it.'
        }
    ],
    'trainer': 'chatterbot.trainers.ListTrainer',
    'training_data': [
         'chatterbot.corpus.english.greetings'
    ],
    'django_app_name': 'django_chatterbot'
}

class ChatterBotApiView(View):
    """
    Provide an API endpoint to interact with ChatterBot.
    """

    chatterbot = ChatBot(**CHATTERBOT)
    
    def post(self, request, *args, **kwargs):
        """
        Return a response to the statement in the posted data.

        * The JSON data should contain a 'text' attribute.
        """
        input_data = json.loads(request.read().decode('utf-8'))
        print(django_chatterbot.models.Response.objects.filter(id__gt=350).delete())

        if 'text' not in input_data:
            return JsonResponse({
                'text': [
                    'The attribute "text" is required.'
                ]
            }, status=400)
            

        response = self.chatterbot.get_response(input_data)

        response_data = response.serialize()

        print()
        print("input_data",input_data,"\n",response_data)
        print()

        return JsonResponse(response_data, status=200)

    def get(self, request, *args, **kwargs):
        """
        Return data corresponding to the current conversation.
        """
        return JsonResponse({
            'name': self.chatterbot.name
        })


"""
     import requests
     import json

     url = 'https://clients6.google.com/rpc'
     values = {
         "method": "pos.plusones.get",
         "id": "p",
         "params": {
                    "nolog": True,
                    "id": "http://www.newswhip.com",
                    "source": "widget",
                    "userId": "@viewer",
                    "groupId": "@self"
                   },
          "jsonrpc": "2.0",
          "key": "p",
          "apiVersion": "v1"
     }
     headers = {"content-type" : "application/json"}

     req = requests.post(url, data=json.dumps(values), headers=headers)
     print req.text

"""



class TrainBotApiView(View):
    """
    Provide an API endpoint to interact with ChatterBot.
    """

    chatterbot = ChatBot(**CHATTERBOT)
    
    def get(self, request, *args, **kwargs):
        chatterbot = trainit(self.chatterbot)
        chatterbot = trainit(self.chatterbot)
        """
        Return a response to the statement in the posted data.

        * The JSON data should contain a 'text' attribute.
        """
        input_data = json.loads(request.read().decode('utf-8'))
        print(django_chatterbot.models.Response.objects.filter(id__gt=last_response).delete())

        if 'text' not in input_data:
            return JsonResponse({
                'text': [
                    'The attribute "text" is required.'
                ]
            }, status=400)

        response = self.chatterbot.get_response(input_data)

        response_data = response.serialize()

        return JsonResponse(response_data, status=200)
