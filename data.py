from faker import Faker
import random
import datetime
import csv
from dateutil.relativedelta import relativedelta

fake = Faker()


class Restaurant:
    def __init__(self):
        self.restaurants = []

    def generate_restaurants(self, num_restaurants):
        restaurant_types = ["Cafe", "Restaurant", "Fast Food", "Fine Dining"]

        for _ in range(num_restaurants):
            restaurant_id = len(self.restaurants) + 1
            restaurant_name = fake.company()
            restaurant_type = random.choice(restaurant_types)
            restaurant_location = fake.city()
            restaurant_address = fake.street_address()
            restaurant_city_id = random.randint(1, 100)
            restaurant_state_prov = fake.state()
            restaurant_phone = fake.phone_number()
            restaurant_email = fake.company_email()
            restaurant_country = fake.country()
            restaurant_postal_code = fake.postcode()
            restaurant_owner = fake.name()
            restaurant_website = fake.url()
            restaurant_rating = round(random.uniform(1, 5), 1)
            chain_code = fake.uuid4()

            restaurant_data = {
                'Restaurant_UID': restaurant_id,
                'Restaurant_Name': restaurant_name,
                'Restaurant_Type': restaurant_type,
                'Restaurant_Location': restaurant_location,
                'Restaurant_Address': restaurant_address,
                'Restaurant_City_ID': restaurant_city_id,
                'Restaurant_StateProv': restaurant_state_prov,
                'Restaurant_PhoneNo': restaurant_phone,
                'Restaurant_Email': restaurant_email,
                'Restaurant_Country': restaurant_country,
                'Restaurant_PostalCode': restaurant_postal_code,
                'Restaurant_Owner': restaurant_owner,
                'Restaurant_Website': restaurant_website,
                'Restaurant_Rating': restaurant_rating,
                'Chain_Code': chain_code
            }
            self.restaurants.append(restaurant_data)

    def get_data(self):
        return {
            'restaurants': self.restaurants,
        }


class Customer:
    def __init__(self):
        self.customers = set()
        self.starting_customer_id = 201

    def generate_customers(self, num_customers, restaurants):
        usa_codes = ['+1', '+01']  # Country codes for USA
        canada_codes = ['+1', '+01']  # Country codes for Canada
        mexico_codes = ['+52']
        for _ in range(num_customers):
            customer_id = self.starting_customer_id
            self.starting_customer_id += 1
            while customer_id in self.customers:
                customer_id = len(self.customers) + 1

            restaurant = random.choice(restaurants)
            restaurant_name = restaurant['Restaurant_Name']
            survey_questions = [
                {
                    'question': f"How was the food at {restaurant_name}?",
                    'recommendations': {
                        'Excellent': "Try their specialty dish!",
                        'Good': "Their desserts are fantastic!",
                        'Average': "Consider trying their daily specials.",
                        'Poor': "We apologize for the inconvenience. Please provide feedback to improve."
                    }
                },
                {
                    'question': f"How was the service at {restaurant_name}?",
                    'recommendations': {
                        'Excellent': "Ask for the attentive waiter, they're great!",
                        'Good': "Service is good; try their weekend specials.",
                        'Average': "Service can be improved during peak hours.",
                        'Poor': "We apologize for the service. Let us know how we can assist."
                    }
                },
            ]
            country = fake.random_element(
                elements=['USA', 'Canada', 'Mexico'])

            if country == 'USA':
                country_code = fake.random_element(elements=usa_codes)
                phone_number = fake.phone_number()  # Generates US phone number
            elif country == 'Canada':
                country_code = fake.random_element(elements=canada_codes)
                # Generates Canadian phone number
                phone_number = fake.phone_number()
            else:
                country_code = fake.random_element(elements=mexico_codes)
                phone_number = fake.phone_number()
            question = random.choice(survey_questions)
            restaurant_id = random.choice(restaurants)['Restaurant_UID']
            title = random.choice(['Mr.', 'Ms.', 'Mrs.', 'Dr.'])
            first_name = fake.first_name()
            middle_name = fake.first_name()
            last_name = fake.last_name()
            age = random.randint(5, 95)
            gender = random.choice(['Male', 'Female', 'Other'])
            contact_type = random.choice(['Primary', 'Secondary'])

            email = fake.email()
            email_type = random.choice(['Personal', 'Work'])
            dob = fake.date_of_birth(minimum_age=age)
            nationality = fake.country()
            location = fake.city()
            address_type = random.choice(['Home', 'Work'])
            address_line1 = fake.street_address()
            address_line2 = fake.secondary_address()
            address_line3 = fake.building_number()
            city_name = fake.city()
            state_prov = fake.state()
            postal_code = fake.postcode()
            latitude = fake.latitude()
            longitude = fake.longitude()
            occupation = fake.job()
            marital_status = random.choice(
                ['Single', 'Married', 'Divorced', 'Widowed'])
            preferred_language = random.choice(
                ['English', 'Spanish', 'French', 'Mandarin'])
            primary_credit_card = fake.credit_card_number(card_type='visa16')
            primary_cc_expiry_month = fake.credit_card_expire(
                start='now', end='+10y', date_format='%m')
            primary_cc_expiry_year = fake.credit_card_expire(
                start='now', end='+10y', date_format='%Y')
            secondary_credit_card = fake.credit_card_number(
                card_type='mastercard')
            secondary_cc_expiry_month = fake.credit_card_expire(
                start='now', end='+10y', date_format='%m')
            secondary_cc_expiry_year = fake.credit_card_expire(
                start='now', end='+10y', date_format='%Y')
            anniversary = fake.date_between_dates(
                datetime.date(1960, 1, 1), datetime.date.today())
            registration_date = fake.date_between_dates(
                datetime.date(2010, 1, 1), datetime.date.today())

            income_level = int(round(random.uniform(20000, 100000), 0))
            if random.random() < 0.7:
                food_allergies = fake.random_element(
                    elements=['nuts', 'dairy', 'seafood', 'gluten', 'soy', 'eggs'])
            else:
                food_allergies = None
            government_id_proof = random.choice(
                ['Passport', 'Driver License', 'ID Card'])
            government_id_number = fake.ssn()
            government_id_expiry_date = fake.date_between_dates(
                datetime.date.today(), datetime.date.today() + datetime.timedelta(days=365*10))
            special_event = fake.random_element(
                elements=('Birthday', 'Anniversary', 'Graduation'))
            special_event_date = fake.date_between_dates(
                datetime.date.today(), datetime.date.today() + datetime.timedelta(days=365))
            last_purchase_date = fake.date_between_dates(
                datetime.date.today() - datetime.timedelta(days=365), datetime.date.today())
            last_purchase_time = fake.time()
            loyalty_points_status = fake.random_element(
                elements=('regular', 'silver', 'gold', 'platinum', 'diamond'))
            customer_segment = 'Loyal' if loyalty_points_status != 'regular' else 'Non-Loyal'
            survey_date = fake.date_between_dates(
                datetime.date.today() - datetime.timedelta(days=365), datetime.date.today())
            survey_time = fake.time()
            survey_question = fake.sentence(nb_words=6)
            survey_answer = fake.sentence(nb_words=10)
            survey_recommendation = fake.sentence(nb_words=8)
            survey_rating = random.randint(1, 5)
            survey_result = random.choice(
                ['Excellent', 'Good', 'Average', 'Poor'])
            customer_lead_source = random.choice(
                ['Referral', 'Website', 'Promotional Ads'])
            customer_data = {
                'Customer_UID': customer_id,
                'Restaurant_UID': restaurant_id,
                'Customer_Title': title,
                'Customer_FirstName': first_name,
                'Customer_MiddleName': middle_name,
                'Customer_LastName': last_name,
                'Customer_Age': age,
                'Customer_Gender': gender,
                'Customer_Contact_Type': contact_type,
                'Customer_country_code': country_code,
                'Customer_PhoneNo': phone_number,
                'Customer_Email': email,
                'Customer_Email_type': email_type,
                'Customer_DOB': dob,
                'Customer_Nationality': nationality,
                'Customer_Location': location,
                'Customer_Address_Type': address_type,
                'Customer_Address_Line1': address_line1,
                'Customer_Address_Line2': address_line2,
                'Customer_Address_Line3': address_line3,
                'Customer_City_name': city_name,
                'Customer_State_Prov': state_prov,
                'Customer_Postal_Code': postal_code,
                'Customer_Latitude': latitude,
                'Customer_Longitude': longitude,
                'Secondary_Country_Name': fake.country(),
                # US country code for secondary contact
                'Secondary_Country_Code': country_code,
                'Secondary_Contact_Type': random.choice(['Email', 'Phone']),
                'Secondary_Phone_Number': phone_number,
                'Secondary_Email_Type': random.choice(['Personal', 'Work']),
                'Secondary_Email': fake.email(),
                'Secondary_Address_Type': random.choice(['Home', 'Work']),
                'Secondary_Address_Line1': fake.street_address(),
                'Secondary_Address_Line2': fake.secondary_address(),
                'Secondary_Address_Line3': fake.building_number(),
                'Secondary_City_Name': fake.city(),
                'Secondary_State_Prov': fake.state(),
                'Secondary_Postal_Code': fake.postcode(),
                'Secondary_Latitude': fake.latitude(),
                'Secondary_Longitude': fake.longitude(),
                'Customer_Occipation': occupation,
                'Customer_Maritial_Status': marital_status,
                'Customer_Perferred_Language': preferred_language,
                'Primary_Credit_Card': primary_credit_card,
                'Primary_Credit_Card_Expiry_Month': primary_cc_expiry_month,
                'Primary_Credit_Card_Expiry_Year': primary_cc_expiry_year,
                'Secondary_Credit_Card': secondary_credit_card,
                'Secondary_Credit_Card_Expiry_Month': secondary_cc_expiry_month,
                'Secondary_Credit_Card_Expiry_Year': secondary_cc_expiry_year,
                'Customer_Anniversary': anniversary,
                'Customer_Registration_Date': registration_date,
                'Customer_IncomeLevel': income_level,
                'Customer_Allergies': food_allergies,
                'Government_Identity_Proof': government_id_proof,
                'Government_Identity_Number': government_id_number,
                'Government_Identity_Expiry_Date': government_id_expiry_date,
                'Special_Event': special_event,
                'Special_Event_Date': special_event_date,
                'Last_Purchase_Date': last_purchase_date,
                'Last_Purchase_Time': last_purchase_time,
                'LoyaltyPoints_MemberStatus': loyalty_points_status,
                'Customer_Segment': customer_segment,
                'Customer_Lead_Source': customer_lead_source,
                'Survey_date': survey_date,
                'Survey_Time': survey_time,
                'Survey_Question': question['question'],
                'Survey_Answer': survey_result,
                'Survey_Recommendation': question['recommendations'][survey_result],
                'Survey_Rating': self.get_rating_from_answer(survey_result),
            }
            self.customers.add(customer_id)
            yield customer_data

    def get_data(self):
        return {
            'customers': list(self.customers),
        }

    def get_rating_from_answer(self, answer):
        if answer == 'Excellent':
            return random.randint(4, 5)
        elif answer == 'Good':
            return random.randint(3, 4)
        elif answer == 'Average':
            return random.randint(2, 3)
        elif answer == 'Poor':
            return random.randint(1, 2)


