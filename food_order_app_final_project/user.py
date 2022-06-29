class user:

    def __init__(self,user_id,user_name,user_contact,user_email,user_address,user_password):
        self.user_id = user_id
        self.user_name = user_name
        self.user_contact = user_contact
        self.user_email = user_email
        self.user_address = user_address
        self.user_password = user_password
        

    def __str__(self):
         return f"user_id: {self.user_id} \nuser_name : {self.user_name} \nuser_contact : {self.user_contact} \nuser_email : {self.user_email} \nuser_address : {self.user_address} \nuser_password : {self.user_password} \n"
   
    def set_user_id(self,user_id):
        self.user_id = user_id

    def get_user_id(self):
        return self.user_id

    def set_user_name(self,user_name):
        self.user_name = user_name

    def get_user_name(self):
        return self.user_name

    def set_user_contact(self,user_contact):
        self.user_contact = user_contact

    def get_user_contact(self):
        return self.user_contact

    def set_user_email(self,user_email):
        self.user_email = user_email

    def get_user_email(self):
        return self.user_email
    
    def set_user_address(self,user_address):
        self.user_address = user_address

    def get_user_address(self):
        return self.user_address

    def set_user_password(self,user_password):
        self.user_password = user_password

    def get_user_password(self):
        return self.user_password