# import json
# import time
# from datetime import datetime
# from django.http import *
# from myserver.mongodb import expense_collection, client
# from django.views.decorators.csrf import csrf_exempt
# from django.shortcuts import *


# # @csrf_exempt
# # def getExpense(request):
# #     cursor = expense_collection.find()
# #     documents = list(cursor)
# #     return HttpResponse(json.dumps(documents), content_type='application/json')


# @csrf_exempt
# def addNewEntry(request, section):
#     if request.method == 'POST':

#         body = json.loads(request.body)
#         try:
#             current_date = datetime.now().strftime("%Y-%m-%d")
#             value = body.get("value")
#             comment = body.get("comment")
#             typ = "debit" if value < 0 else "credit"
#             res = addEntryFun(current_date, value, comment, section, typ)
#             # print(res)
#             if res:
#                 return HttpResponse(json.dumps({"msg": res}), content_type='application/json')
#             else:
#                 return HttpResponseServerError(json.dumps({"msg": "Server Error"}), content_type='application/json')
#         except json.JSONDecodeError:
#             return HttpResponseBadRequest(json.dumps({"msg": "Invalid JSON data"}), content_type='application/json')
#         except:
#             return HttpResponseServerError(json.dumps({"msg": "Server Error"}), content_type='application/json')
#     else:
#         return HttpResponseServerError(json.dumps({"msg": "Server Error "}), content_type='application/json')


# @csrf_exempt
# def addNewSection(request):
#     if request.method == 'POST':
#         section = json.loads(request.body).get("section")
#         try:
#             doc = {
#                 "_id": section,
#                 "debit": 0,
#                 "credit": 0,
#                 "allEntries": []
#             }
#             if expense_collection.find_one({"_id": section}):
#                 return HttpResponse(json.dumps({"msg": "Section already Exist"}), content_type='application/json')
#             expense_collection.insert_one(doc)
#             return HttpResponse(json.dumps({"msg": "Section added Successfully"}), content_type='application/json')
#         except json.JSONDecodeError:
#             return HttpResponseBadRequest(json.dumps({"msg": "Invalid JSON data"}), content_type='application/json')
#         except:
#             return HttpResponseServerError(json.dumps({"msg": "Server Error"}), content_type='application/json')
#     else:
#         return HttpResponseBadRequest(json.dumps({"msg": "Server Error "}), content_type='application/json')


# @csrf_exempt
# def delSection(request, section):
#     try:
#         if request.method == 'DELETE':
#             expense_collection.delete_one({"_id": section})
#             return HttpResponse(json.dumps({"msg": "Successfully deleted"}), content_type='application/json')
#         else:
#             return HttpResponseBadRequest(json.dumps({"msg": "Request Not Allowed"}), content_type='application/json')
#     except:
#         return HttpResponseBadRequest(json.dumps({"msg": "Invalid Expense Id"}), content_type='application/json')


# def templateOfPost(bdy):
#     if request.method == 'POST':
#         try:
#             bdy
#             return HttpResponse(json.dumps({"msg": "Form Submitted Successfully"}), content_type='application/json')
#         except json.JSONDecodeError:
#             return HttpResponseBadRequest(json.dumps({"msg": "Invalid JSON data"}), content_type='application/json')
#         except:
#             return HttpResponseServerError(json.dumps({"msg": "Server Error"}), content_type='application/json')
#     else:
#         return HttpResponseServerError(json.dumps({"msg": "Server Error "}), content_type='application/json')


# def addEntryFun(dd, val, comment, _id, typ):
#     mm = dd[:7]
#     with client.start_session() as session:
#         try:
#             # start a transaction
#             with session.start_transaction():
#                 # check if the document with _id _id exists
#                 doc = expense_collection.find_one({"_id": _id})
#                 if doc is None:
#                     return "No Section Exist"
#                 # check if the month mm exists
#                 month_obj = next(
#                     (obj for obj in doc["allEntries"] if obj["month"] == mm), None)
#                 if month_obj is None:
#                     # create a new object for the month mm
#                     month_obj = {"month": mm, "monthlydebit": 0,
#                                  "monthlycredit": 0, "entries": []}
#                     doc["allEntries"].append(month_obj)

#                 # check if the date dd exists
#                 date_obj = next(
#                     (obj for obj in month_obj["entries"] if obj["date"] == dd), None)
#                 if date_obj is None:
#                     # create a new object for the date dd
#                     date_obj = {"date": dd, "dailydebit": 0,
#                                 "dailycredit": 0, "entries": []}
#                     month_obj["entries"].append(date_obj)

#                 # insert the new entry {comment: comment, value: val}
#                 date_obj["entries"].append({"comment": comment, "value": val})

#                 # increment the debit, monthlydebit, and dailydebit values
#                 doc[typ] += val
#                 month_obj["monthly"+typ] += val
#                 date_obj["daily"+typ] += val

#                 # update the document in the expense_collection
#                 expense_collection.update_one({"_id": _id}, {"$set": doc})

#                 return "entry Added Successfull"

#         except Exception as e:
#             # if an exception occurred, abort the transaction and log the error
#             session.abort_transaction()
#             # print(f"An error occurred: {e}")


# def removeEntryFun(val, _id, index):
#     query = {
#         '_id': _id
#     }
#     update = {
#         '$unset': {'allEntries.0.entries.0.entries.3': 1},
#         '$inc': {
#             'debit': -val,
#             'allEntries.0.monthlydebit': -val,
#             'allEntries.0.entries.0.dailydebit': -val
#         }
#     }

#     rm_null = {
#         '$pull': {
#             'allEntries.0.entries.0.entries': None
#         },
#     }
#     expense_collection.update_one(query, update)
#     expense_collection.update_one(query, rm_null)