class Menu:
    def __init__(self):
        self.menu_items = []

    def generate_menu_items(self):
        fine_dining_menu = [
            {
                'Menu_Item_UID': 1,
                'Menu_Item_Name': 'Tomato Soup',
                'Menu_Item_Category': 'Soup',
                'Menu_Item_Description': 'Classic tomato soup.',
                'Menu_Item_Type': 'Veg', 'Menu_Item_Price': 100.00,
                'Menu_Item_Cost_Price': 50.00,
                'Menu_Item_Ingredients': 'Tomatoes, herbs, spices'
            },
            {
                'Menu_Item_UID': 2,
                'Menu_Item_Name': 'Hot & Sour Veggie Soup',
                'Menu_Item_Category': 'Soup',
                'Menu_Item_Description': 'Spicy and tangy soup with vegetables.',
                'Menu_Item_Type': 'Veg',
                'Menu_Item_Price': 120.00,
                'Menu_Item_Cost_Price': 60.00,
                'Menu_Item_Ingredients': 'Vegetables, spices'
            },
            {
                'Menu_Item_UID': 3,
                'Menu_Item_Name': 'Hot & Sour Chicken Soup',
                'Menu_Item_Category': 'Soup',
                'Menu_Item_Description': 'Spicy and tangy soup with chicken.',
                'Menu_Item_Type': 'Non-Veg',
                'Menu_Item_Price': 170.00,
                'Menu_Item_Cost_Price': 90.00,
                'Menu_Item_Ingredients': 'chicken, spices'
            },
            {
                'Menu_Item_UID': 4,
                'Menu_Item_Name': 'Sweet Corn Veggie Soup',
                'Menu_Item_Category': 'Soup',
                'Menu_Item_Description': 'Delicious sweet corn soup with veggies.',
                'Menu_Item_Type': 'Veg',
                'Menu_Item_Price': 110.00,
                'Menu_Item_Cost_Price': 55.00,
                'Menu_Item_Ingredients': 'Sweet corn, veggies, spices'
            },
            {
                'Menu_Item_UID': 5,
                'Menu_Item_Name': 'Sweet Corn Chicken Soup',
                'Menu_Item_Category': 'Soup',
                'Menu_Item_Description': 'Delicious sweet corn soup with of chicken.',
                'Menu_Item_Type': 'Non-Veg',
                'Menu_Item_Price': 140.00,
                'Menu_Item_Cost_Price': 88.00,
                'Menu_Item_Ingredients': 'Sweet corn, chicken, spices'
            },
            {
                'Menu_Item_UID': 6,
                'Menu_Item_Name': 'Lemon Coriander Veggie Soup',
                'Menu_Item_Category': 'Soup',
                'Menu_Item_Description': 'Refreshing soup with lemon, veggie and coriander flavor.',
                'Menu_Item_Type': 'Veg',
                'Menu_Item_Price': 130.00,
                'Menu_Item_Cost_Price': 65.00,
                'Menu_Item_Ingredients': 'Lemon, coriander, veggies, spices'
            },
            {
                'Menu_Item_UID': 7,
                'Menu_Item_Name': 'Lemon Coriander Chicken Soup',
                'Menu_Item_Category': 'Soup',
                'Menu_Item_Description': 'Refreshing soup with lemon, chicken and coriander flavor.',
                'Menu_Item_Type': 'Non-Veg',
                'Menu_Item_Price': 170.00,
                'Menu_Item_Cost_Price': 95.00,
                'Menu_Item_Ingredients': 'Lemon, coriander, chicken, spices'
            },
            {
                'Menu_Item_UID': 8,
                'Menu_Item_Name': 'Manchow Veggie Soup',
                'Menu_Item_Category': 'Soup',
                'Menu_Item_Description': 'Spicy and flavorful Manchow soup with veggies.',
                'Menu_Item_Type': 'Veg',
                'Menu_Item_Price': 140.00,
                'Menu_Item_Cost_Price': 70.00,
                'Menu_Item_Ingredients': 'Vegetables, noodles, spices'
            },
            {
                'Menu_Item_UID': 9,
                'Menu_Item_Name': 'Manchow Chicken Soup',
                'Menu_Item_Category': 'Soup',
                'Menu_Item_Description': 'Spicy and flavorful Manchow soup with chicken.',
                'Menu_Item_Type': 'Non-Veg',
                'Menu_Item_Price': 160.00,
                'Menu_Item_Cost_Price': 95.00,
                'Menu_Item_Ingredients': 'Chicken, noodles, spices'
            },
            {
                'Menu_Item_UID': 10,
                'Menu_Item_Name': 'Cheese Corn Bites',
                'Menu_Item_Category': 'Starters',
                'Menu_Item_Description': 'Crispy bites with cheese and corn.',
                'Menu_Item_Type': 'Veg',
                'Menu_Item_Price': 120.00,
                'Menu_Item_Cost_Price': 60.00,
                'Menu_Item_Ingredients': 'Cheese, corn, spices'
            },
            {
                'Menu_Item_UID': 11,
                'Menu_Item_Name': 'Cheese Chilli Mushroom',
                'Menu_Item_Category': 'Starters',
                'Menu_Item_Description': 'Spicy cheese and chilli coated mushrooms.',
                'Menu_Item_Type': 'Veg',
                'Menu_Item_Price': 130.00,
                'Menu_Item_Cost_Price': 70.00,
                'Menu_Item_Ingredients': 'Cheese, chilli, mushroom, spices'
            },
            {
                'Menu_Item_UID': 12,
                'Menu_Item_Name': 'Mushroom Salt & Pepper',
                'Menu_Item_Category': 'Starters',
                'Menu_Item_Description': 'Mushrooms seasoned with salt and pepper.',
                'Menu_Item_Type': 'Veg',
                'Menu_Item_Price': 110.00,
                'Menu_Item_Cost_Price': 55.00,
                'Menu_Item_Ingredients': 'Mushrooms, salt, pepper, spices'
            },
            {
                'Menu_Item_UID': 13,
                'Menu_Item_Name': 'Veg Manchurian Dry',
                'Menu_Item_Category': 'Starters',
                'Menu_Item_Description': 'Crispy veg balls in Manchurian sauce.',
                'Menu_Item_Type': 'Veg',
                'Menu_Item_Price': 140.00,
                'Menu_Item_Cost_Price': 75.00,
                'Menu_Item_Ingredients': 'Vegetables, Manchurian sauce, spices'
            },
            {
                'Menu_Item_UID': 14,
                'Menu_Item_Name': 'Veg Spring Roll',
                'Menu_Item_Category': 'Starters',
                'Menu_Item_Description': 'Crispy spring rolls filled with veggies.',
                'Menu_Item_Type': 'Veg',
                'Menu_Item_Price': 120.00,
                'Menu_Item_Cost_Price': 65.00,
                'Menu_Item_Ingredients': 'Vegetables, spring roll sheet, spices'
            },
            {
                'Menu_Item_UID': 15,
                'Menu_Item_Name': 'Paneer Papper Chilli',
                'Menu_Item_Category': 'Starters',
                'Menu_Item_Description': 'Spicy paneer cubes with bell peppers.',
                'Menu_Item_Type': 'Veg',
                'Menu_Item_Price': 150.00,
                'Menu_Item_Cost_Price': 80.00,
                'Menu_Item_Ingredients': 'Paneer, bell peppers, chilli, spices'
            },
            {
                'Menu_Item_UID': 16,
                'Menu_Item_Name': 'Paneer Satay',
                'Menu_Item_Category': 'Starters',
                'Menu_Item_Description': 'Grilled paneer skewers with satay sauce.',
                'Menu_Item_Type': 'Veg',
                'Menu_Item_Price': 160.00,
                'Menu_Item_Cost_Price': 85.00,
                'Menu_Item_Ingredients': 'Paneer, satay sauce, spices'
            },
            {
                'Menu_Item_UID': 17,
                'Menu_Item_Name': 'Chicken Lollipop',
                'Menu_Item_Category': 'Starters',
                'Menu_Item_Description': 'Crispy chicken lollipops with a flavorful coating.',
                'Menu_Item_Type': 'Non-Veg',
                'Menu_Item_Price': 180.00,
                'Menu_Item_Cost_Price': 100.00,
                'Menu_Item_Ingredients': 'Chicken, spices'
            },
            {
                'Menu_Item_UID': 18,
                'Menu_Item_Name': 'Chilli Chicken',
                'Menu_Item_Category': 'Starters',
                'Menu_Item_Description': 'Spicy and flavorful Chilli Chicken.',
                'Menu_Item_Type': 'Non-Veg',
                'Menu_Item_Price': 160.00,
                'Menu_Item_Cost_Price': 85.00,
                'Menu_Item_Ingredients': 'Chicken, chilli, spices'
            },
            {
                'Menu_Item_UID': 19,
                'Menu_Item_Name': 'Chicken Satay',
                'Menu_Item_Category': 'Starters',
                'Menu_Item_Description': 'Grilled chicken skewers with satay sauce.',
                'Menu_Item_Type': 'Non-Veg',
                'Menu_Item_Price': 170.00,
                'Menu_Item_Cost_Price': 90.00,
                'Menu_Item_Ingredients': 'Chicken, satay sauce, spices'
            },
            {
                'Menu_Item_UID': 20,
                'Menu_Item_Name': 'Buffalo Wings',
                'Menu_Item_Category': 'Starters',
                'Menu_Item_Description': 'Spicy and tangy buffalo wings.',
                'Menu_Item_Type': 'Non-Veg',
                'Menu_Item_Price': 150.00,
                'Menu_Item_Cost_Price': 80.00,
                'Menu_Item_Ingredients': 'Chicken wings, buffalo sauce, spices'
            },
            {
                'Menu_Item_UID': 21,
                'Menu_Item_Name': 'Chicken China Town',
                'Menu_Item_Category': 'Starters',
                'Menu_Item_Description': 'Flavorful chicken stir-fry with Chinese spices.',
                'Menu_Item_Type': 'Non-Veg',
                'Menu_Item_Price': 190.00,
                'Menu_Item_Cost_Price': 110.00,
                'Menu_Item_Ingredients': 'Chicken, vegetables, Chinese spices'
            },
            {
                'Menu_Item_UID': 22,
                'Menu_Item_Name': 'Mongolian Chicken',
                'Menu_Item_Category': 'Starters',
                'Menu_Item_Description': 'Stir-fried chicken with Mongolian sauce.',
                'Menu_Item_Type': 'Non-Veg',
                'Menu_Item_Price': 180.00,
                'Menu_Item_Cost_Price': 95.00,
                'Menu_Item_Ingredients': 'Chicken, Mongolian sauce, vegetables'
            },
            {
                'Menu_Item_UID': 23,
                'Menu_Item_Name': 'Fish Finger (Basa)',
                'Menu_Item_Category': 'Starters',
                'Menu_Item_Description': 'Crispy fish fingers made with Basa fish.',
                'Menu_Item_Type': 'Non-Veg',
                'Menu_Item_Price': 160.00,
                'Menu_Item_Cost_Price': 90.00,
                'Menu_Item_Ingredients': 'Basa fish, breadcrumbs, spices'
            },
            {
                'Menu_Item_UID': 24,
                'Menu_Item_Name': 'Chilli Garlic Fish',
                'Menu_Item_Category': 'Starters',
                'Menu_Item_Description': 'Spicy and garlicky fish preparation.',
                'Menu_Item_Type': 'Non-Veg',
                'Menu_Item_Price': 170.00,
                'Menu_Item_Cost_Price': 95.00,
                'Menu_Item_Ingredients': 'Fish, chilli, garlic, spices'
            },
            {
                'Menu_Item_UID': 25,
                'Menu_Item_Name': 'Mutton Lime Chilli',
                'Menu_Item_Category': 'Starters',
                'Menu_Item_Description': 'Spicy and tangy mutton preparation.',
                'Menu_Item_Type': 'Non-Veg',
                'Menu_Item_Price': 200.00,
                'Menu_Item_Cost_Price': 120.00,
                'Menu_Item_Ingredients': 'Mutton, lime, chilli, spices'
            },
            {
                'Menu_Item_UID': 26,
                'Menu_Item_Name': 'Butter Garlic Prawns',
                'Menu_Item_Category': 'Starters',
                'Menu_Item_Description': 'Juicy prawns in a buttery garlic sauce.',
                'Menu_Item_Type': 'Non-Veg',
                'Menu_Item_Price': 210.00,
                'Menu_Item_Cost_Price': 130.00,
                'Menu_Item_Ingredients': 'Prawns, butter, garlic, spices'
            },
            {
                'Menu_Item_UID': 27,
                'Menu_Item_Name': 'Prawns Chilli',
                'Menu_Item_Category': 'Starters',
                'Menu_Item_Description': 'Spicy chilli prawns.',
                'Menu_Item_Type': 'Non-Veg',
                'Menu_Item_Price': 190.00,
                'Menu_Item_Cost_Price': 110.00,
                'Menu_Item_Ingredients': 'Prawns, chilli, spices'
            },
            {
                'Menu_Item_UID': 28,
                'Menu_Item_Name': 'Papad (Roasted/Fried)',
                'Menu_Item_Category': 'Chakna',
                'Menu_Item_Description': 'Roasted or fried papads for munching.',
                'Menu_Item_Type': 'Veg',
                'Menu_Item_Price': 50.00,
                'Menu_Item_Cost_Price': 25.00,
                'Menu_Item_Ingredients': 'Papad, oil, spices'
            },
            {
                'Menu_Item_UID': 29,
                'Menu_Item_Name': 'Masala Papad',
                'Menu_Item_Category': 'Chakna',
                'Menu_Item_Description': 'Crispy papad topped with masala.',
                'Menu_Item_Type': 'Veg',
                'Menu_Item_Price': 60.00,
                'Menu_Item_Cost_Price': 30.00,
                'Menu_Item_Ingredients': 'Papad, masala, spices'
            },
            {
                'Menu_Item_UID': 30,
                'Menu_Item_Name': 'Peanuts (Roasted/Masala)',
                'Menu_Item_Category': 'Chakna',
                'Menu_Item_Description': 'Roasted or masala-coated peanuts.',
                'Menu_Item_Type': 'Veg',
                'Menu_Item_Price': 40.00,
                'Menu_Item_Cost_Price': 20.00,
                'Menu_Item_Ingredients': 'Peanuts, spices'
            },
            {
                'Menu_Item_UID': 31,
                'Menu_Item_Name': 'Cheese Cherry Pineapple',
                'Menu_Item_Category': 'Chakna',
                'Menu_Item_Description': 'Cheese cubes with cherries and pineapple.',
                'Menu_Item_Type': 'Veg',
                'Menu_Item_Price': 70.00,
                'Menu_Item_Cost_Price': 35.00,
                'Menu_Item_Ingredients': 'Cheese, cherries, pineapple'
            },
            {
                'Menu_Item_UID': 32,
                'Menu_Item_Name': 'French Fries',
                'Menu_Item_Category': 'Chakna',
                'Menu_Item_Description': 'Classic french fries.',
                'Menu_Item_Type': 'Veg',
                'Menu_Item_Price': 50.00,
                'Menu_Item_Cost_Price': 25.00,
                'Menu_Item_Ingredients': 'Potatoes, oil, spices'
            },
            {
                'Menu_Item_UID': 33,
                'Menu_Item_Name': 'Mexican Potato Wedges',
                'Menu_Item_Category': 'Chakna',
                'Menu_Item_Description': 'Spicy potato wedges with Mexican flavors.',
                'Menu_Item_Type': 'Veg',
                'Menu_Item_Price': 60.00,
                'Menu_Item_Cost_Price': 30.00,
                'Menu_Item_Ingredients': 'Potatoes, spices, Mexican seasoning'
            },
            {
                'Menu_Item_UID': 34,
                'Menu_Item_Name': 'Cheese Fritters',
                'Menu_Item_Category': 'Chakna',
                'Menu_Item_Description': 'Crispy cheese fritters.',
                'Menu_Item_Type': 'Veg',
                'Menu_Item_Price': 80.00,
                'Menu_Item_Cost_Price': 40.00,
                'Menu_Item_Ingredients': 'Cheese, batter, spices'
            },
            {
                'Menu_Item_UID': 35,
                'Menu_Item_Name': 'Chispy Corns',
                'Menu_Item_Category': 'Chakna',
                'Menu_Item_Description': 'Crispy and spicy corn kernels.',
                'Menu_Item_Type': 'Veg',
                'Menu_Item_Price': 70.00,
                'Menu_Item_Cost_Price': 35.00,
                'Menu_Item_Ingredients': 'Corn, batter, spices'
            },
            {
                'Menu_Item_UID': 36,
                'Menu_Item_Name': 'Garden Green Salad',
                'Menu_Item_Category': 'Salads',
                'Menu_Item_Description': 'Fresh garden salad with greens and veggies.',
                'Menu_Item_Type': 'Veg',
                'Menu_Item_Price': 80.00,
                'Menu_Item_Cost_Price': 40.00,
                'Menu_Item_Ingredients': 'Greens, veggies, dressing'
            },
            {
                'Menu_Item_UID': 37,
                'Menu_Item_Name': 'Coleslaw Salad',
                'Menu_Item_Category': 'Salads',
                'Menu_Item_Description': 'Crispy coleslaw salad with cabbage and carrots.',
                'Menu_Item_Type': 'Veg',
                'Menu_Item_Price': 70.00,
                'Menu_Item_Cost_Price': 35.00,
                'Menu_Item_Ingredients': 'Cabbage, carrots, dressing'
            },
            {
                'Menu_Item_UID': 38,
                'Menu_Item_Name': 'Caesar Salad (Veg)',
                'Menu_Item_Category': 'Salads',
                'Menu_Item_Description': 'Classic Caesar salad with veggies.',
                'Menu_Item_Type': 'Veg',
                'Menu_Item_Price': 90.00,
                'Menu_Item_Cost_Price': 45.00,
                'Menu_Item_Ingredients': 'Lettuce, croutons, Caesar dressing'
            },
            {
                'Menu_Item_UID': 39,
                'Menu_Item_Name': 'Caesar Salad (Chicken)',
                'Menu_Item_Category': 'Salads',
                'Menu_Item_Description': 'Classic Caesar salad with grilled chicken.',
                'Menu_Item_Type': 'Non-Veg',
                'Menu_Item_Price': 120.00,
                'Menu_Item_Cost_Price': 70.00,
                'Menu_Item_Ingredients': 'Lettuce, croutons, grilled chicken, Caesar dressing'
            },
            {
                'Menu_Item_UID': 40,
                'Menu_Item_Name': 'Amritsari Paneer Bhurji',
                'Menu_Item_Category': 'Main Course',
                'Menu_Item_Description': 'Spicy scrambled paneer with Amritsari flavors.',
                'Menu_Item_Type': 'Veg',
                'Menu_Item_Price': 150.00,
                'Menu_Item_Cost_Price': 80.00,
                'Menu_Item_Ingredients': 'Paneer, spices'
            },
            {
                'Menu_Item_UID': 41,
                'Menu_Item_Name': 'Rasoi Paneer Makhani',
                'Menu_Item_Category': 'Main Course',
                'Menu_Item_Description': 'Paneer in a rich and creamy tomato-based gravy.',
                'Menu_Item_Type': 'Veg',
                'Menu_Item_Price': 170.00,
                'Menu_Item_Cost_Price': 90.00,
                'Menu_Item_Ingredients': 'Paneer, tomatoes, cream, spices'
            },
            {
                'Menu_Item_UID': 42,
                'Menu_Item_Name': 'Paneer Khurchan',
                'Menu_Item_Category': 'Main Course',
                'Menu_Item_Description': 'Paneer cooked with bell peppers and spices.',
                'Menu_Item_Type': 'Veg',
                'Menu_Item_Price': 160.00,
                'Menu_Item_Cost_Price': 85.00,
                'Menu_Item_Ingredients': 'Paneer, bell peppers, spices'
            },
            {
                'Menu_Item_UID': 43,
                'Menu_Item_Name': 'Paneer Tikka Masala',
                'Menu_Item_Category': 'Main Course',
                'Menu_Item_Description': 'Paneer tikka in a flavorful masala gravy.',
                'Menu_Item_Type': 'Veg',
                'Menu_Item_Price': 180.00,
                'Menu_Item_Cost_Price': 95.00,
                'Menu_Item_Ingredients': 'Paneer, tikka masala, spices'
            },
            {
                'Menu_Item_UID': 44,
                'Menu_Item_Name': 'Kadai Paneer',
                'Menu_Item_Category': 'Main Course',
                'Menu_Item_Description': 'Paneer cooked in a kadai with aromatic spices.',
                'Menu_Item_Type': 'Veg',
                'Menu_Item_Price': 160.00,
                'Menu_Item_Cost_Price': 80.00,
                'Menu_Item_Ingredients': 'Paneer, spices'
            },
            {
                'Menu_Item_UID': 45,
                'Menu_Item_Name': 'Paneer Angara Masala',
                'Menu_Item_Category': 'Main Course',
                'Menu_Item_Description': 'Spicy and smoky paneer preparation.',
                'Menu_Item_Type': 'Veg',
                'Menu_Item_Price': 170.00,
                'Menu_Item_Cost_Price': 90.00,
                'Menu_Item_Ingredients': 'Paneer, spices, smoky flavor'
            },
            {
                'Menu_Item_UID': 46,
                'Menu_Item_Name': 'Palak Paneer',
                'Menu_Item_Category': 'Main Course',
                'Menu_Item_Description': 'Paneer in a creamy spinach gravy.',
                'Menu_Item_Type': 'Veg',
                'Menu_Item_Price': 150.00,
                'Menu_Item_Cost_Price': 75.00,
                'Menu_Item_Ingredients': 'Paneer, spinach, cream, spices'
            },
            {
                'Menu_Item_UID': 47,
                'Menu_Item_Name': 'Sarson Da Daag',
                'Menu_Item_Category': 'Main Course',
                'Menu_Item_Description': 'Paneer in a mustard-flavored gravy.',
                'Menu_Item_Type': 'Veg',
                'Menu_Item_Price': 160.00,
                'Menu_Item_Cost_Price': 80.00,
                'Menu_Item_Ingredients': 'Paneer, mustard, spices'
            },
            {
                'Menu_Item_UID': 48,
                'Menu_Item_Name': 'Punjabi Chole Masala',
                'Menu_Item_Category': 'Main Course',
                'Menu_Item_Description': 'Spicy and tangy chickpeas curry.',
                'Menu_Item_Type': 'Veg',
                'Menu_Item_Price': 140.00,
                'Menu_Item_Cost_Price': 70.00,
                'Menu_Item_Ingredients': 'Chickpeas, spices'
            },
            {
                'Menu_Item_UID': 49,
                'Menu_Item_Name': 'Malai Kofta',
                'Menu_Item_Category': 'Main Course',
                'Menu_Item_Description': 'Vegetable dumplings in a creamy tomato-based gravy.',
                'Menu_Item_Type': 'Veg',
                'Menu_Item_Price': 180.00,
                'Menu_Item_Cost_Price': 90.00,
                'Menu_Item_Ingredients': 'Vegetables, kofta, cream, spices'
            },
            {
                'Menu_Item_UID': 50,
                'Menu_Item_Name': 'Rasoi Murg Makhani',
                'Menu_Item_Category': 'Main Course',
                'Menu_Item_Description': 'Butter chicken in a rich and creamy tomato-based gravy.',
                'Menu_Item_Type': 'Non-Veg',
                'Menu_Item_Price': 200.00,
                'Menu_Item_Cost_Price': 120.00,
                'Menu_Item_Ingredients': 'Chicken, tomatoes, cream, spices'
            },
            {
                'Menu_Item_UID': 51,
                'Menu_Item_Name': 'Rasoi Chicken Handi',
                'Menu_Item_Category': 'Main Course',
                'Menu_Item_Description': 'Chicken cooked in a traditional handi with aromatic spices.',
                'Menu_Item_Type': 'Non-Veg',
                'Menu_Item_Price': 190.00,
                'Menu_Item_Cost_Price': 100.00,
                'Menu_Item_Ingredients': 'Chicken, spices'
            },
            {
                'Menu_Item_UID': 52,
                'Menu_Item_Name': 'Murg Matka Handi',
                'Menu_Item_Category': 'Main Course',
                'Menu_Item_Description': 'Chicken curry cooked in a matka with special spices.',
                'Menu_Item_Type': 'Non-Veg',
                'Menu_Item_Price': 180.00,
                'Menu_Item_Cost_Price': 95.00,
                'Menu_Item_Ingredients': 'Chicken, spices'
            },
            {
                'Menu_Item_UID': 53,
                'Menu_Item_Name': 'Chicken Achari Kolhapuri',
                'Menu_Item_Category': 'Main Course',
                'Menu_Item_Description': 'Chicken curry with achari and Kolhapuri flavors.',
                'Menu_Item_Type': 'Non-Veg',
                'Menu_Item_Price': 210.00,
                'Menu_Item_Cost_Price': 120.00,
                'Menu_Item_Ingredients': 'Chicken, achari spices, Kolhapuri spices'
            },
            {
                'Menu_Item_UID': 54,
                'Menu_Item_Name': 'Murg Tikka Lababdar',
                'Menu_Item_Category': 'Main Course',
                'Menu_Item_Description': 'Chicken tikka in a rich and flavorful lababdar gravy.',
                'Menu_Item_Type': 'Non-Veg',
                'Menu_Item_Price': 220.00,
                'Menu_Item_Cost_Price': 130.00,
                'Menu_Item_Ingredients': 'Chicken tikka, lababdar gravy, spices'
            },
            {
                'Menu_Item_UID': 55,
                'Menu_Item_Name': 'Murg Tikka Masala',
                'Menu_Item_Category': 'Main Course',
                'Menu_Item_Description': 'Chicken tikka in a spicy masala gravy.',
                'Menu_Item_Type': 'Non-Veg',
                'Menu_Item_Price': 210.00,
                'Menu_Item_Cost_Price': 110.00,
                'Menu_Item_Ingredients': 'Chicken tikka, masala gravy, spices'
            },
            {
                'Menu_Item_UID': 56,
                'Menu_Item_Name': 'Murg Afghani',
                'Menu_Item_Category': 'Main Course',
                'Menu_Item_Description': 'Afghani-style chicken preparation.',
                'Menu_Item_Type': 'Non-Veg',
                'Menu_Item_Price': 200.00,
                'Menu_Item_Cost_Price': 100.00,
                'Menu_Item_Ingredients': 'Chicken, Afghani spices'
            },
            {
                'Menu_Item_UID': 57,
                'Menu_Item_Name': 'Lahori Murg',
                'Menu_Item_Category': 'Main Course',
                'Menu_Item_Description': 'Chicken curry with Lahori flavors.',
                'Menu_Item_Type': 'Non-Veg',
                'Menu_Item_Price': 190.00,
                'Menu_Item_Cost_Price': 95.00,
                'Menu_Item_Ingredients': 'Chicken, Lahori spices'
            },
            {
                'Menu_Item_UID': 58,
                'Menu_Item_Name': 'Chicken Keema Methi Khaas',
                'Menu_Item_Category': 'Main Course',
                'Menu_Item_Description': 'Minced chicken curry with fenugreek leaves.',
                'Menu_Item_Type': 'Non-Veg',
                'Menu_Item_Price': 180.00,
                'Menu_Item_Cost_Price': 90.00,
                'Menu_Item_Ingredients': 'Minced chicken, fenugreek leaves, spices'
            },
            {
                'Menu_Item_UID': 59,
                'Menu_Item_Name': 'Chicken Manchurian',
                'Menu_Item_Category': 'Main Course',
                'Menu_Item_Description': 'Indo-Chinese style chicken Manchurian.',
                'Menu_Item_Type': 'Non-Veg',
                'Menu_Item_Price': 190.00,
                'Menu_Item_Cost_Price': 100.00,
                'Menu_Item_Ingredients': 'Chicken, Manchurian sauce, spices'
            },
            {
                'Menu_Item_UID': 60,
                'Menu_Item_Name': 'Kashmiri Mutton',
                'Menu_Item_Category': 'Main Course',
                'Menu_Item_Description': 'Mutton curry with Kashmiri spices.',
                'Menu_Item_Type': 'Non-Veg',
                'Menu_Item_Price': 220.00,
                'Menu_Item_Cost_Price': 120.00,
                'Menu_Item_Ingredients': 'Mutton, Kashmiri spices'
            },
            {
                'Menu_Item_UID': 61,
                'Menu_Item_Name': 'Laal Mutton',
                'Menu_Item_Category': 'Main Course',
                'Menu_Item_Description': 'Spicy red mutton curry.',
                'Menu_Item_Type': 'Non-Veg',
                'Menu_Item_Price': 230.00,
                'Menu_Item_Cost_Price': 130.00,
                'Menu_Item_Ingredients': 'Mutton, spices'
            },
            {
                'Menu_Item_UID': 62,
                'Menu_Item_Name': 'Jhunga Masala',
                'Menu_Item_Category': 'Main Course',
                'Menu_Item_Description': 'Prawn curry with special masala.',
                'Menu_Item_Type': 'Non-Veg',
                'Menu_Item_Price': 240.00,
                'Menu_Item_Cost_Price': 140.00,
                'Menu_Item_Ingredients': 'Prawns, masala, spices'
            },
        ]
        self.menu_items = fine_dining_menu

    def get_data(self):
        return {
            'menu_items': self.menu_items,
        }


