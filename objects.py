'''
Initialization of student and queue objects

Author: Lucas Hyatt
'''

class Student:
	def __init__(self, fname, lname, uoID, email, phoneticSpelling, revealCode):
		self.fname = fname
		self.lname = lname
		self.uoID = uoID
		self.email = email
		self.phonetic = phoneticSpelling
		self.reveal = revealCode # Not entirely sure about this variable, just put it as boolean for now

	def printStudent(self):
		print("Student:", self.fname, self.lname, "has ID:", self.uoID)

# Testing

student1 = Student("Lucas", "Hyatt", 951550079, "llh@uoregon.edu", "loo-kiss", True)
student2 = Student("Maura", "McCabe", 111222333, "maura@uoregon.edu", "mor-uh", True)
student3 = Student("Noah", "Tigner", 123456789, "notig@uoregon.edu", "no-uh", False)
student4 = Student("Jimmy", "Lam", 987654321, "jim@uoregon.edu", "ji-mee", True)
student5 = Student("Yin", "Jin", 123789456, "yjin@uoregon.edu", "yi-n", False)
student6 = Student("Anthony", "Hornoff", 123456789, "noff@uoregon.edu", "hor-noff", True)

# student1.printStudent()
# student2.printStudent()
# student3.printStudent()
# student4.printStudent()
# student5.printStudent()

'''
Notes regarding input file (Source: https://classes.cs.uoregon.edu/20W/cis422/Handouts/Cold_Call_System_SRS_v2.pdf):

The UO ID will be nine digits.
The <reveal_code> will be used to indicate details about this entry, such as if the photo will be
displayed to other students in the classroom.
<LF> is a Unix line feed character.
The spaces around the <tab> and <LF> characters should not be added to the file. 

Line consists of:
<first_name> <tab> <last_name> <tab> <UO ID> <tab> <email_address> <tab> <phonetic_spelling> <tab> <reveal_code> <LF>
'''

class Queue: 
	def __init__(self):
		self.q = []

	#Pushes a new element to queue
	def enqueue(self, student):
		self.q.append(student)

	#Removes oldest element from queue, returns True upon success
	def dequeue(self):
		if len(self.q) != 0:
			self.q.pop(0)
			return True
		print("Cannot dequeue, queue is empty...")
		return False

	def printQ(self):
		if len(self.q) == 0:
			print("Nothing to print, queue is empty...")
		else:
			print("Length of queue is:", len(self.q))
			for i in range(len(self.q)):
				print("Queue at index", i, "has", end = " ")
				self.q[i].printStudent()


studentQ = Queue()

studentQ.enqueue(student1)
studentQ.enqueue(student2)
studentQ.enqueue(student3)
studentQ.enqueue(student4)
studentQ.enqueue(student5)
studentQ.enqueue(student6)

studentQ.printQ()

studentQ.dequeue()
studentQ.dequeue()
studentQ.dequeue()

studentQ.printQ()

studentQ.dequeue()
studentQ.printQ()
studentQ.dequeue()
studentQ.printQ()
studentQ.dequeue()
studentQ.printQ()
studentQ.dequeue()


'''
Sources used: 

https://classes.cs.uoregon.edu/20W/cis422/Handouts/Cold_Call_System_SRS_v2.pdf
https://www.geeksforgeeks.org/queue-in-python/
'''




