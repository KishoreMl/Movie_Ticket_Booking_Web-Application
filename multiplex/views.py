from twilio.rest import Client
from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Movie, Ticket, TicketTemporary
from .models import Theatre
from .models import Crew
from .models import Cast
from .models import Kirthika
from .models import User
import datetime
import random

def index(request):
    return render(request,"index.html")

def checkPhone(phno):
    if(phno.isnumeric()):
       if(len(phno)==10):
           return True
       else:
            return False   
    else:
        return False


def checkOTP(otp):
    if(otp.isnumeric()):
       if(len(otp)==6):
           return True
       else:
            return False   
    else:
        return False        
           
def OTP(request):
    if request.method=='POST':
        phone = request.POST['phno']
        if(checkPhone(phone)):
            code = random.randint(111111,999999)
            code2 = random.randint(1111,9999)
            userid = "MPUI"+str(code2)

            account_sid="ACa86d57d60692ae495e24922252a1aa50"
            auth_token="d06c16814877911454aeacfad5629ca0"
            myNum="+14195065825"
            client = Client(account_sid,auth_token)
            client.messages.create(from_=myNum,body="This is OTP "+str(code)+" for logging in  Multiplex.com",to="+91"+str(phone))

            user = User.objects.create(userId=userid,phno=phone,name="null",cardno="null",ticketId="null")
            user.save()
            return render(request,"checkOtp.html",{'otp':str(code),"userid":userid})
        else:
            messages.info(request,'Invalid Phone number')
            return render(request,"index.html")    
    else:
        return render(request,"index.html")    

def home(request):
    if request.method=='POST':
        code1 = request.POST['otpReal']
        code2 = request.POST['otpUser']
        userid =request.POST['userid']
        if(checkOTP(code2) and (code1==code2)):
            movies1 = Movie.objects.all().filter(released=1)
            movies2 = Movie.objects.all().filter(released=0)
            return render(request,"home.html",{'movies':movies1,"moviesR":movies2,"userid":userid})
        else:
            messages.info(request,'Incorrect OTP')
            return render(request,"checkOtp.html",{"userid":userid})    
    else:
        movies1 = Movie.objects.all().filter(released=1)
        movies2 = Movie.objects.all().filter(released=0)
        return render(request,"home.html",{'movies':movies1,"moviesR":movies2})



def movie(request):
    if request.method == 'POST':
        movieName = request.POST['moviename']
        userid = request.POST['userid']
        if Movie.objects.filter(movieName=movieName):
            movie=Movie.objects.get(movieName=movieName)
            cast = Cast.objects.all().filter(movieName=movieName) 
            crew = Crew.objects.all().filter(movieName=movieName)
        return render(request,"movie.html",{"movie":movie,"cast":cast,"crew":crew,"userid":userid})
    else:
        return render(request,"home.html")

def allmovies(request):
    if request.method == 'GET':
        userid = request.GET['userid']
        movies  = Movie.objects.all()
        return render(request,"movies.html",{"movies":movies,"userid":userid})

def checkDate(day,month):

    mon ={
        1 : 31,
        2 : 28,
        3 : 31,
        4 : 30,
        5 : 31,
        6 : 30,
        7 : 31,
        8 : 31,
        9 : 30,
        10 : 31,
        11 : 30,
        12 : 31
    }
    if(day==mon[month]):
        if(month==12):
            return 1,1
        else:
            return 1,month+1    
    else:    
        return day+1,month

def assignMonth(month):
    mon ={
        1 : "JAN",
        2 : "FEB",
        3 : "MAR",
        4 : "APR",
        5 : "MAY",
        6 : "JUN",
        7 : "JUL",
        8 : "AUG",
        9 : "SEP",
        10 : "OCT",
        11 : "NOV",
        12 : "DEC"
    }

    return mon[month]

