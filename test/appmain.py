import os  
from flask import Flask,render_template, request, jsonify, redirect, url_for, session ,send_from_directory
import mysql.connector
from mysql.connector import pooling

#####the main app.py before closing the connections 

app = Flask(__name__)  
app.secret_key = 'your_secret_key'  

UPLOAD_FOLDER = os.path.join(os.path.expanduser("~"), "Desktop", "AssessmentPictures")
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

UPLOAD_IMG = os.path.join(os.path.expanduser("~"), "Desktop", "RemedyPictures")
app.config["UPLOAD_IMG"] = UPLOAD_IMG

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

if not os.path.exists(UPLOAD_IMG):
    os.makedirs(UPLOAD_IMG)

# Connect to MySQL
#def get_db_connection():
#    return mysql.connector.connect(
#        host="localhost",  # Connecting to localhost
#        user="root",
#        password="nare@2058",
#        database="remedydb",
#        autocommit=True,  # Prevents timeout issues
#        connection_timeout=300000  # Keeps connection alive
# )

db_pool = pooling.MySQLConnectionPool(
    pool_name="mypool",
    pool_size=30,  # Adjust based on workload
    host="localhost",  # Or server IP if hosted remotely
    user="root",
    password="nare@2058",
    database="remedydb",
    autocommit=True,  # Prevents timeout issues
    connection_timeout=60  # 60 seconds is ideal
)

def get_db_connection():
    return db_pool.get_connection()

@app.route('/service-worker.js')
def serve_worker():
    return send_from_directory('static/js', 'service-worker.js')
    
# Route to render the login.html page
@app.route('/')
def index():
    return render_template('login.html')

@app.route('/A001hotspot')
def A001hotspot():
    return render_template('A001hotspot.html')

@app.route('/A002hotspot')
def A002hotspot():
    return render_template('A002hotspot.html')

@app.route('/A003hotspot')
def A003hotspot():
    return render_template('A003hotspot.html')

@app.route('/A004hotspot')
def A004hotspot():
    return render_template('A004hotspot.html')

@app.route('/A005hotspot')
def A005hotspot():
    return render_template('A005hotspot.html')

@app.route('/A001remedyhotspot')
def A001_remedy_hotspot():
    return render_template('A001remedyhotspot.html')

@app.route('/A002remedyhotspot')
def A002_remedy_hotspot():
    return render_template('A002remedyhotspot.html')

@app.route('/A003remedyhotspot')
def A003_remedy_hotspot():
    return render_template('A003remedyhotspot.html')

@app.route('/A004remedyhotspot')
def A004_remedy_hotspot():
    return render_template('A004remedyhotspot.html')

@app.route('/A005remedyhotspot')
def A005_remedy_hotspot():
    return render_template('A005remedyhotspot.html')


# Route for the home page
@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if 'email' not in session:
        return redirect('/login')  # Redirect to login if not authenticated

    user_type = session.get('user_type', 'Normal User')
    username = session.get('username')  # Get the username from the session
    return render_template('dashboard.html', user_type=user_type, username=username)

@app.context_processor
def inject_user():
    full_name = session.get('username', '')  
    first_name = full_name.split()[0] if full_name else '' 
    return {
        'username': first_name,  
        'user_type': session.get('user_type', 'Normal User')
    }

# for create route 
@app.route('/site')
def site():
    return render_template('site.html')

# route to select the pile from the image map
@app.route('/image-map')
def image_map():
    return render_template('area1hotspot.html')

@app.route('/customer')
def customer():
    return render_template('customer.html')

@app.route('/userform')
def userform():
    return render_template('userform.html')

@app.route('/area')
def area():
    return render_template('area.html')

@app.route('/rows')
def rows():
    return render_template('rows.html')

@app.route('/tables')
def tables():
    return render_template('tables.html')

@app.route('/piles')
def piles():
    return render_template('pile.html')

@app.route('/assessment')
def assessment():
    return render_template('assessment.html')

@app.route('/remedy')
def remedy():
    return render_template('remedy.html')

@app.route('/inventory')
def inventory():
    return render_template('inventory.html')

@app.route('/invtrans')
def invtrans():
    return render_template('invtrans.html')

#@app.route('/quality')
#def quality():
    #return render_template('quality.html')

@app.route('/reports')
def reports():
    return render_template('assreports.html')

@app.route('/remedyreports')
def remedyreports():
    return render_template('remedyreports.html')

@app.route('/profile', methods=['GET'])
def profile():
    if 'email' not in session:  
        return redirect('/login')  

    email = session['email']  # Retrieve the email from the session
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

   
    cursor.execute("SELECT * FROM users WHERE `Email` = %s", (email,))
    user = cursor.fetchone()

    if not user:  # Handle the case where no user is found
        return redirect('/login')  # Redirect to login if the user is not found

    # Pass the user data to the profile template
    return render_template('profile.html', user=user)


@app.route('/user_log')
def user_log():
    return render_template('user_log.html')

@app.route('/comments')
def comments():
    return render_template('comments.html')

@app.route('/area1remedyhotspot')
def area12hotspot():
    return render_template('area1remedyhotspot.html')

################################################################

#for update route

@app.route('/updateusers')
def update_users():
   
    return render_template('updateusers.html')

@app.route('/updatesite')
def update_site():
    
    return render_template('updatesite.html')

@app.route('/updatecustomer')
def update_customer():
   
    return render_template('updatecustomer.html')

@app.route('/updateinventory')
def update_inventory():
    
    return render_template('updateinventory.html')

@app.route('/updateinvtrans')
def update_invtrans():
   
    return render_template('updateinvtrans.html')

@app.route('/updatearea')
def update_area():
    return render_template('updatearea.html')

@app.route('/updatetable')
def update_table():
    return render_template('updatetable.html')

@app.route('/updatepile')
def update_pile():
    return render_template('updatepile.html')

@app.route('/updaterow')
def update_row():
    return render_template('updaterow.html')

@app.route('/updateassmnt')
def update_assmnt():
    return render_template('updateassmnt.html')

@app.route('/updateremedy')
def update_remedy():
    return render_template('updateremedy.html')

###########################################################

# Route for user login verification
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users WHERE email = %s AND password = %s", (email, password))
    user = cursor.fetchone()

    if user:
        # Store necessary details in the session
        session['email'] = user['Email']  
        session['username'] = user['User Name']  
        session['user_type'] = user['User Type'] 
        return jsonify({"success": True, "message": "Login successful"})
    else:
        return jsonify({"success": False, "message": "Invalid credentials"})


# Route for user creation
@app.route('/create_user', methods=['POST'])
def create_user():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')

    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        query = "INSERT INTO loginusers (name, email, password) VALUES (%s, %s, %s)"
        cursor.execute(query, (name, email, password))
        connection.commit()
        return jsonify({"success": True, "message": "User created successfully"})
    except mysql.connector.Error as e:
        return jsonify({"success": False, "message": f"Error creating user: {e}"})

# Route for logging out
@app.route('/logout', methods=['POST'])
def logout():
    session.pop('username', None)  # Remove the username from the session
    return redirect(url_for('index'))

