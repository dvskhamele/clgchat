import uuid
def tosend(request):
	"""k={"CorrelationID": request.POST["correlation_id"],
			"BusinessType": request.POST["business_type"],
			"DealId": request.POST["deal_id"],
			"VehicleMakeCode": request.POST["vehical_make_code"],
			"VehicleModelCode": request.POST["vehical_model_code"],
			"VehicleDescription": request.POST["vehical_description"],
			"RTOLocationCode": request.POST["rto_location_code"],
			"ExShowRoomPrice": request.POST["ex_showroom_price"],
			"IsNoPrevInsurance": request.POST["is_no_prev_insurance"],
			"Tenure": request.POST["tenure"],
			"ManufacturingYear": request.POST["manufacturing_year"],
			"DeliveryOrRegistrationDate": request.POST["delivery_or_registration_date"],
			"FirstRegistrationDate": request.POST["first_registration_date"],
			"IsTransferOfNCB": request.POST["is_transfer_of_ncb"],
			"TransferOfNCBPercent": request.POST["transfer_of_ncb_percent"],
			"BonusOnPreviousPolicy": request.POST["bonus_on_previous_policy"],
			"PreviousPolicyStartDate": request.POST["previous_policy_start_date"],
			"PreviousPolicyEndDate": request.POST["previous_policy_end_date"],
			"ClaimOnPreviousPolicy": request.POST["claim_on_previous_policy"],
			"TotalNoOfODIClaims": request.POST["total_no_of_odi_claims"],
			"PreviousPolicyType": request.POST["previous_policy_type"],
			"PreviousInsurerName": request.POST["previous_insurance_name"],
			"PreviouslyPolicyNumber": request.POST["previous_policy_number"],
			"PreviousVehicleSaleDate": request.POST["previously_policy_sale_date"],
			"PreviouslyPolicyTenure": request.POST["previously_policy_tenure"],
			"PolicyStartDate": request.POST["policy_start_date"],
			"PolicyEndDate": request.POST["policy_end_date"],
			"CustomerType": request.POST["customer_type"],
			"IsValidDrivingLicense": request.POST["is_valid_driving_licence"],
			"IsHaveElectricalAccessories": request.POST["is_have_electrical_accessories"],
			"SIHaveElectricalAccessories": request.POST["si_have_electrical_accessories"],
			"IsHaveNonElectricalAccessories": request.POST["is_have_non_electrical_accessories"],
			"SIHaveNonElectricalAccessories": request.POST["si_have_non_electrical_accessories"],
			"TPPDLimit": request.POST["tppd_limit"],
			"IsLegalLiabilityToPaidDriver": request.POST["is_legal_liability_to_paid_driver"],
			"IsLegalLiabilityToPaidEmpolyee": request.POST["is_legal_liability_to_paid_empolyee"],
			"NoOfEmpolyee": request.POST["no_of_empolyee"],
			"IsPACoverUnnamedPassenger": request.POST["is_pa_cover_unnamed_passenger"],
			"SIPACoverUnnamedPassenger": request.POST["sipa_cover_unnamed_passenger"],
			"IsMoreThanOneVehicle": request.POST["is_more_than_one_vehical"],
			"IsPACoverOwnerDriver": request.POST["is_pa_cover_owner_driver"],
			"IsVoluntaryDeductible": request.POST["is_voluntary_deductible"],
			"VoluntaryDeductiblePlanName": request.POST["voluntry_deductible_plan_name"],
			"IsAutomobileAssocnFlag": request.POST["is_automobile_assocn_flag"],
			"IsAntiTheftDisc": request.POST["is_anti_theft_disk"],
			"IsHandicapDisc": request.POST["is_handicap_disk"],
			"ExtensionCountryName":request.POST["extension_country_name"],
			"IsExtensionCountry": request.POST["is_extension_country"],
			"ZeroDepPlanName": request.POST["zero_dep_plan_name"],
			"IsRTIApplicableFlag": request.POST["is_rti_applicable_flag"],
			"IsConsumables": request.POST["is_consumables"],
			"IsEngineProtectPlus": request.POST["is_engine_protect_plus"],
			"RSAPlanName": request.POST["rsa_plan_name"],
			"KeyProtectPlan": request.POST["key_protect_plan"],
			"LossOfPersonalBelongingPlanName": request.POST["loss_of_personal_belonging_plan_name"],
			"OtherLoading": request.POST["other_loading"],
			"OtherDiscount": request.POST["other_discount"],
			"GSTToState": request.POST["gstto_state"],
						"TPTenure" : request.POST["tp_tenure"],
			"IsPACoverUnnamedPassenger":"true",
			"SIPACoverUnnamedPassenger":100000,
			}"""

	"""k={
						#"VehicleModelCode" : "380",
						#"RTOLocationCode" : "192",
						#U "ManufacturingYear" : "2017",
						#U "Tenure" : "1",
						#U "CustomerType" : "INDIVIDUAL",
						#U "VehicleMakeCode" : "31",
						#U "DeliveryOrRegistrationDate" : "2018/09/02",
						#U " PolicyStartDate" : "2018/09/19",
						#U "PolicyEndDate" : "2019/09/18",
			
						#U "ExShowRoomPrice" : "73689",
						#U "BusinessType" : "New Business",
			
						#C "GSTToState" : "MAHARASHTRA",
			
						#"TPTenure" : "5",
						#"DealId" : "DL-3005/411041",
						
						"CorrelationId":str(uuid.uuid4()),
						}
				return k"""
	k = {
			"BusinessType": request.POST["select"],
			"DealId": "DL-3005/1483341",
			"VehicleMakeCode": request.POST["modelc"],
			"VehicleModelCode":request.POST["makec"],
			"DeliveryOrRegistrationDate": request.POST["delivery_date"],
			"ManufacturingYear": request.POST["manufacturing_year"],
			"Tenure": request.POST["tenure"],
			"TPTenure": request.POST["tptenure"],
			"ExShowRoomPrice": request.POST["price"],
			"FirstRegistrationDate": request.POST["reg_date"],
			"PolicyStartDate":request.POST["start_date"],
			"PolicyEndDate":request.POST["end_date"],
			"GSTToState":str(request.POST["gst"]).upper(),
			"CustomerType":str(request.POST["customer"]).upper(),
			"CorrelationId":str(uuid.uuid4()),

			"RTOLocationCode": request.POST["rto_code"],
			"IsNoPrevInsurance": request.POST["insurance"],


"RegistrationNumber":request.POST["reg_number"],



	}
	return k
	k={
"BusinessType":"Roll Over",

"DealId":"DL-3005/1483341",
"DeliveryOrRegistrationDate":"2018-07-15",
"FirstRegistrationDate":"2018-07-15",
"PolicyStartDate":"2018-07-16",
"PolicyEndDate":"2019-07-15",
"ManufacturingYear":"2018",
"VehicleMakeCode":"31",

"GSTToState":"MAHARASHTRA",
"CustomerType":"INDIVIDUAL",

"VehicleModelCode":"380",
"RTOLocationCode":"192",
"ExShowRoomPrice":"73689",
"CorrelationId":"49baa781-2fde-472d-a326-4f097f26b9aa",
"IsNoPrevInsurance":"false"
}
	return k

    