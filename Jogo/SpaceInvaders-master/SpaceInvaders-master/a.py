from firebase import firebase

firebase = firebase.FirebaseApplication("https://mini-arcade-69906.firebaseio.com", None)

data = {
    'pontos':2000
}

firebase.post("Pontos",data)

record = {
    'new_record?':True
}

firebase.post("record",record)