@app.route('/submit_siteform', methods=['POST'])
def submit_siteform():
    site_name = request.form.get('site_name')
    site_location = request.form.get('location')
    site_owner = request.form.get('site_owner_name')
    site_gps = request.form.get('site_gps')

    connection = get_db_connection()
    cursor = connection.cursor()

    try:
        # Fetch the current maximum Site ID
        cursor.execute("SELECT `Site ID` FROM `Site` ORDER BY `Site ID` DESC LIMIT 1")
        result = cursor.fetchone()
        if result:
           
            last_site_id = result[0]  
            next_number = int(last_site_id[1:]) + 1  
        else:
            
            next_number = 1
        new_site_id = f"S{next_number:03d}" 
        query = """
        INSERT INTO `Site` (`Site ID`, `Cust ID`, `Site Name`, `Site Location`, `Site Owner Name`, `Site GPS`)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (new_site_id, "", site_name, site_location, site_owner, site_gps))
        connection.commit()

        return jsonify({"success": True, "message": f"Site information saved successfully "})
    except mysql.connector.Error as e:
        return jsonify({"success": False, "message": f"Error saving site information: {e}"})
    finally:
        cursor.close()
        connection.close()

@app.route('/submit_customerform', methods=['POST'])
def submit_customerform():
    # Getting data from the form
    name = request.form.get('name')
    address = request.form.get('address')
    contact_person = request.form.get('contact_person')
    website = request.form.get('website')
    phone_no = request.form.get('phone_no')
    country = request.form.get('country')

    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        # Fetch the current maximum Cust ID
        cursor.execute("SELECT `Cust ID` FROM `Customer` ORDER BY `Cust ID` DESC LIMIT 1")
        result = cursor.fetchone()
        if result:
           
            last_cust_id = result[0]  
            next_number = int(last_cust_id[1:]) + 1 
        else:
            
            next_number = 1
        new_cust_id = f"C{next_number:03d}"  
        query = """
        INSERT INTO Customer 
        (`Cust ID`, `Customer Name`, `Customer Address`, `Contact Person`, `Customer Website`, `Phone No`, `Country`)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (new_cust_id, name, address, contact_person, website, phone_no, country))
        connection.commit()

        return jsonify({"success": True, "message": f"Customer information saved successfully"})
    except mysql.connector.Error as e:
        return jsonify({"success": False, "message": f"Error saving customer information: {e}"})
    finally:
        cursor.close()
        connection.close()

@app.route('/submit_user_form', methods=['POST'])
def submit_userform():
    # Retrieve form data
    user_name = request.form.get('user_name')
    user_type = request.form.get('user_type')
    designation = request.form.get('designation')
    phone_no = request.form.get('phone_no')
    reports_to = request.form.get('reports_to')
    date_created = request.form.get('date_created')
    site_id = request.form.get('site_id')  
    email = request.form.get('gmail_address') 
    password = request.form.get('create_password')
    confirm_password = request.form.get('confirm_password') 

    if password != confirm_password:
        return jsonify({"success": False, "message": "Passwords do not match!"})

    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        # Check if the Site ID exists
        cursor.execute("SELECT  `Site ID` FROM `site` WHERE `Site ID` = %s", (site_id,))
        if not cursor.fetchone():
            return jsonify({"success": False, "message": "Invalid Site ID selected."})

        cursor.execute("SELECT `Email` FROM `users` WHERE `Email` = %s", (email,))
        if cursor.fetchone():
            return jsonify({"success": False, "message": "Email already exists. Please use a different email."})

        cursor.execute("SELECT `User ID` FROM `users` ORDER BY `User ID` DESC LIMIT 1")
        result = cursor.fetchone()
        if result and result[0]:
            last_user_id = result[0]
            next_number = int(last_user_id[1:]) + 1
        else:
            next_number = 1

        new_user_id = f"U{next_number:03d}" 

        query = """
        INSERT INTO `users` (`User ID`, `Site ID`, `User Name`, `User Type`, `User Designation`, `User Phone number`, `Reports To`, `Date Created`, `Date Removed`, `Email`, `Password`)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (new_user_id, site_id, user_name, user_type, designation, phone_no, reports_to, date_created, None, email, password))
        connection.commit()

        return jsonify({"success": True, "message": f"User information saved successfully "})
    except mysql.connector.Error as e:
        return jsonify({"success": False, "message": f"Error saving user information: {e}"})
    finally:
        cursor.close()
        connection.close()

@app.route('/submit_area_form', methods=['POST'])
def submit_area_form():
    # Retrieve form data
    location = request.form.get('location')
    gps = request.form.get('gps')
    if not location or not gps:
        return jsonify({"success": False, "message": "All fields are required."})

    connection = get_db_connection()
    cursor = connection.cursor()

    try:
        # Fetch the current maximum Area ID
        cursor.execute("SELECT `Area ID` FROM `areas` ORDER BY `Area ID` DESC LIMIT 1")
        result = cursor.fetchone()
        
        # Determine the next Area ID
        if result and result[0]:
            last_area_id = result[0]
            next_number = int(last_area_id[1:]) + 1
        else:
            next_number = 1
        new_area_id = f"A{next_number:03d}"
        query = """
        INSERT INTO `areas` (`Area ID`, `Location`, `GPS`)
        VALUES (%s, %s, %s)
        """
        cursor.execute(query, (new_area_id, location, gps)) 
        connection.commit()

        return jsonify({"success": True, "message": f"Area information saved successfully "})
    except mysql.connector.Error as e:
        return jsonify({"success": False, "message": f"Error saving area information: {e}"})
    finally:
        cursor.close()
        connection.close()

@app.route('/submit_user_log_form', methods=['POST'])
def submit_user_log_form():
    # Retrieve form data
    user_id = request.form.get('user_id')
    date_logged_in = request.form.get('date_logged_in')
    date_logged_out = request.form.get('date_logged_out')
    if not user_id or not date_logged_in:
        return jsonify({"success": False, "message": "User ID and Date Logged In are required."})

    connection = get_db_connection()
    cursor = connection.cursor()

    try:
        # Insert data into the users_log table
        query = """
        INSERT INTO `user_log` (`User ID`, `Date Logged in`, `Date Logged out`)
        VALUES (%s, %s, %s)
        """
        cursor.execute(query, (user_id, date_logged_in, date_logged_out))
        connection.commit()
        return jsonify({"success": True, "message": "User log information saved successfully"})
    except mysql.connector.Error as e:
        return jsonify({"success": False, "message": f"Error saving user log information: {e}"})
    finally:
        cursor.close()
        connection.close()

@app.route('/submit_comment_form', methods=['POST'])
def submit_comment_form():
    comment_type = request.form.get('comment_type')
    related_comment_id = request.form.get('related_comment_id')
    pile_id = request.form.get('pile_id')
    user_id = request.form.get('user_id')
    usage_id = request.form.get('usage_id')
    date_posted = request.form.get('date_posted')
    comment_text = request.form.get('comment_text')
    comment_date = request.form.get('comment_date')
    commented_by = request.form.get('commented_by')
    status = request.form.get('status')

    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        # Insert the data into the Comment table
        query = """
        INSERT INTO `Comments` (`Comment Type`, `Related Comment ID`, `Pile ID`, `User ID`, `Usage ID`, 
                               `Date Posted`, `Comment Text`, `Comment Date`, `Commented By`, `Status`)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (comment_type, related_comment_id, pile_id, user_id, usage_id,
                               date_posted, comment_text, comment_date, commented_by, status))
        connection.commit()
        return jsonify({"success": True, "message": "Comment information saved successfully"})
    except mysql.connector.Error as e:
        return jsonify({"success": False, "message": f"Error saving comment information: {e}"})
    finally:
        cursor.close()
        connection.close()

