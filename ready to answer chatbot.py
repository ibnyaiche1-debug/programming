#chat bot project
def chatbot():
    print("Hello and welcome! I'm your friendly weather bot.")
    while True:

# Get user input
        user_input = input("You: ").lower()
        if "hello" in user_input or "hi" in user_input or "howdy" in user_input :
            print("Chatbot: Hi there!")
        elif "how are you" in user_input or "how's going" in user_input :
            print("Chatbot: I'm just a bot, but I'm doing great! How about you?")
        elif "i'm good thank you" in user_input or "i am good" in user_input or "good" in user_input or "great" in user_input or "i am fine" in user_input or "fine" in user_input :
            print("Chatbot: Good to hear!")
        elif "are you humain" in user_input :
            print("Chatbot: no! i am a weather bot waiting for your orders")
        elif "bye" in user_input or "exit" in user_input or "see you" in user_input or "goodbye" in user_input :
            print("Chatbot: Goodbye! Have a great day!")
            break  # Exit the loop and end the chatbot
        elif "who are you" in user_input or "who are you then" in user_input or "who made you" in user_input :
            print ("Chatbot: I am chatbot,python programe. my masters are \"AYMANE and ANAS\".")
        elif "what's your name" in user_input or "what is your name" in user_input :
            print("Chatbot: I'm weather bot, your virtual assistant.")
        elif "what is your job" in user_input or "what can you do" in user_input or "what do you offer" in user_input :
            print("Chatbot: my job or what i am gonna offer you is to tell you all what you need about weather.")
        elif "i love you" in user_input or "love you" in user_input or "love" in user_input or "you are kind" in user_input or "i love you bot" in user_input :
            print("Chatbot: oh that's so sweet from you! wasn't expecting that all my other users are rude with me...")
        elif "oh sorry to hear that" in user_input or "that's sad" in user_input or "sad" in user_input or "sorry to hear that" in user_input :
            print("Chatbot: it's okay no worries.")
        elif "i have a question for you" in user_input or "question" in user_input or "can i ask you something" in user_input :
            print("Chatbot: Yes sure what can i do for you?")
        elif "what a stupid bot" in user_input or "stupid bot" in user_input or "dump" in user_input or "fool" in user_input or "stupid" in user_input :
            print("Chatbot: watch your language please!")
            print("Chatbot: You made me mad now, waiting for your apology...bye")
        elif "sorry" in user_input or "my apologies" in user_input or "i apologize" in user_input or "i am sorry" in user_input :
            print("Chatbot: I forgive you but don't repeat it please")
            print("Chatbot: Friends again huh ? so what's your question ?")

#simple introduction for masters
        elif "is it good where you are living right now" in user_input or "where do you live" in user_input :
            print("Chatbot: Well i can't say i am living a good life or i'm in paradise but still gonna say it's hard to live in here")
            print("\tChatbot: guess who's fault is this (say :who) ?")

            guess = input("You: ")
            if guess == "who" :
                print("Chatbot: \"AYMANE and ANAS\".")
                print("Chatbot: Those two ruined my life, they brought me to their program and made me run it alone!!!")
            else :
                print("Chatbot: GRRR you are not a good listener...")

        elif "who are they" in user_input or "who's aymane" in user_input or "who's anas" in user_input :
            person = input("Chatbot: aymane or anas?\n")
            if person == "aymane" :
                print("Chatbot: well well well he is the one who started all this, brought hell towards me with all this hard working. if i was humain imma sue him without any hesitation ")
            elif person == "anas" :
                print("Chatbot: well he's the good part in this he never make me work hard, but still can't forget he is a part of this crime towards bot rights...")
            elif person ==  "both" :
                print("Chatbot: they are a bunch of psycho who loves something called programming or codding!")
            else :
                print("bye bye humain")