class Drinks:
    def __init__(self):
        self.drink_items = []

    def generate_drink_items(self):
        drinks_menu = [
            {
                'Drink_Item_UID': 1,
                'Drink_Item_Name': "Teacher's (60ml)",
                'Drink_Item_Category': 'Domestic Whisky',
                'Drink_Item_Description': 'Teacher\'s brand whisky.',
                'Drink_Item_Volume': '60ml',
                'Drink_Item_Price': 150.00,
                'Drink_Item_Cost_Price': 80.00,
            },
            {
                'Drink_Item_UID': 2,
                'Drink_Item_Name': "Ballentine's (60ml)",
                'Drink_Item_Category': 'Domestic Whisky',
                'Drink_Item_Description': 'Ballentine\'s brand whisky.',
                'Drink_Item_Volume': '60ml',
                'Drink_Item_Price': 160.00,
                'Drink_Item_Cost_Price': 85.00,
            },
            {
                'Drink_Item_UID': 3,
                'Drink_Item_Name': "100 Pipers (60ml)",
                'Drink_Item_Category': 'Domestic Whisky',
                'Drink_Item_Description': '100 Pipers brand whisky.',
                'Drink_Item_Volume': '60ml',
                'Drink_Item_Price': 170.00,
                'Drink_Item_Cost_Price': 90.00,
            },
            {
                'Drink_Item_UID': 4,
                'Drink_Item_Name': "Black Dog (60ml)",
                'Drink_Item_Category': 'Domestic Whisky',
                'Drink_Item_Description': 'Black Dog brand whisky.',
                'Drink_Item_Volume': '60ml',
                'Drink_Item_Price': 180.00,
                'Drink_Item_Cost_Price': 95.00,
            },
            {
                'Drink_Item_UID': 5,
                'Drink_Item_Name': "Black & White (60ml)",
                'Drink_Item_Category': 'Domestic Whisky',
                'Drink_Item_Description': 'Black & White brand whisky.',
                'Drink_Item_Volume': '60ml',
                'Drink_Item_Price': 160.00,
                'Drink_Item_Cost_Price': 85.00,
            },
            {
                'Drink_Item_UID': 6,
                'Drink_Item_Name': "Vat 69 (60ml)",
                'Drink_Item_Category': 'Domestic Whisky',
                'Drink_Item_Description': 'Vat 69 brand whisky.',
                'Drink_Item_Volume': '60ml',
                'Drink_Item_Price': 150.00,
                'Drink_Item_Cost_Price': 80.00,
            },
            {
                'Drink_Item_UID': 7,
                'Drink_Item_Name': "Teacher's Highland Cream (60ml)",
                'Drink_Item_Category': 'Domestic Whisky',
                'Drink_Item_Description': 'Teacher\'s Highland Cream brand whisky.',
                'Drink_Item_Volume': '60ml',
                'Drink_Item_Price': 190.00,
                'Drink_Item_Cost_Price': 100.00,
            },
            {
                'Drink_Item_UID': 8,
                'Drink_Item_Name': "Blenders Pride Reserve (60ml)",
                'Drink_Item_Category': 'Domestic Whisky',
                'Drink_Item_Description': 'Blenders Pride Reserve brand whisky.',
                'Drink_Item_Volume': '60ml',
                'Drink_Item_Price': 200.00,
                'Drink_Item_Cost_Price': 110.00,
            },
            {
                'Drink_Item_UID': 9,
                'Drink_Item_Name': "Antiquity Blue (60ml)",
                'Drink_Item_Category': 'Domestic Whisky',
                'Drink_Item_Description': 'Antiquity Blue brand whisky.',
                'Drink_Item_Volume': '60ml',
                'Drink_Item_Price': 180.00,
                'Drink_Item_Cost_Price': 95.00,
            },
            {
                'Drink_Item_UID': 10,
                'Drink_Item_Name': "Blenders Pride (60ml)",
                'Drink_Item_Category': 'Domestic Whisky',
                'Drink_Item_Description': 'Blenders Pride brand whisky.',
                'Drink_Item_Volume': '60ml',
                'Drink_Item_Price': 170.00,
                'Drink_Item_Cost_Price': 90.00,
            },
            {
                'Drink_Item_UID': 11,
                'Drink_Item_Name': "Royal Stag (60ml)",
                'Drink_Item_Category': 'Domestic Whisky',
                'Drink_Item_Description': 'Royal Stag brand whisky.',
                'Drink_Item_Volume': '60ml',
                'Drink_Item_Price': 160.00,
                'Drink_Item_Cost_Price': 85.00,
            },
            {
                'Drink_Item_UID': 12,
                'Drink_Item_Name': "Oaksmith Silver (60ml)",
                'Drink_Item_Category': 'Domestic Whisky',
                'Drink_Item_Description': 'Oaksmith Silver brand whisky.',
                'Drink_Item_Volume': '60ml',
                'Drink_Item_Price': 180.00,
                'Drink_Item_Cost_Price': 95.00,
            },
            {
                'Drink_Item_UID': 13,
                'Drink_Item_Name': "Oaksmith Gold (60ml)",
                'Drink_Item_Category': 'Domestic Whisky',
                'Drink_Item_Description': 'Oaksmith Gold brand whisky.',
                'Drink_Item_Volume': '60ml',
                'Drink_Item_Price': 190.00,
                'Drink_Item_Cost_Price': 100.00,
            },
            {
                'Drink_Item_UID': 14,
                'Drink_Item_Name': 'Chivas Regal (60ml)',
                'Drink_Item_Category': 'Blended Scotch Whisky',
                'Drink_Item_Description': 'Chivas Regal brand whisky.',
                'Drink_Item_Volume': '60ml',
                'Drink_Item_Price': 250.00,
                'Drink_Item_Cost_Price': 120.00,
            },
            {
                'Drink_Item_UID': 15,
                'Drink_Item_Name': 'J.W. Black Label (60ml)',
                'Drink_Item_Category': 'Blended Scotch Whisky',
                'Drink_Item_Description': 'Johnnie Walker Black Label brand whisky.',
                'Drink_Item_Volume': '60ml',
                'Drink_Item_Price': 260.00,
                'Drink_Item_Cost_Price': 130.00,
            },
            {
                'Drink_Item_UID': 16,
                'Drink_Item_Name': 'J.W. Red Label (60ml)',
                'Drink_Item_Category': 'Blended Scotch Whisky',
                'Drink_Item_Description': 'Johnnie Walker Red Label brand whisky.',
                'Drink_Item_Volume': '60ml',
                'Drink_Item_Price': 240.00,
                'Drink_Item_Cost_Price': 110.00,
            },
            {
                'Drink_Item_UID': 17,
                'Drink_Item_Name': 'Jameson (60ml)',
                'Drink_Item_Category': 'Blended Scotch Whisky',
                'Drink_Item_Description': 'Jameson brand whisky.',
                'Drink_Item_Volume': '60ml',
                'Drink_Item_Price': 230.00,
                'Drink_Item_Cost_Price': 100.00,
            },
            {
                'Drink_Item_UID': 18,
                'Drink_Item_Name': 'Glenfiddich 12 Years (60ml)',
                'Drink_Item_Category': 'Single Malt Whisky',
                'Drink_Item_Description': 'Glenfiddich 12 Years brand whisky.',
                'Drink_Item_Volume': '60ml',
                'Drink_Item_Price': 280.00,
                'Drink_Item_Cost_Price': 150.00,
            },
            {
                'Drink_Item_UID': 19,
                'Drink_Item_Name': 'Glenlivet (60ml)',
                'Drink_Item_Category': 'Single Malt Whisky',
                'Drink_Item_Description': 'Glenlivet brand whisky.',
                'Drink_Item_Volume': '60ml',
                'Drink_Item_Price': 270.00,
                'Drink_Item_Cost_Price': 140.00,
            },
            {
                'Drink_Item_UID': 20,
                'Drink_Item_Name': 'Glenmorangie (60ml)',
                'Drink_Item_Category': 'Single Malt Whisky',
                'Drink_Item_Description': 'Glenmorangie brand whisky.',
                'Drink_Item_Volume': '60ml',
                'Drink_Item_Price': 290.00,
                'Drink_Item_Cost_Price': 160.00,
            },
            {
                'Drink_Item_UID': 21,
                'Drink_Item_Name': 'Jack Daniel (60ml)',
                'Drink_Item_Category': 'Tennessee & Bourbon Whisky',
                'Drink_Item_Description': 'Jack Daniel brand whisky.',
                'Drink_Item_Volume': '60ml',
                'Drink_Item_Price': 220.00,
                'Drink_Item_Cost_Price': 100.00,
            },
            {
                'Drink_Item_UID': 22,
                'Drink_Item_Name': 'Jim Beam (60ml)',
                'Drink_Item_Category': 'Tennessee & Bourbon Whisky',
                'Drink_Item_Description': 'Jim Beam brand whisky.',
                'Drink_Item_Volume': '60ml',
                'Drink_Item_Price': 210.00,
                'Drink_Item_Cost_Price': 90.00,
            },
            {
                'Drink_Item_UID': 23,
                'Drink_Item_Name': 'Bacardi Superior (60ml)',
                'Drink_Item_Category': 'Rum',
                'Drink_Item_Description': 'Bacardi Superior brand rum.',
                'Drink_Item_Volume': '60ml',
                'Drink_Item_Price': 180.00,
                'Drink_Item_Cost_Price': 95.00,
            },
            {
                'Drink_Item_UID': 24,
                'Drink_Item_Name': 'Bacardi Flavours (60ml)',
                'Drink_Item_Category': 'Rum',
                'Drink_Item_Description': 'Bacardi Flavours brand rum.',
                'Drink_Item_Volume': '60ml',
                'Drink_Item_Price': 190.00,
                'Drink_Item_Cost_Price': 100.00,
            },
            {
                'Drink_Item_UID': 25,
                'Drink_Item_Name': 'Old Monk (60ml)',
                'Drink_Item_Category': 'Rum',
                'Drink_Item_Description': 'Old Monk brand rum.',
                'Drink_Item_Volume': '60ml',
                'Drink_Item_Price': 170.00,
                'Drink_Item_Cost_Price': 90.00,
            },
            {
                'Drink_Item_UID': 26,
                'Drink_Item_Name': 'Silver Tequila (60ml)',
                'Drink_Item_Category': 'Tequila',
                'Drink_Item_Description': 'Silver Tequila.',
                'Drink_Item_Volume': '60ml',
                'Drink_Item_Price': 200.00,
                'Drink_Item_Cost_Price': 100.00,
            },
            {
                'Drink_Item_UID': 27,
                'Drink_Item_Name': 'Absolut (60ml)',
                'Drink_Item_Category': 'Vodka',
                'Drink_Item_Description': 'Absolut brand vodka.',
                'Drink_Item_Volume': '60ml',
                'Drink_Item_Price': 180.00,
                'Drink_Item_Cost_Price': 90.00,
            },
            {
                'Drink_Item_UID': 28,
                'Drink_Item_Name': 'Smirnoff/Flavours (60ml)',
                'Drink_Item_Category': 'Vodka',
                'Drink_Item_Description': 'Smirnoff/Flavours brand vodka.',
                'Drink_Item_Volume': '60ml',
                'Drink_Item_Price': 170.00,
                'Drink_Item_Cost_Price': 85.00,
            },
            {
                'Drink_Item_UID': 29,
                'Drink_Item_Name': 'Magic Moment Verve (60ml)',
                'Drink_Item_Category': 'Vodka',
                'Drink_Item_Description': 'Magic Moment Verve brand vodka.',
                'Drink_Item_Volume': '60ml',
                'Drink_Item_Price': 190.00,
                'Drink_Item_Cost_Price': 95.00,
            },
            {
                'Drink_Item_UID': 30,
                'Drink_Item_Name': 'Blue Riband (60ml)',
                'Drink_Item_Category': 'Gin',
                'Drink_Item_Description': 'Blue Riband brand gin.',
                'Drink_Item_Volume': '60ml',
                'Drink_Item_Price': 160.00,
                'Drink_Item_Cost_Price': 80.00,
            },
            {
                'Drink_Item_UID': 31,
                'Drink_Item_Name': 'Bombay Sapphire (60ml)',
                'Drink_Item_Category': 'Gin',
                'Drink_Item_Description': 'Bombay Sapphire brand gin.',
                'Drink_Item_Volume': '60ml',
                'Drink_Item_Price': 170.00,
                'Drink_Item_Cost_Price': 85.00,
            },
            {
                'Drink_Item_UID': 32,
                'Drink_Item_Name': 'Honey Bee (60ml)',
                'Drink_Item_Category': 'Brandy',
                'Drink_Item_Description': 'Honey Bee brand brandy.',
                'Drink_Item_Volume': '60ml',
                'Drink_Item_Price': 160.00,
                'Drink_Item_Cost_Price': 80.00,
            },
            {
                'Drink_Item_UID': 33,
                'Drink_Item_Name': 'Corona Extra (650ml)',
                'Drink_Item_Category': 'Beer',
                'Drink_Item_Description': 'Corona Extra brand beer.',
                'Drink_Item_Volume': '650ml',
                'Drink_Item_Price': 250.00,
                'Drink_Item_Cost_Price': 120.00,
            },
            {
                'Drink_Item_UID': 34,
                'Drink_Item_Name': 'Heineken (650ml)',
                'Drink_Item_Category': 'Beer',
                'Drink_Item_Description': 'Heineken brand beer.',
                'Drink_Item_Volume': '650ml',
                'Drink_Item_Price': 240.00,
                'Drink_Item_Cost_Price': 110.00,
            },
            {
                'Drink_Item_UID': 35,
                'Drink_Item_Name': 'Bira Blonde (650ml)',
                'Drink_Item_Category': 'Beer',
                'Drink_Item_Description': 'Bira Blonde brand beer.',
                'Drink_Item_Volume': '650ml',
                'Drink_Item_Price': 230.00,
                'Drink_Item_Cost_Price': 100.00,
            },
            {
                'Drink_Item_UID': 36,
                'Drink_Item_Name': 'Bira White (650ml)',
                'Drink_Item_Category': 'Beer',
                'Drink_Item_Description': 'Bira White brand beer.',
                'Drink_Item_Volume': '650ml',
                'Drink_Item_Price': 220.00,
                'Drink_Item_Cost_Price': 90.00,
            },
        ]
        self.drink_items = drinks_menu

    def get_data(self):
        return {
            'drink_items': self.drink_items,
        }