#connection for assessment
@app.route('/submit_task_assignment', methods=['POST'])
def submit_task_assignment():
    area_id=request.form.get('area_id')
    user_id = request.form.get('user_id')
    table_id = request.form.get('selectedHotspots')  # Comma-separated Table IDs
    task_date = request.form.get('task_date')
    allotted_date = request.form.get('allotted_date')
    allotted_by = request.form.get('allotted_by')
    date_completed = request.form.get('date_completed')

    if not table_id:
        return jsonify({"success": False, "message": "No tables selected!"}), 400

    connection = get_db_connection()
    cursor = connection.cursor()

    try:
        # Split table_id into a list and ensure all are valid (no empty strings)
        table_id_list = [table.strip() for table in table_id.split(",") if table.strip()]

        for table in table_id_list:
            for pile_no in range(1, 5):  # Create 4 rows per Table ID with Pile No 1-4
                # Generate a new unique Assessment ID
                cursor.execute("SELECT `Assessment ID` FROM `assessment` ORDER BY `Assessment ID` DESC LIMIT 1")
                result = cursor.fetchone()
                next_number = int(result[0][2:]) + 1 if result else 1
                new_assessment_id = f"AS{next_number:05d}"

                # Insert each row with increasing Pile No
                query = """
                INSERT INTO `assessment` (`Assessment ID`,`Area ID`, `User ID`, `Table ID`, `Pile No`, `Task Date`, `Allotted Date`, `Allotted By`, `Date Completed`)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                """
                cursor.execute(query, (new_assessment_id, area_id, user_id, table, pile_no, task_date, allotted_date, allotted_by, date_completed))

        connection.commit()  # Commit after all inserts

        return jsonify({"success": True, "message": "Task assignment saved successfully"})

    except mysql.connector.Error as e:
        return jsonify({"success": False, "message": f"Error saving task assignment: {e}"}), 500
    finally:
        cursor.close()
        connection.close()



@app.route('/submit_remedy_form', methods=['POST'])
def submit_remedy_form():
    # Get form data
    area_id=request.form.get('area_id')
    user_id = request.form.get('user_id')
    table_ids = request.form.get('selectedHotspots')  # Comma-separated Table IDs
    task_date = request.form.get('task_date')
    assessed_case = request.form.get('assessed_case')
    allotted_date = request.form.get('allotted_date')
    allotted_by = request.form.get('allotted_by')
    date_completed = request.form.get('date_completed')
    remedy_status = request.form.get('remedy_status') or None
    remedy_text = request.form.get('remedy_text')

    if not table_ids:
        return jsonify({"success": False, "message": "No tables selected!"}), 400

    connection = get_db_connection()
    cursor = connection.cursor()

    try:
        table_id_list = [table.strip() for table in table_ids.split(",") if table.strip()]

        for table_id in table_id_list:
            for pile_no in range(1, 5):  # Create 4 rows per Table ID with Pile No 1-4
                # Fetch the latest Remedy ID
                cursor.execute("SELECT `Remedy ID` FROM `Remedy` ORDER BY `Remedy ID` DESC LIMIT 1")
                result = cursor.fetchone()

                next_number = int(result[0][2:]) + 1 if result else 1
                new_remedy_id = f"RM{next_number:05d}"

                # Insert each row with increasing Pile No
                query = """
                INSERT INTO `Remedy` (`Remedy ID`, `Area ID`,`User ID`, `Table ID`, `Pile No`, `Task Date`, `Assessed Case`, 
                                      `Allotted Date`, `Allotted By`, `Date Completed`, `Remedy Status`, `Remedy Text`)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s)
                """
                cursor.execute(query, (new_remedy_id, area_id, user_id, table_id, pile_no, task_date, assessed_case,
                                       allotted_date, allotted_by, date_completed, remedy_status, remedy_text))

        connection.commit()
        return jsonify({"success": True, "message": "Remedy form submitted successfully"})

    except mysql.connector.Error as e:
        return jsonify({"success": False, "message": f"Error saving remedy form: {e}"}), 500
    finally:
        cursor.close()
        connection.close()


@app.route('/update_assessment', methods=['POST'])
def update_assessment_pics():
    try:
        user_id = request.form.get('user_id')
        task_date = request.form.get('task_date')
        table_ids = request.form.get('table_id')
        assessment_status = request.form.get('assessment_status')
        assessment_case = request.form.get('assessment_case')

        if not table_ids or "-" not in table_ids:
            return jsonify({"success": False, "message": "Invalid Table ID format"}), 400

        table_id = table_ids.split("-")[0]
        pile_no = table_ids.split("-")[1][-1]

        if not (user_id and task_date and table_id):
            return jsonify({"success": False, "message": "Missing required fields"}), 400

        # 🔹 Database connection
        connection = get_db_connection()
        cursor = connection.cursor(buffered=True)

        # 🔹 Fetch the Assessment ID
        cursor.execute("""
            SELECT `Assessment ID`, `Pile No` FROM assessment 
            WHERE `User ID` = %s AND `Task Date` = %s AND `Table ID` = %s AND `Pile No` = %s
        """, (user_id, task_date, table_id, pile_no))

        result = cursor.fetchone()
        cursor.close()

        if not result:
            connection.close()
            return jsonify({"success": False, "message": "Assessment not found"}), 404

        assessment_id = result[0]  # Extract assessment ID

        # 🔹 Create the folder for this assessment
        assessment_folder = os.path.join(app.config["UPLOAD_FOLDER"], f"{assessment_id}")
        os.makedirs(assessment_folder, exist_ok=True)  # Ensure the folder exists

        # 🔹 Fetch Pile IDs for the given Table ID (sorted in order)
        cursor = connection.cursor(buffered=True)
        cursor.execute("""
            SELECT `Pile ID` FROM piles 
            WHERE `Table ID` = %s 
            ORDER BY `Pile No` ASC
        """, (table_id,))

        pile_ids = [row[0] for row in cursor.fetchall()]
        cursor.close()

        if len(pile_ids) < 4:
            connection.close()
            return jsonify({"success": False, "message": "Not enough Pile IDs found"}), 400

        image_paths = []
        for i in range(4):  # Loop through 4 images
            image = request.files.get(f'image{i+1}')  # Image names start from 'image1'
            if image:
                image_filename = f"{assessment_id}_{table_id}_{pile_ids[i]}.jpg"  # Use Pile ID
                image_path = os.path.join(assessment_folder, image_filename)  # Save inside the assessment folder
                image.save(image_path)
                image_paths.append(image_filename)
            else:
                image_paths.append(None)

        # 🔹 Update the assessment record with image paths
        cursor = connection.cursor()
        query = """
            UPDATE assessment 
            SET `Assessment Status` = %s, `Assessment Case` = %s, 
                `Picture1 Name` = %s, `Picture2 Name` = %s, 
                `Picture3 Name` = %s, `Picture4 Name` = %s,
                `Picture Location` = %s
            WHERE `Assessment ID` = %s
        """

        cursor.execute(query, (
            assessment_status, assessment_case,
            image_paths[0], image_paths[1], image_paths[2], image_paths[3],
            assessment_folder,  # Save the folder path
            assessment_id
        ))

        connection.commit()
        cursor.close()
        connection.close()

        return jsonify({"success": True, "message": "Assessment updated successfully", "folder": assessment_folder})

    except mysql.connector.Error as e:  # ✅ Fixed the "Error" exception issue
        print(traceback.format_exc())  # Print the full error traceback
        return jsonify({"success": False, "message": f"Database error: {str(e)}"}), 500

    except Exception as e:
        print(traceback.format_exc())  # Print the full error traceback
        return jsonify({"success": False, "message": str(e)}), 500