def theatres(request):
    if request.method == 'POST':
        movieName = request.POST['moviename']
        userid = request.POST['userid']
        if Movie.objects.filter(movieName=movieName):
            movie=Movie.objects.get(movieName=movieName)
            theatre=Theatre.objects.all()
            cast = Cast.objects.all().filter(movieName=movieName) 
            date=datetime.datetime.now()
            
            day1=date.day
            month1=date.month
            day2,month2=checkDate(day1,month1)
            day3,month3=checkDate(day2,month2)
            day4,month4=checkDate(day3,month3)
            day5,month5=checkDate(day4,month4)

            month1 = assignMonth(month1)
            month2 = assignMonth(month2)
            month3 = assignMonth(month3)
            month4 = assignMonth(month4)
            month5 = assignMonth(month5)

        return render(request,"theatres.html",{"movie":movie,"theatre":theatre,"cast":cast,
        "day1":day1,"day2":day2,"day3":day3,"day4":day4,"day5":day5,"month1":month1,
        "month2":month2,"month3":month3,"month4":month4,"month5":month5,"userid":userid})    

    else:
        return render(request,"movie.html")        

def theatrehall(request):
    if request.method == 'POST':
        result = request.POST['theatre'].split(',')
        theatreName = result[0]
        time = result[1]
        movie = request.POST['moviename']
        date = request.POST['date']
        userid = request.POST['userid']
        theatre = Theatre.objects.get(theatreName=theatreName)
        Seats = Kirthika.objects.all().order_by('rowId')
        return render(request,"theatrehall.html",{"date":date,"theatre":theatre,"movie":movie,"time":time,"seats":Seats,"userid":userid})
    else:
        return render(request,"theatres.html")    

def search(request):
    if request.method =='POST':
        movieName = request.POST['movie']
        if Movie.objects.filter(movieName=movieName):
            movies=Movie.objects.get(movieName=movieName)
            cast = Cast.objects.all().filter(movieName=movieName) 
            crew = Crew.objects.all().filter(movieName=movieName)
            return render(request,"search.html",{"movie":movies,"cast":cast,"crew":crew}) 
        else:
            return render(request,"search.html")     
    else:
        return render(request,"home.html")    


def ticketType(tickets):
    platinumRow = "ABC"
    goldRow = "DEFGHIKL"
    silverRow  = "MNO"
    gold = []
    platinum = []
    silver = []

    for t in tickets:
            if(t != ""):
                row = t[0]
                if(row in platinumRow):
                    platinum.append(t)
                elif(row in goldRow):
                    gold.append(t)
                else:
                    silver.append(t)

    return gold,platinum,silver                

def bookingSummary(request):
    if request.method == 'POST':
        theatre = request.POST['theatre']
        time = request.POST['time']
        mov = request.POST['movie']
        seats = request.POST['seats']
        date = request.POST['date']
        userid = request.POST['userid']
        tickets =seats.split(',')
        movie = Movie.objects.get(movieName=mov)
        location = request.POST['location']
        convenienceFee = (len(tickets)-1)*30
        totalTickets = len(tickets)-1
        total=0
        subtotal=0
        gold = []
        platinum = []
        silver = []
        
        gold,platinum,silver=ticketType(tickets)

        subtotal = len(gold)*100 + len(platinum)*150 + len(silver)*70
        total = subtotal + convenienceFee

        tidno = random.randint(0000,9999)
        tid = "MP"+str(tidno)

        ticke = TicketTemporary.objects.create(ticketId=tid,movieName=mov,theatreName=theatre,location=location,
        time=time,date=date,seats=seats,totalTickets=totalTickets,confee=convenienceFee,subtotal=subtotal,total=total)
        ticke.save()

        ticket = TicketTemporary.objects.get(ticketId=tid)
        

        return render(request,"bookingSummary.html",{"ticket":ticket,"gold":gold,"silver":silver,"platinum":platinum,"movie":movie,"userid":userid})
    else:
        return render(request,"bookingSummary.html")  