class Kitchen:
    def __init__(self):
        self.inventory = []

    def generate_inventory(self, num_items):
        ingredient_categories = {
            'Vegetables': ['Carrot', 'Broccoli', 'Spinach', 'Onion', 'Tomato', 'Bell Pepper', 'Cabbage', 'Potato', 'Cucumber', 'Lettuce', 'Zucchini', 'Mushroom', 'Eggplant', 'Radish', 'Artichoke', 'Asparagus', 'Kale', 'Pumpkin', 'Turnip', 'Celery'],
            'Meat': ['Chicken', 'Beef', 'Pork', 'Lamb', 'Turkey', 'Duck', 'Veal', 'Goat', 'Rabbit', 'Venison', 'Buffalo', 'Quail', 'Pheasant', 'Ostrich', 'Kangaroo', 'Alligator', 'Elk', 'Bison', 'Wild Boar', 'Emu'],
            'Dairy': ['Milk', 'Cheese', 'Yogurt', 'Butter', 'Cream', 'Sour Cream', 'Cottage Cheese', 'Whipped Cream', 'Condensed Milk', 'Evaporated Milk', 'Ghee', 'Clotted Cream', 'Mascarpone', 'Ricotta', 'Provolone', 'Feta', 'Mozzarella', 'Gouda', 'Swiss', 'Colby'],
            'Spices': ['Salt', 'Pepper', 'Paprika', 'Cumin', 'Cinnamon', 'Chili Powder', 'Garlic Powder', 'Onion Powder', 'Turmeric', 'Ginger', 'Mustard', 'Oregano', 'Basil', 'Rosemary', 'Thyme', 'Coriander', 'Nutmeg', 'Cardamom', 'Cloves', 'Allspice'],
            'Grains': ['Rice', 'Wheat Flour', 'Pasta', 'Quinoa', 'Barley', 'Oats', 'Cornmeal', 'Buckwheat', 'Couscous', 'Bulgur', 'Millet', 'Polenta', 'Rye', 'Farro', 'Spelt', 'Amaranth', 'Teff', 'Sorghum', 'Kamut', 'Freekeh']
        }
        payment_methods = ['Credit Card',
                           'Debit Card', 'Cash', 'Online Payment']

        ingredient_locations = ['Shelf A',
                                'Shelf B', 'Refrigerator', 'Freezer']
        ingredient_ids = [f'00A{i:02}' for i in range(1, num_items + 1)]

        for index, ingredient_id in enumerate(ingredient_ids):
            category = random.choice(list(ingredient_categories.keys()))
            ingredient_name = random.choice(ingredient_categories[category])
            ingredient_location = random.choice(ingredient_locations)

            purchase_date = fake.date_between(
                start_date='-3y', end_date='today')
            ingredient_cost = round(random.uniform(5, 50), 2)
            supplier_id = fake.uuid4()
            ingredient_quantity = random.randint(1, 100)
            expiration_date = fake.date_between(
                start_date='today', end_date='+2y')
            unit_measurement = fake.random_element(
                elements=['kg', 'grams', 'liters', 'pieces'])
            last_restocked_date = fake.date_between(
                start_date='-3y', end_date='today')

            inventory_data = {
                'Inventory_ID': index + 1,
                'Ingredient_ID': ingredient_id,
                'IngredientName': ingredient_name,
                'Ingredient_Category': category,
                'Ingredient_Location': ingredient_location,
                'Ingredient_Purchase_Date': purchase_date,
                'Ingredient_Cost': ingredient_cost,
                'IngredientSupplier_ID': supplier_id,
                'Ingredient_Quantity_Instock': ingredient_quantity,
                'Ingredient_Expiration_Date': expiration_date,
                'Unit_of_Measurement_of_Ingredient': unit_measurement,
                'Last_Restocked_Date': last_restocked_date,
            }
            # Supplier details
            supplier_name = fake.company()
            supplier_contact = fake.phone_number()
            supplier_address = fake.address()
            shipping_id = fake.uuid4()
            payment_id = fake.uuid4()
            payment_date = fake.date_between(
                start_date='-2y', end_date='today')
            payment_time = fake.time()
            payment_amount = round(random.uniform(100, 1000), 2)
            payment_method = fake.random_element(elements=payment_methods)
            amount_paid = round(random.uniform(100, payment_amount), 2)

            supplier_data = {
                'Supplier_ID': supplier_id,
                'Supplier_Name': supplier_name,
                'Supplier_Contact': supplier_contact,
                'Supplier_Address': supplier_address,
                'Shipping_ID': shipping_id,
                'Supplier_Payment_ID': payment_id,
                'Payment_Date': payment_date,
                'Payment_Time': payment_time,
                'Payment_Amount': payment_amount,
                'Payment_Method': payment_method,
                'Amount_Paid': amount_paid
            }

            inventory_data.update(supplier_data)
            self.inventory.append(inventory_data)

    def get_data(self):
        return self.inventory