@app.route('/update_remedy_pics', methods=['POST'])
def update_remedy_pics():
    try:
        # Get form data
        user_id = request.form.get('user_id')
        task_date = request.form.get('task_date')
        table_ids = request.form.get('table_id')
        assessed_case = request.form.get('assessed_case')  
        remedy_status = request.form.get('remedy_status')

        if not table_ids or "-" not in table_ids:
            return jsonify({"success": False, "message": "Invalid Table ID format"}), 400

        table_id = table_ids.split("-")[0]
        pile_no = table_ids.split("-")[1][-1]

        if not (user_id and task_date and table_id and pile_no):
            return jsonify({"success": False, "message": "Missing required fields"}), 400

        # Get the corresponding Remedy ID
        connection = get_db_connection()
        cursor = connection.cursor(buffered=True)

        cursor.execute("""
            SELECT `Remedy ID`, `Pile No` FROM remedy 
            WHERE `User ID` = %s AND `Task Date` = %s AND `Table ID` = %s AND `Pile No` = %s
        """, (user_id, task_date, table_id, pile_no))

        result = cursor.fetchone()
        cursor.close()

        if not result:
            connection.close()
            return jsonify({"success": False, "message": "Remedy not found"}), 404

        remedy_id = result[0]  # Extract Remedy ID

        # 🔹 Create a unique folder for the remedy
        remedy_folder = os.path.join(app.config["UPLOAD_IMG"], f"{remedy_id}")
        os.makedirs(remedy_folder, exist_ok=True)  # Ensure the folder exists

        # 🔹 Fetch Pile IDs for the given Table ID (sorted in order)
        cursor = connection.cursor(buffered=True)
        cursor.execute("""
            SELECT `Pile ID` FROM piles 
            WHERE `Table ID` = %s 
            ORDER BY `Pile No` ASC
        """, (table_id,))

        pile_ids = [row[0] for row in cursor.fetchall()]  # Extract all Pile IDs in order
        cursor.close()

        if len(pile_ids) < 4:
            connection.close()
            return jsonify({"success": False, "message": "Not enough Pile IDs found"}), 400

        image_paths = []
        for i in range(4):  # Loop through 4 images
            image = request.files.get(f'image{i+1}')
            if image:
                image_filename = f"{remedy_id}_{table_id}_{pile_ids[i]}.jpg"  # Use Pile ID
                image_path = os.path.join(remedy_folder, image_filename)  # Save inside remedy folder
                image.save(image_path)
                image_paths.append(image_filename)
            else:
                image_paths.append(None)  

        # 🔹 Store the folder path in the database
        cursor = connection.cursor()
        query = """
            UPDATE remedy 
            SET `Remedy Status` = %s, `Assessed Case` = %s,
                `Picture1 Name` = %s, `Picture2 Name` = %s, 
                `Picture3 Name` = %s, `Picture4 Name` = %s,
                `Picture Location` = %s
            WHERE `Remedy ID` = %s
        """

        cursor.execute(query, (
            remedy_status, assessed_case,  
            image_paths[0], image_paths[1], image_paths[2], image_paths[3],
            remedy_folder,  # Save the folder path
            remedy_id  
        ))

        connection.commit()
        cursor.close()
        connection.close()

        return jsonify({"success": True, "message": "Remedy updated successfully", "folder": remedy_folder})

    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500


   
@app.route('/get_submitted_hotspots', methods=['GET'])
def get_submitted_hotspots():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    try:
        cursor.execute("SELECT `Table ID` FROM `assessment`")  
        rows = cursor.fetchall()

        # Flatten and split the stored values
        submitted_hotspots = []
        for row in rows:
            if row['Table ID']:
                submitted_hotspots.extend(row['Table ID'].split(","))  # Split on commas

        return jsonify({"submitted_hotspots": submitted_hotspots})  
    finally:
        cursor.close()
        connection.close()

@app.route('/get_final_submitted_hotspots', methods=['GET'])
def get_final_submitted_hotspots():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    try:
        cursor.execute("SELECT `Table ID` FROM `assessment` WHERE `Assessment Status` = 'OE Approved'")  
        rows = cursor.fetchall()

        # Flatten and split the stored values
        final_submitted_hotspots = []
        for row in rows:
            if row['Table ID']:
                final_submitted_hotspots.extend(row['Table ID'].split(","))  # Split on commas

        return jsonify({"final_submitted_hotspots": final_submitted_hotspots})  
    finally:
        cursor.close()
        connection.close()

@app.route('/get_submitted_hotspots_remedy', methods=['GET'])
def get_submitted_hotspots_remedy():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    try:
        cursor.execute("SELECT `Table ID` FROM `remedy`")  
        rows = cursor.fetchall()

        # Flatten and split the stored values
        submitted_hotspots = []
        for row in rows:
            if row['Table ID']:
                submitted_hotspots.extend(row['Table ID'].split(","))  # Split on commas

        return jsonify({"submitted_hotspots": submitted_hotspots})  
    finally:
        cursor.close()
        connection.close()

@app.route('/submit_row_form', methods=['POST'])
def submit_row_form():
    # Retrieve form data
    row_name = request.form.get('row_name')
    area_id = request.form.get('area_id')
    location = request.form.get('location')
    gps = request.form.get('gps')

    # Validate required fields
    if not row_name or not area_id or not location or not gps:
        return jsonify({"success": False, "message": "All fields are required."})

    # Establish DB connection
    connection = get_db_connection()
    cursor = connection.cursor()

    try:
        # Fetch the current maximum Row ID
        cursor.execute("SELECT `Row ID` FROM `rows` ORDER BY `Row ID` DESC LIMIT 1")
        result = cursor.fetchone()

        # Determine the next Row ID
        if result and result[0]:
            last_row_id = result[0]
            next_number = int(last_row_id[1:]) + 1
        else:
            next_number = 1

        # Format the new Row ID as 'R001', 'R002', etc.
        new_row_id = f"R{next_number:03d}"

        # Insert data into the rows table with the generated Row ID
        query = """
        INSERT INTO `rows` (`Row ID`, `Row Name`, `Area ID`, `Location`, `GPS`)
        VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(query, (new_row_id, row_name, area_id, location, gps))
        connection.commit()

        return jsonify({"success": True, "message": f"Row information saved successfully with ID {new_row_id}"})
    except mysql.connector.Error as e:
        return jsonify({"success": False, "message": f"Error saving row information: {e}"})
    finally:
        cursor.close()
        connection.close()

@app.route('/submit_pile_form', methods=['POST'])
def submit_pile_form():
    # Get form data
    pile_ids = request.form.get('table_id')  # This contains multiple pile IDs as a string (e.g., "P1, P2, P3")
    area_id = request.form.get('area_id')
    location_description = request.form.get('location_description')
    gps_location = request.form.get('gps_location')

    # Establish DB connection
    connection = get_db_connection()
    cursor = connection.cursor()

    try:
        if not pile_ids:
            return jsonify({"success": False, "message": "No pile selected"})
        pile_list = pile_ids.split(", ")  
        for pile_id in pile_list:
            # Fetch the current maximum Pile ID modifiy the
            cursor.execute("SELECT `Pile ID` FROM `Piles` ORDER BY `Pile ID` DESC LIMIT 1")
            result = cursor.fetchone()

            # Generate the next Pile ID
            if result and result[0]:
                last_pile_id = result[0]
                next_number = int(last_pile_id[1:]) + 1  
            else:
                next_number = 1  

            new_pile_id = f"P{next_number:03d}"

            # Insert each pile as a new row
            query = """
            INSERT INTO `Piles` (`Pile ID`, `Table ID`,  `Area ID`, `Location Description`, `GPS Location`)
            VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(query, (new_pile_id, pile_id,  area_id, location_description, gps_location))

        connection.commit()

        return jsonify({"success": True, "message": "Pile information saved successfully"})

    except mysql.connector.Error as e:
        print(f"Error: {e}")
        return jsonify({"success": False, "message": f"Error saving pile information: {e}"})

    finally:
        cursor.close()
        connection.close()

