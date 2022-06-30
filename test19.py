#  Використовуючи Python випиши чому дорівнює зарплата

sampleJson = {
   "company":{
      "employee":{
         "name":"emma",
         "payble":{
            "salary":7000,
            "bonus":800
         }
      }
   }
}
print(sampleJson["company"]["employee"]["payble"]["salary"])