def checkName(name):
    if(name.isalpha):
        return True
    else:
        return False    

def checkCardNumber(no):
    if(no.isnumeric()):
       if(len(no)==12):
           return True
       else:
            return False   
    else:
        return False

def checkCCV(ccv):
    if(ccv.isnumeric()):
       if(len(ccv)==3):
           return True
       else:
            return False   
    else:
        return False

def checkMonth(mon):
    if(mon.isnumeric()):
       if(len(mon)==2):
           m = int(mon)
           if(m>=1 or m<=12):
               return True
           else:    
                return False
       else:
            return False   
    else:
        return False

def checkYear(year):
    if(year.isnumeric()):
       if(len(year)==2):
           return True
       else:
            return False   
    else:
        return False

def payment(request):
    if request.method == 'POST':
        tid = request.POST['ticketId']
        mov = request.POST['movie']
        userid = request.POST['userid']
        movie = Movie.objects.get(movieName=mov) 
        ticket = TicketTemporary.objects.get(ticketId=tid)
        tickets = ticket.seats.split(',')
        gold = []
        platinum = []
        silver = []
        gold,platinum,silver=ticketType(tickets)   
        

        return render(request,"payment.html",{"ticket":ticket,"movie":movie,"gold":gold,"platinum":platinum,"silver":silver,"userid":userid})        
    else:
        return render(request,"payment.html")

def paymentOTP(request):
    if request.method =='POST':
        otp= random.randint(111111,999999)
        movie = request.POST['movie']
        userid = request.POST['userid']
        ccv = request.POST['ccv']
        name = request.POST['name']
        month = request.POST['month']
        year = request.POST['year']
        cardNo = request.POST['cardNo']
        tid = request.POST['ticketId']
        mov = Movie.objects.get(movieName=movie) 
        ticket = TicketTemporary.objects.get(ticketId=tid)
        user = User.objects.get(userId=userid)
        ph = user.phno 
        tickets = ticket.seats.split(',')
        gold = []
        platinum = []
        silver = []
        gold,platinum,silver=ticketType(tickets)
        
       
       
        if(not(checkCardNumber(cardNo)) or not(checkName(name)) or not(checkMonth(month)) or not(checkYear(year)) or not(checkCCV(ccv)) ):
            messages.info(request,"Invalid card details")
            return render(request,"payment.html",{"ticket":ticket,"movie":mov,"gold":gold,"platinum":platinum,"silver":silver})  
        else:
             account_sid="ACa86d57d60692ae495e24922252a1aa50"
            auth_token="d06c16814877911454aeacfad5629ca0"
            myNum="+14195065825"
            client = Client(account_sid,auth_token)
            client.messages.create(from_=myNum,body="This is your OTP "+str(code),to="+91"+str(ph))
            return render(request,"paymentOtp.html",{"OTP":otp,"movie":mov,"ccv":ccv,"name":name,
            "month":month,"year":year,"cardno":cardNo,"userid":userid,"ticket":ticket})
    else:
        return render(request,"payment.html")