class Staff:
    def __init__(self):
        self.staff_data = []

    def generate_staff_data(self, num_staff, restaurants):
        staff_roles = ['Manager', 'Chef', 'Waiter', 'Bartender',
                       'Host/Hostess', 'Sous Chef', 'Dishwasher', 'Server']
        titles = ['Mr.', 'Ms.', 'Mrs.', 'Dr.']
        positions = ['Full-time', 'Part-time']
        addresses = ['123 Main St', '456 Elm St',
                     '789 Oak St', '101 Pine St', '202 Maple St']
        start_times = ['08:00 AM', '09:00 AM',
                       '10:00 AM', '11:00 AM', '12:00 PM']
        end_times = ['04:00 PM', '05:00 PM',
                     '06:00 PM', '07:00 PM', '08:00 PM']

        for i in range(num_staff):
            staff_id = i + 1
            restaurant_id = random.choice(restaurants)['Restaurant_UID']
            staff_role = random.choice(staff_roles)
            title = random.choice(titles)
            first_name = fake.first_name()
            middle_name = fake.first_name()
            last_name = fake.last_name()
            position = random.choice(positions)
            email = fake.email()
            phone_number = fake.phone_number()
            dob = fake.date_of_birth(minimum_age=18, maximum_age=65)
            address = random.choice(addresses)
            hire_date = fake.date_between(start_date='-3y', end_date='today')
            salary = round(random.uniform(20000, 80000), 2)
            working_month = fake.month()
            start_time = random.choice(start_times)
            end_time = random.choice(end_times)
            hours_worked = random.randint(120, 220)
            hourly_wage = round(salary / hours_worked, 2)
            overtime_hours = max(random.randint(0, 40), hours_worked - 180)
            monthly_salary = salary + overtime_hours * hourly_wage
            tips_received = round(random.uniform(0, 500), 2)

            staff_data = {
                'Staff_ID': staff_id,
                'Restaurant_UID': restaurant_id,
                'Staff_Role': staff_role,
                'Staff_FirstName': first_name,
                'Staff_MiddleName': middle_name,
                'Staff_LastName': last_name,
                'Staff_Position': position,
                'Staff_Title': title,
                'Staff_Email': email,
                'Staff_Phone_Number': phone_number,
                'Staff_DateofBirth': dob,
                'Staff_Address': address,
                'Hire_Date': hire_date,
                'Staff_Salary': salary,
                'Working_Month': working_month,
                'Shift_StartTime': start_time,
                'Shift_EndTime': end_time,
                'Hour_Worked': hours_worked,
                'Hourly_Wage': hourly_wage,
                'Overtime_Hours': overtime_hours,
                'Monthly_Salary': monthly_salary,
                'Tips_Received': tips_received,
            }
            self.staff_data.append(staff_data)

    def get_data(self):
        return self.staff_data