@app.route('/submit_table_form', methods=['POST'])
def submit_table_form():
    # Get form data
    table_ids = request.form.get('table_id')  # This contains multiple table IDs as a string (e.g., "T1, T2, T3")
    area_id = request.form.get('area_id')
    location_description = request.form.get('location')
    gps_location = request.form.get('gps_location')

    # Establish DB connection
    connection = get_db_connection()
    cursor = connection.cursor()

    try:
        if not table_ids:
            return jsonify({"success": False, "message": "No table IDs provided"})

        # Split the comma-separated table IDs into a list
        table_list = table_ids.split(", ")  # Convert the string of table_ids to a list

        # Insert each table as a new row
        for table_id in table_list:
            # Insert into the `tables` table
            query = """
            INSERT INTO `tables` (`Table ID`, `Area ID`, `Location`, `GPS`)
            VALUES (%s, %s, %s, %s)
            """
            cursor.execute(query, (table_id, area_id, location_description, gps_location))

        connection.commit()

        return jsonify({"success": True, "message": "Table information saved successfully"})

    except mysql.connector.Error as e:
        print(f"Error: {e}")
        return jsonify({"success": False, "message": f"Error saving table information: {e}"})

    finally:
        cursor.close()
        connection.close()



@app.route('/submit_inventory_details', methods=['POST'])
def submit_inventory_details():
    # Get form data
    item_type = request.form.get('item_type')
    item_uom = request.form.get('item_uom')
    item_desc = request.form.get('item_desc')
    item_avl_qty = request.form.get('item_avl_qty')
    item_ror = request.form.get('item_ror') or None
    item_value = request.form.get('item_value') or None
    item_rate = request.form.get('item_rate') or None

    # Establish DB connection
    connection = get_db_connection()
    cursor = connection.cursor()

    try:
        # Generate the next Item ID
        cursor.execute("SELECT `Item ID` FROM `Inventory` ORDER BY `Item ID` DESC LIMIT 1")
        result = cursor.fetchone()
        
        if result and result[0]:
            last_item_id = result[0]
            next_number = int(last_item_id[1:]) + 1
        else:
            next_number = 1
        
        # Format the new Item ID as 'I001', 'I002', etc.
        new_item_id = f"I{next_number:04d}"

        # Insert data into Inventory table
        query = """
        INSERT INTO `Inventory` (`Item ID`, `Item Type`, `Item UOM`, `Item Desc`, 
                                 `Item Avl Qty`, `Item ROR`, `Item Value`, `Item Rate`)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (new_item_id, item_type, item_uom, item_desc, item_avl_qty, item_ror, item_value, item_rate))
        connection.commit()

     
        return jsonify({"success": True, "message": f"Item details saved successfully "})

    except mysql.connector.Error as e:
        print(f"Error: {e}")
        return jsonify({"success": False, "message": f"Error saving item details: {e}"})

    finally:
        cursor.close()
        connection.close()

#invtrans
@app.route('/submit_item_transaction_form', methods=['POST'])
def submit_item_transaction_form():
    # Get form data
    item_type = request.form.get('item_type')
    trans_qty = request.form.get('trans_qty')
    trans_type = request.form.get('trans_type')
    trans_date = request.form.get('trans_date')
    user_id = request.form.get('user_id')
    usage = request.form.get('usage')

    # Establish DB connection
    connection = get_db_connection()
    cursor = connection.cursor()

    try:
        # Get the last Item ID
        cursor.execute("SELECT `Item ID` FROM `Invtrans` ORDER BY `Item ID` DESC LIMIT 1")
        result = cursor.fetchone()

        if result and result[0]:  # Ensure result exists and is not None
            last_item_id = result[0]

            if last_item_id.startswith("IT"):  # Check format
                try:
                    next_number = int(last_item_id[2:]) + 1  # Extract number part safely
                except ValueError:
                    next_number = 1  # Reset if format is incorrect
            else:
                next_number = 1  # Reset if format is not as expected
        else:
            next_number = 1  # If no previous records exist, start with IT001

        # Generate new Item ID
        new_item_id = f"IT{next_number:04d}"  # Format as IT001, IT002, etc.

        # Insert data into Item Transaction table
        query = """
        INSERT INTO `invtrans` (`Item ID`, `Item Type`, `Trans Qty`, `Trans Type`, 
                                `Trans Date`, `User ID`, `Usage`)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (new_item_id, item_type, trans_qty, trans_type, trans_date, user_id, usage))
        connection.commit()

     
        return jsonify({"success": True, "message": "Item transaction details saved successfully"})

    except mysql.connector.Error as e:
        print(f"Error: {e}")
        return jsonify({"success": False, "message": f"Error saving item transaction details: {e}"})

    finally:
        cursor.close()
        connection.close()


###########################################################################

@app.route('/generate_report', methods=['GET'])
def generate_report():
    user_id = request.args.get('user_id')
    from_date = request.args.get('from_date')
    to_date = request.args.get('to_date')
    assessment_status = request.args.get('assessment_status')  # ✅ Get assessment_status

    if not from_date or not to_date:
        return jsonify({"error": "Missing required parameters"}), 400

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    # ✅ Base Query (Include All Users if "All Users" is selected)
    query = """
        SELECT u.`User Name`, a.`Table ID`, a.`Pile No`, 
               DATE_FORMAT(a.`Task Date`, '%d %b %Y') AS `Task Date`,
               a.`Assessment Status`, a.`Assessment Case`
        FROM assessment a
        JOIN users u ON a.`User ID` = u.`User ID`
        WHERE DATE(a.`Task Date`) BETWEEN %s AND %s
    """
    
    params = [from_date, to_date]

    # ✅ If a specific user is selected, filter by User ID
    if user_id and user_id != "all":
        query += " AND a.`User ID` = %s"
        params.append(user_id)

    # ✅ Add assessment_status filter if provided
    if assessment_status and assessment_status != "All Status":
        query += " AND a.`Assessment Status` = %s"
        params.append(assessment_status)

    cursor.execute(query, params)
    result = cursor.fetchall()

    cursor.close()
    connection.close()

    return jsonify(result)