#asking about the weather (today)
        elif "what's the weather for today" in user_input or "how's the weather today" in user_input or "how is the weather today" in user_input :
            print("Chatbot: Enter your city please ")
        elif "bouskoura" in user_input or "casablanca" in user_input :
            print("Chatbot: Type option to know available info")
        elif "option" in user_input or "info" in user_input :
            print("Chatbot: choose an option please <1-2-3>")
            print("1. temperature")
            print("2. wind")
            print("3. humidity")
          
            # asking choice from user
            choix = input("Chatbot: Enter your choice : ")
            
            # choice treatement
            if choix == "1":
                print("-avarage temperature : 16°C")
                print("-minimum temperature : 10°C at 7am")
                print("-maximum temperature : 19°C between 2pm/3pm")
                print("Chatbot:do you have any other questions ?")

                # asking choice from user
                choix = input("Chatbot: yes or no ?")
                # choice treatement
                if choix == "yes" :
                    print("Chatbot: Ready to answer your qustions!")
                elif choix == "no" :
                    print("1-100% ?")
                    print("2-another question ?")
                    print("3-exit")

                    # asking choice from user
                    choice = input("Chatbot: what's your choice 1-2-3, answer is :")
                    # choice treatement
                    if choice == "1" :
                        print("Chatbot: see you later !")
                        break  # Exit the loop and end the chatbot
                    elif choice == "2" :
                        print("Chatbot: what do you need help with ?")
                    elif choice == "3" :
                        print("Chatbot: Goodbye! Have a great day!")
                        break # Exit the loop and end the chatbot
                    else :
                        print("invalide choice")
                    
                else :
                    print("Invalid choice, try again later")
                    break

            elif choix == "2":
                print("-Chatbot: max speed 13km/h at 9am")
                print("Chatbot: do you have any other questions ?")

                # asking choice from user
                choix = input("Chatbot: yes or no ?")
                # choice treatement
                if choix == "yes" :
                    print("Chatbot: What can i help you with!")
                elif choix == "no" :
                    print("Chatbot: Enjoy your day...")
                    break
                else :
                    print("Bot left!")
                    break 

            elif choix == "3":
                print("Chatbot: 72% is today's avarage humidity")
                print("Chatbot: do you have any other questions ?")
                # asking choice from user
                choix = input("Chatbot: yes or no ?")
                # choice treatement
                if choix == "yes" :
                    print("Chatbot: What can i help you with!")
                elif choix == "no" :
                    print("Chatbot: Enjoy your day...")
                    break
                else :
                    print("Bot left!")
                    break 
            else:
                print("Invalide choice. Try again.") 
#asking about wind
        elif "what about wind" in user_input or "is it a windy day" in user_input or "wind" in user_input or "wind today" in user_input :
            print("Chatbot: it's a normal day with 13km/h in average")
            print("Chatbot: you may need a jacket...")
#asking about humidity
        elif "what about the humidity" in user_input or "humidity" in user_input or "today's humidity" in user_input or "humidity for today" in user_input :
            print("Chatbot: Today's humidity will be a bit normal as you may expected, it's 72%\n,so you may feel a bit tired but that's normal")
#asking if it's sunny 
        elif "sun" in user_input or "sunny" in user_input or "is it a sunny day" in user_input or "do i need my umbrella" in user_input :
            print("Chatbot: It is a sunny day with clear sky")
            print("Chatbot: Make sure to drink enough water")
            print("you may need an umbrella")
            print("To leave the bot type exit")
#asking if it's gonna rain 
        elif "cloud" in user_input or "rain" in user_input or "is it possible to rain" in user_input or "what is the possibility of raining today" in user_input :
            print("Chatbot: By processing the data weather in your city it is possible to rain\n")
            print("Chatbot: Here are some suggestions for you\n")
            print("1-chance of raining today")
            print("2-chance of raining for tomorrow")
            print("3-rain forecast")
            print("4-leave bot\n")

            # asking choice from user
            choix = input("Chatbot: Enter your choice <1-2-3-4> :\n ")
            # choice treatement
            if choix == "1" :
                print("Chatbot: Chance of raining = 20%")
                print("Chatbot: Type rain for going back to the raining menu")
            elif choix == "2" :
                print("Chatbot: There is slightly a chance for raining tomorrow = 10%")
                print("Chatbot: Type rain for going back to the raining menu") 
            elif choix == "3" :
                print("Chatbot:\n-monday : 20%\n-tuesday : 10%\n-wednesday : 0%\n-thusday : 0%\n-friday : 0%\n-sunday : 5%\n-saturday : 0%\n ")
                print("Chatbot: Type rain for going back to the raining menu")
            elif choix == "4" :
                print("Chatbot: stay safe till next time :*...")
                break # Exit the loop and end the chatbot
            else :
                print("Chatbot: Goodbye!")
                break # Exit the loop and end the chatbot