class Order:
    def __init__(self):
        self.orders = []
        self.starting_order_id = 1001

    def generate_orders(self, num_orders, restaurants, customers, menu_items):
        guest_types = ['Co-operate', 'Individual']
        order_modifiers = ['Spicy', 'Extra cheese', 'Gluten-free', 'No onions']
        positive_feedback = [
            "The food was excellent!",
            "Great service and delicious food!",
            "Wonderful experience. Highly recommended!",
            "Loved the ambiance and the food quality.",
            "Amazing flavors and presentation.",
            "Absolutely delightful!",
            "The staff was friendly and attentive.",
            "Fantastic menu options and taste.",
            "Will definitely come back for more!",
            "An outstanding dining experience.",
            "Impressive service and taste!",
            "Exceeded my expectations.",
            "A delightful culinary journey!",
            "Perfect blend of flavors.",
            "Highly satisfied with the dining experience.",
            "Exceptional service and food quality.",
            "Impeccable presentation and taste.",
            "A delightful gastronomic adventure!",
            "Charming ambiance and delicious food.",
            "Immersive dining experience!"
        ]

        neutral_feedback = [
            "The food was okay, nothing special.",
            "Service was decent, but the food could be better.",
            "Not bad, but not outstanding either.",
            "Average experience overall.",
            "It was fine, but nothing extraordinary.",
            "Could improve on food quality.",
            "Service needs some enhancement.",
            "Not completely satisfied with the meal.",
            "The taste was average.",
            "Room for improvement in menu variety.",
            "Adequate service and taste.",
            "Satisfactory experience.",
            "Fairly good service and food quality.",
            "Mediocre taste and ambiance.",
            "Acceptable dining experience.",
            "Not too impressed, not too disappointed.",
            "Neutral feelings about the food and service.",
            "Middle-of-the-road experience.",
            "Sufficiently pleasing meal.",
            "Decent enough for a one-time visit."
        ]

        negative_feedback = [
            "The food was terrible.",
            "Poor service and tasteless food.",
            "Unpleasant experience overall.",
            "Disappointed with the quality and service.",
            "Would not recommend this place.",
            "Absolutely unsatisfactory!",
            "Worst food I've ever tasted.",
            "Service was slow and unprofessional.",
            "The ambiance was disappointing.",
            "Not worth the price.",
            "Horrible service and taste.",
            "Extremely dissatisfied with the food quality.",
            "A regrettable dining experience.",
            "Below average taste and service.",
            "Dreadful meal and poor service.",
            "Far from expectations.",
            "Avoid this place at all costs.",
            "Unappealing taste and presentation.",
            "Highly disappointed with the meal.",
            "A dismal dining affair."
        ]
        # Generate dates from January 1, 2023, to the current date
        start_date = datetime.date(2023, 1, 1)
        end_date = datetime.date.today()
        for _ in range(num_orders):
            order_id = len(self.orders) + 1
            restaurant_id = random.choice(restaurants)['Restaurant_UID']
            customer_id = random.choice(customers)['Customer_UID']

            guest_type = random.choice(guest_types)
            num_guests = random.randint(1, 10)
            order_time = datetime.time(
                random.randint(8, 23), random.randint(0, 59))
            order_date = fake.date_between_dates(date_start=start_date, date_end=end_date)
            order_modifier = random.choice(order_modifiers)
            order_quantity = random.randint(1, 5)
            total_num_orders = random.randint(1, 10)
            serve_start_time = (datetime.datetime.combine(
                datetime.date.today(), order_time) + datetime.timedelta(minutes=10)).time()
            serve_end_time = (datetime.datetime.combine(datetime.date.today(
            ), serve_start_time) + datetime.timedelta(minutes=random.randint(10, 30))).time()
            menu_item = random.choice(menu_items)
            menu_item_uid = menu_item['Menu_Item_UID']
            menu_item_name = menu_item['Menu_Item_Name']
            order_category = menu_item['Menu_Item_Category']
            menu_item_price = menu_item['Menu_Item_Price']
            item_quantity = random.randint(1, 5)
            modifier_name = random.choice(order_modifiers)
            modifier_price = round(random.uniform(1, 5), 2)
            order_type = random.choices(
                ['Delivery', 'Dine-in', 'Takeout'], weights=[1, 5, 2])[0]
            if order_type == 'Dine-in':
                customer_table_number = random.randint(1, 20)
            else:
                customer_table_number = None
            order_status = 'Pending'
            reservation_status = None
            reservation_date = None
            reservation_time = None
            reservation_special_request = None

            if order_type == 'Delivery':
                order_status = random.choice(
                    ['Pending', 'Delivered', 'Return'])
            elif order_type == 'Dine-in':
                order_status = random.choice(['Pending', 'Served'])
                # Add reservation status for dine-in orders
                if random.random() < 0.8:
                    reservation_status = 'Confirmed'
                    reservation_date = order_date
                    reservation_time = order_time
                    reservation_special_request = random.choice([
                        'Window seat for 4',
                        'Quiet area for 6',
                        'Specific table for 2',
                        'Table near the fireplace for 3',
                        'Outdoor seating for 5',
                        'Private room for 8',
                        'Live music area for 10',
                        'Bar seating for 2',
                        'Corner booth for 4',
                        'Near the garden for 6',
                        'Sofa seating for 3',
                        'Table with a view for 2',
                        'High-top table for 5',
                        'Candlelit table for 2',
                        'VIP section for 8',
                        'Poolside seating for 4',
                        'Booth seating for 6',
                        'Terrace seating for 4',
                        'Banquette seating for 3',
                        'Alcove seating for 2',
                        'Library area for 8',
                        'Counter seating for 4',
                        'Round table for 6',
                        'Central seating for 5',
                        'Chef’s table for 4',
                        'Elevated seating for 3',
                        'Near the stage for 6',
                        'Tasting room for 8',
                        'Zen garden for 4'])
                    reservation_special_requests = reservation_special_request
                else:
                    reservation_status = 'Walk-in'
            elif order_type == 'Takeout':
                order_status = random.choice(['Pending', 'Packed'])
            else:
                order_status = 'Pending'
            feedback_id = random.randint(1, 100)
            feedback_choice = random.choice(
                ["positive", "neutral", "negative"])
            if feedback_choice == "positive":
                feedback_text = random.choice(positive_feedback)
                # Assign a higher rating for positive feedback
                food_rating = random.randint(4, 5)
            elif feedback_choice == "neutral":
                feedback_text = random.choice(neutral_feedback)
                # Assign a moderate rating for neutral feedback
                food_rating = random.randint(2, 3)
            else:
                feedback_text = random.choice(negative_feedback)
                food_rating = random.randint(1, 2)
            feedback_time = (datetime.datetime.combine(
                datetime.date.today(), serve_end_time) + datetime.timedelta(minutes=35)).time()
            customer_entry_time = (datetime.datetime.combine(
                datetime.date.today(), order_time) - datetime.timedelta(minutes=30)).time()
            customer_exit_time = (datetime.datetime.combine(
                datetime.date.today(), feedback_time) + datetime.timedelta(minutes=5)).time()
            order_amount = menu_item_price + modifier_price
            payment_date = order_date
            payment_time = feedback_time
            promotion_type = fake.random_element(
                elements=('Percentage Discount', 'Special Offer', 'Coupon'))  # Example values
            tips = round(order_amount * 0.1, 2)
            tax = round(order_amount * 0.055, 2)  # Assuming a 10% tax rate
            total_amount = order_amount + tax + tips
            if promotion_type == 'Percentage Discount':
                discount = round(total_amount * 0.05, 2)
            elif promotion_type == 'Special Offer':
                discount = round(total_amount * 0.08, 2)
            elif promotion_type == 'Coupon':
                discount = round(total_amount * 0.07, 2)
            else:
                discount = 0
            amount_paid = total_amount - discount
            payment_method = fake.random_element(
                elements=('Cash', 'Credit Card', 'Debit Card', 'Online Payment'))
            bill_id = fake.uuid4()
            bill_date = order_date
            payment_status = 'Paid'
            loyalty_points_earned = round(
                total_amount * 0.05)
            order_data = {
                'Order_ID': order_id,
                'Restaurant_UID': restaurant_id,
                'Customer_UID': customer_id,
                'Customer_Table_Number': customer_table_number,
                'Guest_Type': guest_type,
                'No_of_Guest': num_guests,
                'Order_Type': order_type,
                'Order_Time': order_time,
                'Order_Date': order_date,
                'Order_Modifier': order_modifier,
                'Order_Category': order_category,
                'Order_Quantity': order_quantity,
                'Total_No_Order': total_num_orders,
                'Serve_Start_Time': serve_start_time,
                'Serve_End_Time': serve_end_time,
                'Menu_item_UID': menu_item_uid,
                'Menu_item_Name': menu_item_name,
                'Menu_Item_Price': menu_item_price,
                'Item_Quantity': item_quantity,
                'Modifier_Name': modifier_name,
                'Modifer_Price': modifier_price,
                'Order_Status': order_status,
                'Reservation_Date': reservation_date,
                'Reservation_Time': reservation_time,
                'Reservation_Special_Requests': reservation_special_request,
                'Reservation_Status': reservation_status if order_type == 'Dine-in' else None,
                'Feedback_ID': feedback_id,
                'Feedback_Text': feedback_text,
                'Food_Rating': food_rating,
                'Feedback_Date': order_date,
                'Feedback_Time': feedback_time,
                'Customer_Entry_Time': customer_entry_time,
                'Customer_Exist_Time': customer_exit_time,
                'Payment_Date': payment_date,
                'Payment_time': payment_time,
                'Promotion_Type': promotion_type,
                'Tips': tips,
                'Tax': tax,
                'Total_Amount': total_amount,
                'Discount': discount,
                'Amount_Paid': amount_paid,
                'Payment_Method': payment_method,
                'Bill_ID': bill_id,
                'Bill_Date': bill_date,
                'Payment_status': payment_status,
                'LoyaltyPoints_Earned': loyalty_points_earned,
            }
            self.orders.append(order_data)

    def get_data(self):
        return self.orders


