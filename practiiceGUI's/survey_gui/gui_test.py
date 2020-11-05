from guizero import App, Text, TextBox, PushButton, Slider, Picture, Combo, CheckBox, ButtonGroup, PushButton

def say_my_name():
    welcome_message.value = my_name.value

def change_text_size(slider_value):
    welcome_message.size = slider_value
    
def do_booking():
    info("Booking", "Thank you for booking")
    print( film_choice.value )
    print( vip_seat.value )
    print( row_choice.value )

app = App(title="Hello world")

welcome_message = Text(app, text="Welcome to my app", size=40, font="Times new roman", color="lightblue")
my_name = TextBox(app, width=30)
update_text = PushButton(app, command=say_my_name, text="Display my name")
text_size = Slider(app, command=change_text_size, start=10, end=80)

film_description = Text(app, text="Which film?", grid=[0,0], align="left")

film_choice = Combo(app, options=["Star Wars", "Frozen", "Lion King"], grid=[1,0], align="left")

film_description = Text(app, text="Seat type?", grid=[0,1], align="left")

vip_seat = CheckBox(app, text="VIP seat?", grid=[1,1], align="left")

row_choice = ButtonGroup(app, options=[ ["Front", "F"], ["Middle", "M"],["Back", "B"] ],
selected="M", horizontal=True, grid=[1,2], align="left")

book_seats = PushButton(app, command=do_booking, text="Book seat", grid=[1,3], align="left")

app.display()