@app.route('/generate_remedy_report', methods=['GET'])
def generate_remedyreport():
    user_id = request.args.get('user_id')
    from_date = request.args.get('from_date')
    to_date = request.args.get('to_date')
    remedy_status = request.args.get('remedy_status')  # ✅ Get assessment_status

    if not from_date or not to_date:
        return jsonify({"error": "Missing required parameters"}), 400

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    # ✅ Base Query (Include All Users if "All Users" is selected)
    query = """
        SELECT u.`User Name`, a.`Table ID`, a.`Pile No`, 
               DATE_FORMAT(a.`Task Date`, '%d %b %Y') AS `Task Date`,
               a.`Remedy Status`, a.`Assessed Case`
        FROM remedy a
        JOIN users u ON a.`User ID` = u.`User ID`
        WHERE DATE(a.`Task Date`) BETWEEN %s AND %s
    """
    
    params = [from_date, to_date]

    # ✅ If a specific user is selected, filter by User ID
    if user_id and user_id != "all":
        query += " AND a.`User ID` = %s"
        params.append(user_id)

    # ✅ Add assessment_status filter if provided
    if remedy_status and remedy_status != "All Status":
        query += " AND a.`Remedy Status` = %s"
        params.append(remedy_status)

    cursor.execute(query, params)
    result = cursor.fetchall()

    cursor.close()
    connection.close()

    return jsonify(result)

@app.route('/save_pdf', methods=['POST'])
def save_pdf():
    pdf_file = request.files['pdf']

    # Get Desktop Path
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

    # Create "Assessment Reports" Folder if it doesn't exist
    reports_folder = os.path.join(desktop_path, "Assessment Reports")
    if not os.path.exists(reports_folder):
        os.makedirs(reports_folder)

    # Save PDF in the Folder
    pdf_path = os.path.join(reports_folder, pdf_file.filename)
    pdf_file.save(pdf_path)

    return jsonify({"message": f"PDF saved successfully at {pdf_path}!"})

@app.route('/save_remedypdf', methods=['POST'])
def save_remedypdf():
    pdf_file = request.files['pdf']

    # Get Desktop Path
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

    # Create "Assessment Reports" Folder if it doesn't exist
    reports_folder = os.path.join(desktop_path, "Remedy Reports")
    if not os.path.exists(reports_folder):
        os.makedirs(reports_folder)

    # Save PDF in the Folder
    pdf_path = os.path.join(reports_folder, pdf_file.filename)
    pdf_file.save(pdf_path)

    return jsonify({"message": f"PDF saved successfully at {pdf_path}!"})

# select options get
@app.route('/get_user_ids', methods=['GET'])
def get_user_ids():
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT `User ID`, `User Name` FROM `users`")
        users = [{"id": row[0], "username": row[1]} for row in cursor.fetchall()]
        return jsonify({"success": True, "users": users})
    except mysql.connector.Error as e:
        return jsonify({"success": False, "message": f"Error fetching User IDs and Usernames: {e}"})
    finally:
        cursor.close()
        connection.close()

@app.route('/get_site_ids', methods=['GET'])
def get_site_ids():
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT `Site ID`, `Site Name` FROM `site`")
        sites = [{"id": row[0], "name": row[1]} for row in cursor.fetchall()]
        return jsonify({"success": True, "sites": sites})
    except mysql.connector.Error as e:
        return jsonify({"success": False, "message": f"Error fetching Site IDs and Site Names: {e}"})
    finally:
        cursor.close()
        connection.close()

@app.route('/get_area_ids', methods=['GET'])
def get_area_ids():
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        # Fetch Area IDs and Locations
        cursor.execute("SELECT `Area ID`, `Location` FROM `areas`")
        areas = [{"id": row[0], "location": row[1]} for row in cursor.fetchall()]
        return jsonify({"success": True, "areas": areas})
    except mysql.connector.Error as e:
        return jsonify({"success": False, "message": f"Error fetching Area IDs and Locations: {e}"})
    finally:
        cursor.close()
        connection.close()

@app.route("/get_row_ids", methods=["GET"])
def get_row_ids():
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        # Fetch Row IDs and Row Names from the database
        cursor.execute("SELECT `Row ID`, `Row Name` FROM `rows`")
        rows = [{"id": row[0], "name": row[1]} for row in cursor.fetchall()]
        return jsonify({"success": True, "rows": rows})
    except mysql.connector.Error as e:
        return jsonify({"success": False, "message": f"Error fetching rows: {e}"})
    finally:
        cursor.close()
        connection.close()

@app.route("/get_table_ids", methods=["GET"])
def get_table_ids():
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        # Fetch Table IDs and Locations from the database
        cursor.execute("SELECT `Table ID`, `Location` FROM `tables`")
        tables = [{"id": table[0], "location": table[1]} for table in cursor.fetchall()]
        return jsonify({"success": True, "tables": tables})
    except mysql.connector.Error as e:
        return jsonify({"success": False, "message": f"Error fetching tables: {e}"})
    finally:
        cursor.close()
        connection.close()

@app.route('/get_customer_ids', methods=['GET'])
def get_customer_ids():
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        # Fetch Customer ID and Customer Name from the database
        cursor.execute("SELECT `Cust ID`, `Customer Name` FROM `customer`")
        customers = [{"id": row[0], "name": row[1]} for row in cursor.fetchall()]
        
        # Return the list of customers as a JSON response
        return jsonify({"success": True, "customers": customers})
    except mysql.connector.Error as e:
        return jsonify({"success": False, "message": f"Error fetching Customer IDs and Names: {e}"})
    finally:
        cursor.close()
        connection.close()

@app.route('/get_item_names', methods=['GET'])
def get_item_names():
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        query = "SELECT `Item ID`, `Item Type` FROM `inventory`"
        cursor.execute(query)
        items = cursor.fetchall()

        item_list = [{"item_id": item[0], "item_name": item[1]} for item in items]

        return jsonify({"success": True, "items": item_list})
    except mysql.connector.Error as e:
        return jsonify({"success": False, "message": f"Error fetching item names: {e}"})
    finally:
        cursor.close()
        connection.close()

@app.route('/get_itemtrns_names', methods=['GET'])
def get_itemtrns_names():
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        query = "SELECT `Item ID`, `Item Type` FROM `invtrans`"
        cursor.execute(query)
        items = cursor.fetchall()

        item_list = [{"item_id": item[0], "item_name": item[1]} for item in items]

        return jsonify({"success": True, "items": item_list})
    except mysql.connector.Error as e:
        return jsonify({"success": False, "message": f"Error fetching item names: {e}"})
    finally:
        cursor.close()
        connection.close()

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '')  # Get the search query from the request
    results = []

    try:
        # Connect to the database using get_db_connection
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)

        # SQL Query to search for assessment names
        sql_query = """
        SELECT `assessment id`
        FROM assessment
        WHERE `assessment id` LIKE %s
        LIMIT 10
        """ 
        cursor.execute(sql_query, (f"%{query}%",))

        # Fetch all results
        results = cursor.fetchall()

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return jsonify({"error": str(err)}), 500
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

    return jsonify({"results": results})


@app.route('/search_by_date', methods=['GET'])
def search_by_date():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    user_id = request.args.get('user_id')
    task_date = request.args.get('date')

    if not user_id or not task_date:
        return jsonify({"error": "User ID and Date parameters are required"}), 400

    try:
        # Fetch Table ID, Assessment Status, Assessment Case, and Pile No separately
        cursor.execute("""
            SELECT `Table ID`, `Assessment Status`, `Assessment Case`, `Pile No`
            FROM assessment
            WHERE `User ID` = %s 
            AND DATE(`Task Date`) = %s  
            AND (`Assessment Status` !='OE Approved' OR `Assessment Status` IS NULL)
            ORDER BY `Table ID`, `Pile No`
        """, (user_id, task_date))

        result = cursor.fetchall()

        formatted_data = []
        for row in result:
            table_id = row["Table ID"]
            pile_no = row["Pile No"]

            formatted_data.append({
                "Assessment Case": row["Assessment Case"],
                "Assessment Status": row["Assessment Status"],
                "Pile No": pile_no,
                "Table ID": f"{table_id}-Pile{pile_no}"  # Format Table ID with Pile No
            })

        return jsonify({"data": formatted_data}) if formatted_data else jsonify({"data": []})

    except mysql.connector.Error as e:
        return jsonify({"error": f"Database error: {e}"}), 500

    finally:
        cursor.close()
        connection.close()