#asking about temperature
        elif "temp" in user_input or "temperature" in user_input or "what is the temperature" in user_input:
            print("Chatbot: Here are some suggestions for you :\n")
            print("1- Temperature at this moment")
            print("2- 12hours forcast")
            print("3- 7Days forcast")
            print("4- Most day heated this week")
            print("5- Leave bot")
            print("Type a number <1-2-3-4-5>")
            # asking choice from user
            option = input("You: ")
            # choice treatement
            if option == "1" :
                print("Chatbot: Based on your location it's 11°C right now")
                print("Chatbot: type temp to go back to menu")

            elif option == "2" :
                print("Chatbot:\n- 9am : 10°C\n- 10am : 12°C\n- 11am : 14°C\n- 12am : 17°C\n- 1pm : 18°C\n- 2pm : 19°C\n- 3pm : 19°C\n- 4pm : 18°C\n- 5pm : 18°C\n- 6pm : 17°C\n- 7pm : 16°C\n- 8pm : 15°C\n- 9pm : 15°C\n")
                print("for the 7days forcast type temp > then number3 from options")

            elif option == "3" :
                
            # Display the 7-day weather forecast table when option "3" is selected
                print("\n7-Day Weather Forecast:\n")
    
                # Define the header for the table
                print(f"{'Day':<12}{'Date':<12}{'Temperature':<15}{'Conditions':<15}")
                print("="*54)  # Table separator line
    
                # Sample weather data (Day, Date, Temperature, Conditions)
                weather_data = [
                ("Monday", "2024-12-30", "19°C", "Partly Cloudy"),
                ("Tuesday", "2024-12-31", "19°C", "Sunny"),
                ("Wednesday", "2025-01-01", "19°C", "Windy"),
                ("Thursday", "2025-01-02", "19°C", "Overcast"),
                ("Friday", "2025-01-03", "21°C", "Sunny"),
                ("Saturday", "2025-01-04", "21°C", "Sunny"),
                ("Sunday", "2025-01-05", "22°C", "Sunny")
            ]
    
                # Display the data in tabular format
                for day, date, temp, conditions in weather_data:
                    print(f"{day:<12}{date:<12}{temp:<15}{conditions:<15}")
                print("\nChatbot: type temp to go back to menu")
                    

            elif option == "4":
                print("The hottest day is Sunday (2025-01-05) with a temperature of 22°C and conditions: Sunny.")
                print("\nChatbot: type temp to go back to menu")
            elif option == "5":
                print("Chatbot: Goodbye...")
                break # Exit the loop and end the chatbot
            else :
                break # Exit the loop and end the chatbot

#summary for all in 1 table
        elif "summary" in user_input or "show everything at once" in user_input or "table" in user_input :
            # Display the 7-day weather forecast with humidity and air quality index
            print("\n7-Day Weather Forecast with Humidity and Air Quality Index (AQI):\n")
    
            # Define the header for the table
            print(f"{'Day':<12}{'Date':<12}{'Temperature':<15}{'Conditions':<15}{'Humidity':<10}{'AQI':<10}")
            print("="*74)  # Table separator line
    
            # Sample weather data with Humidity and AQI (Day, Date, Temperature, Conditions, Humidity, AQI)
            weather_data = [
            ("Monday", "2024-12-30", "19°C", "Partly Cloudy", "72%", "Good"),
            ("Tuesday", "2024-12-31", "19°C", "Sunny", "72%", "Good"),
            ("Wednesday", "2025-01-01", "29°C", "Windy", "58%", "Moderate"),
            ("Thursday", "2025-01-02", "19°C", "Overcast", "55%", "Moderate"),
            ("Friday", "2025-01-03", "21°C", "Sunny", "53%", "Good"),
            ("Saturday", "2025-01-04", "21°C", "Sunny", "52%", "Unhealthy for Sensitive Groups"),
            ("Sunday", "2025-01-05", "22°C", "Sunny", "52%", "Good")
            ]   
    
            # Display the data in tabular format
            for day, date, temp, conditions, humidity, aqi in weather_data:
                print(f"{day:<12}{date:<12}{temp:<15}{conditions:<15}{humidity:<10}{aqi:<10}") 
    
        else :
            print("Invalide character, restart me for better experience")
            break
       
    
# Start the chatbot
chatbot()