from django.shortcuts import render, redirect


def input_page(request):
    return render(request, 'members_app/input.html')

def display_page(request):
    user_input = request.POST.get('user_input')
    session_data = request.session['session_data'] = 'Hello, World!'
    return render(request, 'members_app/display.html', {'user_input': user_input})

def session_page(request):
    session_data = "Nothing"
    if request.method == 'POST':
        session_data = request.POST.get('session_input')
    elif 'session_data' in request.session:
        session_data = request.session['session_data']
    return render(request, 'members_app/session.html', {'session_data': session_data})

def clear_session(request):
    request.session.clear()
    return redirect('session_page')