@app.route('/search_by_remedydate', methods=['GET'])
def search_by_remedydate():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    
    user_id = request.args.get('user_id')
    task_date = request.args.get('date')

    if not user_id or not task_date:
        return jsonify({"error": "User ID and Date parameters are required"}), 400

    try:
        # Fetch Table ID, Pile No, Remedy Status, and Assessed Case
        cursor.execute("""
            SELECT `Table ID`, `Pile No`, `Remedy Status`, `Assessed Case`
            FROM remedy
            WHERE `User ID` = %s 
            AND DATE(`Task Date`) = %s  
            AND (`Remedy Status` != 'OE Approved' OR `Remedy Status` IS NULL)
            ORDER BY `Table ID`, `Pile No`
        """, (user_id, task_date))

        result = cursor.fetchall()

        formatted_data = []
        for row in result:
            table_id = row["Table ID"]
            pile_no = row["Pile No"]

            formatted_data.append({
                "Assessed Case": row["Assessed Case"],
                "Remedy Status": row["Remedy Status"],
                "Pile No": pile_no,
                "Table ID": f"{table_id}-Pile{pile_no}"  # Format Table ID with Pile No
            })

        return jsonify({"data": formatted_data}) if formatted_data else jsonify({"data": []})

    except mysql.connector.Error as e:
        return jsonify({"error": f"Database error: {e}"}), 500

    finally:
        cursor.close()
        connection.close()


############################################################################

@app.route('/submit_updateuser_form', methods=['POST'])
def submit_updateuser_form():
    user_id = request.form.get('user_id')  
    user_email = request.form.get('user_email')  
    user_password = request.form.get('user_password')  
    phone_no = request.form.get('phone_no')  

    # Connect to the database
    connection = get_db_connection()
    cursor = connection.cursor()

    try:
        update_fields = []
        params = []

        if user_email:
            update_fields.append("`Email` = %s")
            params.append(user_email)

        if user_password:
            update_fields.append("`Password` = %s")
            params.append(user_password)

        if phone_no:
            update_fields.append("`User Phone number` = %s")
            params.append(phone_no)

        if not update_fields:
            return jsonify({"success": False, "message": "No fields to update provided."})

        params.append(user_id)
        query = f"""
            UPDATE `users`
            SET {', '.join(update_fields)}
            WHERE `User ID` = %s
        """
        cursor.execute(query, tuple(params))
        connection.commit()

        return jsonify({"success": True, "message": "User Details updated successfully."})

    except mysql.connector.Error as e:
        return jsonify({"success": False, "message": f"Error updating user: {e}"})
    finally:
        cursor.close()
        connection.close()

