from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import ensure_csrf_cookie
import os
import os.path
import request
import requests
import json
from requests.auth import HTTPDigestAuth
import cx_Oracle


def essjob(request):
	'''
	print(request)
	path1=request.body
	my_json = path1.decode('utf8').replace("'", '"')
	print(my_json)
	data1 = json.loads(my_json)
	file= data1['fileName']'''
	'''
	con = cx_Oracle.Connection("shubhver/Rtyuiop@2019@uerdx8001-vip.us.oracle.com:1554/ALPHA_ADHOC.us.oracle.com")
	cursor = con.cursor()
	a = cursor.execute("""Select * from ra_interface_lines_all where interface_line_attribute1='33502039'""")
	print(a)'''
	S0=''
	S1=''
	S2=''
	S4=''
	S5='' 


	url="https://efip-dev1.fa.us6.oraclecloud.com:443/fscmService/ErpIntegrationService"
	headers = {'content-type': 'text/xml'}
	body = """<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
	xmlns:typ="http://xmlns.oracle.com/apps/financials/commonModules/shared/model/erpIntegrationService/types/">
	<soapenv:Header/>
	<soapenv:Body>
	   <typ:submitESSJobRequest>
		  <typ:jobPackageName>/oracle/apps/ess/financials/receivables/transactions/autoInvoices/</typ:jobPackageName>
		  <typ:jobDefinitionName>AutoInvoiceMasterEss</typ:jobDefinitionName>
		  <!--Zero or more repetitions:-->
			  <typ:paramList>1</typ:paramList>
			 <typ:paramList>300001096431127</typ:paramList>
			 <typ:paramList>300000311435966</typ:paramList>
			 <typ:paramList>12/11/19</typ:paramList>
			 <typ:paramList>null</typ:paramList>
			 <typ:paramList>null</typ:paramList>
			 <typ:paramList>null</typ:paramList>
			 <typ:paramList>null</typ:paramList>
			 <typ:paramList>null</typ:paramList>
			 <typ:paramList>null</typ:paramList>
			 <typ:paramList>null</typ:paramList>
			 <typ:paramList>null</typ:paramList>
			 <typ:paramList>null</typ:paramList>
			 <typ:paramList>null</typ:paramList>
			 <typ:paramList>null</typ:paramList>
			 <typ:paramList>null</typ:paramList>
			 <typ:paramList>null</typ:paramList>
			 <typ:paramList>null</typ:paramList>
			 <typ:paramList>null</typ:paramList>
			 <typ:paramList>null</typ:paramList>
			 <typ:paramList>null</typ:paramList>
			 <typ:paramList>null</typ:paramList>
			 <typ:paramList>null</typ:paramList>
			 <typ:paramList>Y</typ:paramList>
			 <typ:paramList>null</typ:paramList>
	   </typ:submitESSJobRequest>
	</soapenv:Body>
	</soapenv:Envelope>"""


	response = requests.post(url,data=body,headers=headers,auth=('oalo2c_ww@oracle.com', 'Owcw2!365'))
	print(response)
	print(response.content)
	
	list13 = []
	list13.append(S0)
	
	return HttpResponse(response)