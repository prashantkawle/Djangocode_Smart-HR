from django.shortcuts import render
import pickle

# Create your views here.
def home(request):
    return render(request, 'index.html')

def getPredictions(age, ssc, hsc, grad, postg, exp):
    model = pickle.load(open('ml_model.sav', 'rb'))
    prediction = model.predict(([[age, ssc, hsc, grad, postg, exp]]))
    return prediction[0] 
  
def result(request):
    age = int(request.GET['age'])
    ssc = int(request.GET['ssc'])
    hsc= int(request.GET['hsc'])
    grad = int(request.GET['grad'])
    postg = int(request.GET['postg'])
    exp = int(request.GET['exp'])
    
    result = getPredictions(age, ssc, hsc, grad, postg, exp)
    return render(request, 'result.html', {'result': result})