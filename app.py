from flask import Flask, render_template, request

app = Flask(__name__)
app.static_folder = 'static'
count = -2
Name = ""


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get")
def get_bot_response():
    global count, Name
    if count == -2:
        Name = request.args.get('msg')
        count += 1
        return str("Hello {} would you like to place an order?".format(Name))
    elif count == -1:
        PlaceOrder = request.args.get('msg')
        count += 1
        if PlaceOrder.lower() == "yes":
            return str("{} Plz enter the pickup address".format(Name))
        else:
            return str("Sorry is there anything else i can assist you with")
    elif count == 0:
        Pickup_Address = request.args.get('msg')
        count += 1
        print("Pickup Address: ", Pickup_Address)
        return str("{} Plz Enter Your delivery address".format(Name))
    elif count == 1:
        Delivery_Address = request.args.get('msg')
        count += 1
        print("Delivery Address: ", Delivery_Address)
        return str("Enter the approx weight of the package")
    elif count == 2:
        Weight = request.args.get('msg')
        count += 1
        print("Weight : ", Weight)
        return str("Enter the numbers of the packages to ship")
    elif count == 3:
        Number_of_Packages = request.args.get('msg')
        count += 1
        print("Number of Packages: ", Number_of_Packages)
        return str("Enter the average Height and width of the package")
    elif count == 4:
        Height_width = request.args.get('msg')
        count += 1
        return render_template('dateandtime.html')
    elif count == 5:
        Pickup_date = request.args.get("msg")
        count += 1
        print(str(Pickup_date))
        return str("{} is your pickup date and by when do you want the delivery to happen?".format(Pickup_date))
    elif count == 6:
        # getting input with name = fname in HTML form
        Delivery_date = request.args.get('date')
        count += 1
        print(Delivery_date)
        return str("Plz check the details in the next window and confirm your order.")
    else:
        return str("")


if __name__ == "__main__":
    app.run()
