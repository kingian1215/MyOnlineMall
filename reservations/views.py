from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .models import Reservation, Timeslot
from .forms import ReservationForm
import logging

from django.contrib.auth.decorators import login_required
# Create your views here.

logger = logging.getLogger(__name__) # 取得loggers

# @login_required
def make_reservation(request):
    if request.method == 'POST': 
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.save()

            # 取得用戶預約email
            user_email = request.user.email
            reservation_date = reservation.time_slot.date
            reservation_time = reservation.time_slot.start_time
            # reservation_people_num = reservation.people_num
            
            # 寄送email通知
            email_subject = '預約成功通知'
            email_message = f'親愛的{request.user.username}，\n\n您的預約已成功，\n日期：{reservation_date}\n\n感謝您的預約'
            try:
                send_mail(email_subject, 
                          email_message, 
                          settings.DEFAULT_FROM_EMAIL, 
                          [user_email],
                          fail_silently=False,
                          )
                logger.info(f'Email sent successfully to {user_email}')
                email_sent = 1 # 使用1表示True
            except Exception as e:
                logger.error(f'Error sending email: {e}') # 記錄錯誤訊息
                email_sent = 0 # 使用0表示False
            
            return redirect('reservation_success', email_sent=email_sent)
        
    else:
        form = ReservationForm()

    time_slots = Timeslot.objects.all()
    return render(request,'reservations/make_reservation.html', {'form': form, 'time_slots': time_slots})

def reservation_success(request, email_sent):
    email_sent = bool(int(email_sent)) # 將email_sent轉換為布林值
    return render(request,'reservations/reservation_success.html', {'email_sent': email_sent})