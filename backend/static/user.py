

class User(UserMixin):
	"User class"
	def __init__(self, email, password, surname, given_name): 
		self._email = email.lower()
		self._password = password
		self._surname = surname.lower()
		self._given_name = given_name.lower()

	@property
	def email(self):
		return self._email
	
	@property
	def password(self):
		return self._password

	@property
	def surname(self):
		return self._surname
	
	@property
	def given_name(self):
		return self._given_name

	@property
	def fullname(self):
		return " ".join([self._given_name, self._surname])

	@email.setter
	def email(self, email):
		self._email = email.lower()

	@password.setter
	def password(self, pwd):
		self._password = pwd

	@surname.setter
	def surname(self, surname):
		self._surname = surname.lower()

	@given_name.setter
	def given_name(self, given_name):
		self._given_name = given_name.lower()

	
	def add_appointment(self, appt_obj):
		if not any(appointment.id == appt_obj.id for appointment in self._appointments):
			self._appointments.append(appt_obj)

	def remove_appointment_by_id(self, appt_id):
		for i, appt in enumerate(self._appointments):
			if appt.id == appt_id:
				del self._appointments[i]


	def get_past_appointments(self):
		return [x for x in self._appointments if x.past is True]

	def get_upcoming_appointments(self):
		return [x for x in self._appointments if x.past is False]
		
	def set_past_appointments(self):
		for a in self._appointments:
			s = " ".join([a.date, a.time_slot])
			d = datetime.strptime(s,"%Y-%m-%d %H:%M")
			if a.past is False and d < datetime.now():
				a.past = True

	def get_id(self):
		return self._email

	def get_information(self):
		return {
				'email': self._email,
				'password' : self._password,
				'surname': self._surname,
				'given_name': self._given_name,
				}