def booked(request):
    if request.method == 'POST':
        otp1 = request.POST['otpUser']
        otp2 = request.POST['otpReal']
         
        if(checkOTP(otp1)):
            userid = request.POST['userid']
            name = request.POST['name']
            cardNo = request.POST['cardNo']
            mov = request.POST['movie']
            tid = request.POST['ticketId']
            movie = Movie.objects.get(movieName=mov)
            ticket = TicketTemporary.objects.get(ticketId=tid)
            tickets =ticket.seats.split(',')
            gold = []
            platinum = []
            silver = []

            gold,platinum,silver=ticketType(tickets)     
            years = datetime.datetime.now()
            year = years.year

            if(otp1==otp2):

                updateSeats(tickets)
                finalseats=""
                if(silver):
                    finalseats=finalseats+" SILVER-"
                    for s in silver:
                        finalseats=finalseats+str(s)+","
                if(gold):
                    finalseats=finalseats+" GOLD-"
                    for g in gold:
                        finalseats=finalseats+str(g)+","
                if(platinum):
                    finalseats=" PLATINUM-"
                    for p in platinum:
                        finalseats=finalseats+str(p)+","        

                user = User.objects.get(userId=userid)
                user.name=name
                user.cardno=cardNo
                user.ticketId =ticket.ticketId
                user.save()

                finaldate = ticket.date+","+str(year)

                T = Ticket.objects.create(ticketId=ticket.ticketId,movieName=ticket.movieName,theatreName=ticket.theatreName
                ,location=ticket.location,time=ticket.time,date=finaldate,seats=ticket.seats,totalTickets=ticket.totalTickets,
                confee=ticket.confee,subtotal=ticket.subtotal,total=ticket.total)
                T.save()

                Tickets = Ticket.objects.get(ticketId=ticket.ticketId)
                TicketTemporary.objects.filter(ticketId=ticket.ticketId).delete()

                account_sid="ACa86d57d60692ae495e24922252a1aa50"
                auth_token="d06c16814877911454aeacfad5629ca0"
                myNum="+14195065825"
                client = Client(account_sid,auth_token)
                client.messages.create(from_=myNum,body="Hi "+str({{user.name}})+", \n Booking ID:"+str({{user.ticketId}})+", \n Seats "+str({{finalseats}})+"\n "+str({{Tickets.totalTickets}})+"seat(s) for"+str({{movie.moviName}})+str({{movie.certification}})+"on"+str({{Tickets.date}})+str({{Tickets.time}})+"\n at"+str({{Tickets.theatreName}})+","+str({{Tickets.location}})+"\n  Cancellation not available",to="+91"+str(user.phno))
                        
                return render(request,"ticket.html",{"movie":movie,"ticket":Tickets,"gold":gold,"platinum":platinum,"silver":silver,"year":year,"userid":userid})
            else:
                messages.info(request,'Incorrect OTP')
                return render(request,"paymentOTP.html",{"userid":userid})
        else:
            messages.info(request,'Incorrect OTP')
            return render(request,"paymentOTP.html",{"OTP":otp2})
    else:

        return render(request,"ticket.html") 

def updateSeats(tickets):
    for t in tickets:
        if(t != ""):
            row = Kirthika.objects.get(rowId=t[0])
            s = t[1:]
            seat =int(s)
            if(seat==1):
                row.Seat1="booked"
                row.save()
            elif(seat==2):
                row.Seat2="booked"
                row.save() 
            elif(seat==3):
                row.Seat3="booked"
                row.save() 
            elif(seat==4):
                row.Seat4="booked"
                row.save() 
            elif(seat==5):
                row.Seat5="booked"
                row.save() 
            elif(seat==6):
                row.Seat6="booked"
                row.save() 
            elif(seat==7):
                row.Seat7="booked"
                row.save() 
            elif(seat==8):
                row.Seat8="booked" 
                row.save()
            elif(seat==9):
                row.Seat9="booked"
                row.save() 
            elif(seat==10):
                row.Seat10="booked" 
                row.save()
            elif(seat==11):
                row.Seat11="booked"
                row.save() 
            elif(seat==12):
                row.Seat12="booked"
                row.save()
            elif(seat==13):
                row.Seat13="booked"
                row.save() 
            elif(seat==14):
                row.Seat14="booked" 
                row.save()
            elif(seat==15):
                row.Seat15="booked" 
                row.save()
            elif(seat==16):
                row.Seat16="booked" 
                row.save()
            elif(seat==17):
                row.Seat17="booked" 
                row.save()
            elif(seat==18):
                row.Seat18="booked"
                row.save() 
            elif(seat==19):
                row.Seat19="booked"
                row.save()
            elif(seat==20):
                row.Seat20="booked"
                row.save()          





            
            