@app.route('/delete_user/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    connection = get_db_connection()
    cursor = connection.cursor()

    try:
        # Check if the user exists
        cursor.execute("SELECT `User ID` FROM `users` WHERE `User ID` = %s", (user_id,))
        if not cursor.fetchone():
            return jsonify({"success": False, "message": "User not found."})

        # Delete the user
        cursor.execute("DELETE FROM `users` WHERE `User ID` = %s", (user_id,))
        connection.commit()

        return jsonify({"success": True, "message": "User deleted successfully."})

    except mysql.connector.Error as e:
        return jsonify({"success": False, "message": f"Error deleting user: {e}"})
    finally:
        cursor.close()
        connection.close()

# Update site details
@app.route("/submit_site_update", methods=["POST"])
def submit_site_update():
    try:
        data = request.form
        site_id = data.get("site_id")
        site_location = data.get("location")
        site_owner_name = data.get("site_owner_name")

        if not site_id or not site_location or not site_owner_name:
            return jsonify({"success": False, "message": "All fields are required."})

        connection = get_db_connection()
        cursor = connection.cursor()

        # Enclose column names with spaces in backticks
        query = """
            UPDATE `site` 
            SET `Site Location` = %s, `Site Owner Name` = %s 
            WHERE `Site ID` = %s
        """
        cursor.execute(query, (site_location, site_owner_name, site_id))
        connection.commit()

        if cursor.rowcount > 0:
            return jsonify({"success": True, "message": "Site updated successfully."})
        else:
            return jsonify({"success": False, "message": "No changes made or site not found."})
    except Exception as e:
        return jsonify({"success": False, "message": str(e)})
    finally:
        cursor.close()
        connection.close()

# Delete a site
@app.route("/delete_site/<site_id>", methods=["DELETE"])
def delete_site(site_id):
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        
        # Use backticks for column names
        query = "DELETE FROM `site` WHERE `Site ID` = %s"
        cursor.execute(query, (site_id,))
        connection.commit()

        if cursor.rowcount > 0:
            return jsonify({"success": True, "message": "Site deleted successfully."})
        else:
            return jsonify({"success": False, "message": "Site not found."})
    except Exception as e:
        return jsonify({"success": False, "message": str(e)})
    finally:
        cursor.close()
        connection.close()

# Route to handle customer update
@app.route('/submit_customer_update', methods=['POST'])
def submit_customer_update():
    try:
        # Get form data
        customer_id = request.form.get('customer_name')
        address = request.form.get('address')
        phone_no = request.form.get('phone_no')

        if not customer_id:
            return jsonify({"success": False, "message": "Customer ID is required."})

        # Initialize list to store the updates
        updates = []
        values = []

        # Only add fields if they are provided
        if address:
            updates.append("`Customer Address` = %s")
            values.append(address)
        if phone_no:
            updates.append("`Phone No` = %s")
            values.append(phone_no)

        # If no updates are provided, return an error
        if not updates:
            return jsonify({"success": False, "message": "At least one field should be provided to update."})

        # Add the customer_id to the end of values
        values.append(customer_id)

        # Create the SQL query dynamically based on provided fields
        query = f"""
            UPDATE `customer`
            SET {', '.join(updates)}
            WHERE `Cust ID` = %s
        """

        # Get database connection
        connection = get_db_connection()
        cursor = connection.cursor()

        # Execute the update query
        cursor.execute(query, tuple(values))
        connection.commit()

        # Check if the update was successful
        if cursor.rowcount > 0:
            return jsonify({"success": True, "message": "Customer updated successfully."})
        else:
            return jsonify({"success": False, "message": "No changes made or customer not found."})
    except Exception as e:
        return jsonify({"success": False, "message": str(e)})
    finally:
        # Close the cursor and connection
        cursor.close()
        connection.close()

# Route to handle customer deletion
@app.route("/delete_customer/<customer_id>", methods=["DELETE"])
def delete_customer(customer_id):
    try:
        connection = get_db_connection()
        cursor = connection.cursor()

        # Delete query with backticks for columns
        query = "DELETE FROM `customer` WHERE `Cust ID` = %s"
        cursor.execute(query, (customer_id,))
        connection.commit()

        if cursor.rowcount > 0:
            return jsonify({"success": True, "message": "Customer deleted successfully."})
        else:
            return jsonify({"success": False, "message": "Customer not found."})
    except Exception as e:
        return jsonify({"success": False, "message": str(e)})
    finally:
        cursor.close()
        connection.close()

@app.route('/get_customer_details/<customer_id>', methods=['GET'])
def get_customer_details(customer_id):
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
       
        query = """
        SELECT `Customer Address`, `Phone No`
        FROM `Customer`
        WHERE `Cust ID` = %s
        """
        cursor.execute(query, (customer_id,))
        customer = cursor.fetchone()

        if customer:
           
            return jsonify({"success": True, "customer": {
                "address": customer[0],
                "phone_no": customer[1]
            }})
        else:
            return jsonify({"success": False, "message": "Customer not found."})
    except mysql.connector.Error as e:
        return jsonify({"success": False, "message": f"Error fetching customer details: {e}"})
    finally:
        cursor.close()
        connection.close()

@app.route('/get_inventory_details/<item_id>', methods=['GET'])
def get_inventory_details(item_id):
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        query = """
        SELECT `Item Type`, `Item UOM`, `Item Avl Qty`, `Item ROR`, `Item Value`, `Item Rate`
        FROM `inventory`
        WHERE `Item ID` = %s
        """
        cursor.execute(query, (item_id,))
        item = cursor.fetchone()

        if item:
            return jsonify({
                "success": True,
                "inventory": {
                    "item_type": item[0],
                    "item_uom": item[1],
                    "item_avl_qty": item[2],
                    "item_ror": item[3],
                    "item_value": item[4],
                    "item_rate": item[5]
                }
            })
        else:
            return jsonify({"success": False, "message": "Item not found."})
    except mysql.connector.Error as e:
        return jsonify({"success": False, "message": f"Error fetching item details: {e}"})
    finally:
        cursor.close()
        connection.close()


@app.route('/get_site_details/<site_id>', methods=['GET'])
def get_site_details(site_id):
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        # Query to fetch site details (location, site owner name)
        query = """
        SELECT `Site Location`, `Site Owner Name`
        FROM `Site`
        WHERE `Site ID` = %s
        """
        cursor.execute(query, (site_id,))
        site = cursor.fetchone()

        if site:
            # Return site details as JSON
            return jsonify({"success": True, "site": {
                "location": site[0],
                "owner_name": site[1]
            }})
        else:
            return jsonify({"success": False, "message": "Site not found."})
    except mysql.connector.Error as e:
        return jsonify({"success": False, "message": f"Error fetching site details: {e}"})
    finally:
        cursor.close()
        connection.close()

@app.route('/get_user_details/<user_id>', methods=['GET'])
def get_user_details(user_id):
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        # Query to fetch user details (email, password, phone number, etc.)
        query = """
        SELECT `Email`, `Password`, `User Phone number`
        FROM `users`
        WHERE `User ID` = %s
        """
        cursor.execute(query, (user_id,))
        user = cursor.fetchone()

        if user:
            # Return user details as JSON
            return jsonify({
                "success": True,
                "user": {
                    "email": user[0],
                    "password": user[1],
                    "phone_no": user[2]
                }
            })
        else:
            return jsonify({"success": False, "message": "User not found."})
    except mysql.connector.Error as e:
        return jsonify({"success": False, "message": f"Error fetching user details: {e}"})
    finally:
        cursor.close()
        connection.close()
@app.route("/update_inventory_details", methods=["POST"])
def update_inventory_details():
    try:
        data = request.form
        item_id = data.get("item_type")  # Should be item_id, not item_type
        if not item_id:
            return jsonify({"success": False, "message": "Item ID is required for updating."})

        column_mapping = {
            "item_uom": "Item UOM",
            "item_desc": "Item Desc",
            "item_avl_qty": "Item Avl Qty",
            "item_ror": "Item ROR",
            "item_value": "Item Value",
            "item_rate": "Item Rate"
        }

        updates = []
        values = []

        for form_field, db_column in column_mapping.items():
            value = data.get(form_field)
            if value:
                updates.append(f"`{db_column}` = %s")
                values.append(value)

        if not updates:
            return jsonify({"success": True, "message": "No fields provided for update. Item is unchanged."})

        query = f"""
            UPDATE `inventory`
            SET {', '.join(updates)}
            WHERE `Item ID` = %s
        """
        values.append(item_id)  # Use Item ID as the identifier

        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute(query, tuple(values))
        connection.commit()

        # Always return a success message
        return jsonify({"success": True, "message": "Inventory updated successfully."})

    except Exception as e:
        return jsonify({"success": False, "message": str(e)})

    finally:
        if "cursor" in locals():
            cursor.close()
        if "connection" in locals():
            connection.close()



@app.route('/delete_item/<item_id>', methods=['DELETE'])
def delete_item(item_id):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    try:
        # Execute delete query using Item ID
        cursor.execute("DELETE FROM inventory WHERE `Item ID` = %s", (item_id,))
        connection.commit()

        if cursor.rowcount > 0:
            return jsonify({
                'success': True,
                'message': f'Item with ID "{item_id}" deleted successfully.'
            })
        else:
            return jsonify({
                'success': False,
                'message': f'Item with ID "{item_id}" not found.'
            }), 404
    except Exception as e:
        connection.rollback()
        return jsonify({
            'success': False,
            'message': str(e)
        }), 500
    finally:
        cursor.close()
        connection.close()

@app.route("/update_item_transaction_form", methods=["POST"])
def update_item_transaction_form():
    try:
        data = request.form
        item_id = data.get("item_type")  # Should be item_id, not item_name
        if not item_id:
            return jsonify({"success": False, "message": "Item ID is required for updating."})

        column_mapping = {
            "trans_qty": "Trans Qty",
            "trans_type": "Trans Type",
            "trans_date": "Trans Date",
            "user_id": "User ID",
            "usage": "Usage"
        }

        updates = []
        values = []

        for form_field, db_column in column_mapping.items():
            value = data.get(form_field)
            if value:
                updates.append(f"`{db_column}` = %s")
                values.append(value)

        if not updates:
            return jsonify({"success": True, "message": "No fields provided for update. Item is unchanged."})

        query = f"""
            UPDATE `invtrans`
            SET {', '.join(updates)}
            WHERE `Item ID` = %s
        """
        values.append(item_id)

        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute(query, tuple(values))
        connection.commit()

        return jsonify({"success": True, "message": "Item updated successfully."})

    except Exception as e:
        return jsonify({"success": False, "message": str(e)})

    finally:
        if "cursor" in locals():
            cursor.close()
        if "connection" in locals():
            connection.close()
            
#invtrns
@app.route('/delete_itemtrns/<item_id>', methods=['DELETE'])
def delete_itemtrns(item_id):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    try:
        cursor.execute("DELETE FROM invtrans WHERE `Item ID` = %s", (item_id,))
        connection.commit()

        return jsonify({
            'success': True,
            'message': f'Item with ID "{item_id}" deleted successfully.'
        })
    except Exception as e:
        connection.rollback()
        return jsonify({
            'success': False,
            'message': str(e)
        }), 500
    finally:
        cursor.close()
        connection.close()

@app.route("/get_item_details/<item_id>", methods=["GET"])
def get_item_details(item_id):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    try:
        cursor.execute("SELECT * FROM invtrans WHERE `Item ID` = %s", (item_id,))
        item = cursor.fetchone()

        if item:
            return jsonify({"success": True, "item": item})
        else:
            return jsonify({"success": False, "message": "Item not found."})

    except Exception as e:
        return jsonify({"success": False, "message": str(e)})

    finally:
        cursor.close()
        connection.close()


#############################################################################
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True, threaded=True)