class Return:
    def __init__(self):
        self.returns = []
        self.starting_return_id = 42
        self.starting_refund_id = 42
    def generate_returns(self, orders):
        return_id = self.starting_return_id
        refund_id = self.starting_refund_id

        for order in orders:
            return_date = None
            return_time = None
            refund_date = None
            refund_time = None

            if order['Order_Status'] == 'Return':
                return_date = order['Payment_Date']
                return_time = (datetime.datetime.combine(datetime.date.today(
                ), order['Payment_time']) + datetime.timedelta(minutes=20)).time()
                refund_date = order['Payment_Date']
                refund_time = (datetime.datetime.combine(datetime.date.today(
                ), order['Payment_time']) + datetime.timedelta(minutes=40)).time()

                return_data = {
                    'Return_ID': return_id,
                    'Return_Date': return_date,
                    'Return_Time': return_time,
                    'Refund_ID': refund_id,
                    'Order_ID': order['Order_ID'],
                    'Customer_UID': order['Customer_UID'],
                    'Menu_item_UID': order['Menu_item_UID'],
                    'Menu_item_Name': order['Menu_item_Name'],
                    'Refund_Amount': order['Amount_Paid'],
                    'Refund_Date': refund_date,
                    'Refund_time': refund_time
                }
                self.returns.append(return_data)
                return_id += 1
                refund_id += 1

    def get_data(self):
        return self.returns


class Finance:
    def __init__(self):
        self.financial_data = []
        self.budget_id_counter = 1

    def generate_financial_data(self, restaurants, orders):
        for restaurant in restaurants:
            restaurant_id = restaurant['Restaurant_UID']

            # Extracting Year from Order Table
            order_years = set(
                order['Order_Date'].year for order in orders if order['Restaurant_UID'] == restaurant_id)

            # Calculating Quarterly Revenue
            quarterly_revenues = {'Q1': 0, 'Q2': 0, 'Q3': 0, 'Q4': 0}
            for order in orders:
                if order['Order_Status'] != 'Return' and order['Restaurant_UID'] == restaurant_id:
                    order_month = order['Order_Date'].month
                    order_year = order['Order_Date'].year
                    if order_month in [1, 2, 3] and order_year in order_years:
                        quarterly_revenues['Q1'] += order['Amount_Paid']
                    elif order_month in [4, 5, 6] and order_year in order_years:
                        quarterly_revenues['Q2'] += order['Amount_Paid']
                    elif order_month in [7, 8, 9] and order_year in order_years:
                        quarterly_revenues['Q3'] += order['Amount_Paid']
                    elif order_month in [10, 11, 12] and order_year in order_years:
                        quarterly_revenues['Q4'] += order['Amount_Paid']

            for quarter, revenue in quarterly_revenues.items():
                if revenue > 0:
                    budget_id = f"A{self.budget_id_counter:02}"
                    self.budget_id_counter += 1

                    budget_year = order_years.pop() if order_years else fake.random_element(
                        elements=[2024, 2025])
                    budget_amount = revenue
                    total_revenue = sum(order['Amount_Paid'] for order in orders if order['Order_Status']
                                        != 'Return' and order['Restaurant_UID'] == restaurant_id)
                    tax_amount = round(total_revenue * 0.1, 2)
                    total_sales = sum(
                        1 for order in orders if order['Order_Status'] != 'Return' and order['Restaurant_UID'] == restaurant_id)
                    targeted_sales_amount = round(budget_amount * 0.8, 2)

                    finance_data = {
                        'Budget_ID': budget_id,
                        'Restaurant_UID': restaurant_id,
                        'Budget_Month': quarter,
                        'Budget_Year': budget_year,
                        'Budget_Amount': budget_amount,
                        'Total_Revenue': total_revenue,
                        'Tax_Amount': tax_amount,
                        'Total_Sales': total_sales,
                        'Targeted_Sales_Amount': targeted_sales_amount,
                    }
                    self.financial_data.append(finance_data)

    def get_data(self):
        return self.financial_data


class Marketing:
    def __init__(self):
        self.marketing_data = []
        self.marketing_id_counter = 1

    def generate_marketing_data(self, restaurants):
        # List of dummy campaign names
        campaign_names = [
            "Spring_Fling", "Summer_Splash", "Autumn_Fiesta", "Winter_Wonder",
            "Tasty_Trends", "Foodie_Fiesta", "Flavor_Feast", "Yummy_Yearnings",
            "Sizzling_Specials", "Fresh_Flavors", "Delicious_Discoveries", "Menu_Magic",
            "Savory_Seasons", "Culinary_Craze", "Epicurean_Escape", "Gourmet_Gala",
            "Mouthwatering_Moments", "Tempting_Tastes", "Palate_Pleasers", "Gastronomic_Galore",
            "Feast_Frenzy", "Flavorful_Fiesta", "Eating_Extravaganza", "Dish_Delight",
            "Food_Flair", "Cuisine_Craze", "Appetite_Adventure", "Taste_Treasure",
            "Bite_Bliss", "Yum_Yardstick", "Crave_Carnival", "Food_Fest", "Dine_Delight"
            # Add more dummy campaign names as needed
        ]

        # Dict to store used campaigns for each restaurant
        used_campaigns = {}

        for restaurant in restaurants:
            restaurant_id = restaurant['Restaurant_UID']
            used_campaigns[restaurant_id] = set()

            # Generate at least 15 campaigns for each restaurant
            num_campaigns = random.randint(15, 20)
            for i in range(num_campaigns):
                # Randomly choose a campaign name from the list
                campaign_name = random.choice(campaign_names)

                # Ensure uniqueness for each restaurant
                while campaign_name in used_campaigns[restaurant_id]:
                    campaign_name = random.choice(campaign_names)

                used_campaigns[restaurant_id].add(campaign_name)

                marketing_budget = round(random.uniform(5000, 20000), 2)  # Keep budget high
                marketing_cost = round(random.uniform(500, 2000), 2)  # Keep cost low
                total_campaign_reach = random.randint(1000, 10000)
                total_click = random.randint(100, 1000)
                total_open = random.randint(500, 5000)
                platform = random.choice(['Email', 'Instagram', 'Facebook', 'Twitter', 'Youtube'])  # Added Youtube
                post_id = ''
                total_like = ''
                total_comments = ''
                total_views = ''
                content_type = ''

                # For Email platform, leave certain fields empty
                if platform == 'Email':
                    post_id = ''
                    total_like = ''
                    total_comments = ''
                    total_views = ''
                    content_type = 'Email'
                elif platform == 'Youtube':  # If the platform is Youtube, set content type to video
                    content_type = 'Video'
                    post_id = fake.uuid4()
                    total_like = random.randint(50, 500)
                    total_comments = random.randint(5, 50)
                    total_views = random.randint(1000, 10000)
                else:
                    post_id = fake.uuid4()
                    total_like = random.randint(50, 500)
                    total_comments = random.randint(5, 50)
                    total_views = random.randint(1000, 10000)
                    # Set content type based on the type of content for other platforms (Instagram, Facebook, Twitter)
                    content_type = random.choice(['Video', 'Text', 'Image'])

                # Adjust Total_Customer_Acquired and Follower_Growth
                total_customer_acquired = random.randint(0, 500)
                follower_growth = random.randint(0, 700)

                if i < 2:
                    total_customer_acquired = 0
                    follower_growth = random.randint(-50, 0)

                # If count is less than 2, keep budget low and marketing cost high
                if num_campaigns < 2:
                    marketing_budget = round(random.uniform(1000, 5000), 2)
                    marketing_cost = round(random.uniform(2000, 10000), 2)

                # Adjust other metrics if Follower_Growth and Total_Customer_Acquired are low or negative
                if follower_growth <= 0 or total_customer_acquired <= 0:
                    total_views = random.randint(10, 100)
                    total_comments = random.randint(1, 10)
                    total_share = random.randint(1, 10)
                    total_like = random.randint(1, 10)
                    total_open = random.randint(10, 100)
                    total_click = random.randint(10, 100)
                    total_campaign_reach = random.randint(50, 150)

                # Generate a random hashtag
                hashtag = '#'+fake.word()

                campaign_start_date = fake.date_between(start_date='-1y', end_date='today')
                campaign_end_date = fake.date_between(start_date=campaign_start_date, end_date='today')
                marketing_data = {
                    'Restaurant_UID': restaurant_id,
                    'Marketing_ID': f"M{self.marketing_id_counter:02}",
                    'Campaign_Name': campaign_name,
                    'Campaign_Start_Date': campaign_start_date,
                    'Campaign_End_Date': campaign_end_date,
                    'Campaign_Budget': marketing_budget,
                    'Total_Campaign_Reach': total_campaign_reach,
                    'Total_Click': total_click,
                    'Total_Open': total_open,
                    'Platform': platform,
                    'Post_ID': post_id,
                    'Post_Date': fake.date_between(start_date='-1y', end_date='today'),
                    'Post_Time': fake.time(),
                    'Total_Like': total_like,
                    'Total_Share': random.randint(10, 100),
                    'Total_Comments': total_comments,
                    'Total_Views': total_views,
                    'Follower_Growth': follower_growth,
                    'Marketing_Cost': marketing_cost,
                    'Total_Customer_Acquired': total_customer_acquired,
                    'Content_Type': content_type,
                    'Hashtag': hashtag,
                }
                self.marketing_data.append(marketing_data)
                self.marketing_id_counter += 1

    def get_data(self):
        return self.marketing_data


class Expense:
    def __init__(self):
        self.expense_data = []
        self.expense_id_counter = 1

    def generate_expense_data(self, restaurants, staff_data):
        expense_categories = ['Food', 'Utilities', 'Marketing',
                              'Maintenance', 'Salaries', 'Rent', 'Taxes', 'Insurance']

        for restaurant in restaurants:
            restaurant_id = restaurant['Restaurant_UID']

            # Generate expenses for each expense category
            for category in expense_categories:
                expense_budget = round(random.uniform(100, 5000), 2)
                expense_category = category

                # For salaries, sum up staff salaries from Staff table
                if category == 'Salaries':
                    staff_salaries = sum(
                        [staff['Staff_Salary'] for staff in staff_data if staff['Restaurant_UID'] == restaurant_id])
                    expense_budget = staff_salaries

                # Set fixed dates for expenses (1st day of each month)
                start_date = '2024-01-01'  # Start date: 1st Jan 2024
                end_date = '2024-12-01'  # End date: 1st Dec 2024

                # Generating expense data for the 1st day of each month
                current_date = start_date
                while current_date <= end_date:
                    expense_data = {
                        'Expense_ID': f"E{self.expense_id_counter:02}",
                        'Restaurant_UID': restaurant_id,
                        'Expense_Budget': expense_budget,
                        'Expense_Date': current_date,
                        'Expense_Time': fake.time(),
                        'Expense_Category': expense_category,
                        # Distribute equally for each month
                        'Total_Amount': round(expense_budget / 12, 2)
                    }
                    self.expense_data.append(expense_data)
                    self.expense_id_counter += 1

                    # Move to the next month
                    current_date = (datetime.datetime.strptime(
                        current_date, "%Y-%m-%d") + relativedelta(months=1)).strftime("%Y-%m-%d")

    def get_data(self):
        return self.expense_data


def write_to_csv(data, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)


#! Usage example:
restaurant = Restaurant()
restaurant.generate_restaurants(5)  # Generate 5 restaurants
restaurant_data = restaurant.get_data()['restaurants']

# * Write Restaurant data to CSV
write_to_csv(restaurant_data, '1. Restaurants.csv')


#! Usage example:
customer = Customer()
customer_data = list(customer.generate_customers(200, restaurant_data))

# * Write Customer data to CSV
write_to_csv(customer_data, '2. Customers.csv')


#! Usage example:
menu = Menu()
menu.generate_menu_items()

# * Write Menu data to CSV
fine_dining_menu_data = menu.get_data()['menu_items']
write_to_csv(fine_dining_menu_data, '3. Menu.csv')

#! Usage example:
drinks_menu = Drinks()
drinks_menu.generate_drink_items()
drinks_data = drinks_menu.get_data()['drink_items']
write_to_csv(drinks_data, '4. Drinks.csv')

#! Usage example:
kitchen = Kitchen()
kitchen.generate_inventory(100)
inventory_data = kitchen.get_data()

# * Write Inventory data to CSV
write_to_csv(inventory_data, '5. Kitchen.csv')


#! Usage example:
staff_table = Staff()
staff_table.generate_staff_data(50, restaurant_data)
staff_data = staff_table.get_data()

# * Write Staff data to CSV
write_to_csv(staff_data, '6. Staff.csv')


#! Usage example:
order_table = Order()
order_table.generate_orders(
    1000, restaurant_data, customer_data, fine_dining_menu_data)
order_data = order_table.get_data()

# * Write Order data to CSV
write_to_csv(order_data, '7. Orders.csv')


#! Usage example:
return_table = Return()
return_table.generate_returns(order_data)
return_data = return_table.get_data()

# * Write Return data to CSV
write_to_csv(return_data, '8. Return.csv')

#! Generate Financial Data
finance = Finance()
finance.generate_financial_data(restaurant_data, order_data)
finance_data = finance.get_data()
# * Write Finance data to CSV
write_to_csv(finance_data, '9. Finance.csv')


# Generate Marketing Data
marketing = Marketing()
marketing.generate_marketing_data(restaurant_data)
marketing_data = marketing.get_data()
# Write Marketing data to CSV
write_to_csv(marketing_data, '10. Marketing.csv')

# Generate Expense Data
expense = Expense()
expense.generate_expense_data(restaurant_data, staff_data)
data = expense.get_data()
write_to_csv(data, '11. Expense.csv')
