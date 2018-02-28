'''
Description
'''
import math
from datetime import time

class Course():
	def __init__(self, ID, courseNumber, title, duration, frequency, proffessor, level, numEnrolled):
		
		self.ID = ID
		self.courseNumber = courseNumber
		self.title = title
		self.duration = duration
		self.frequency = frequency
		self.proffessor = proffessor
		self.level = level #3 = 300 level course
		self.importanceIndex = 0 #geometric mean of weights given by students
		self.numEnrolled = numEnrolled #actual number of students enrolled
		self.finalSchedule = [] #list of tuples. Eg:[("M", 8), ("F, 8")]
		self.timeConflictDict = {}
		self.notAvailableAt = []

	#Increases the weight associated with each key
	#key = courseNumber, value = weight(initially 0)
	def addNewConflict(self, nextCourseNumber, coeff = 1):
		try:
			self.timeConflictDict[nextCourseNumber] += coeff
		except:
			self.timeConflictDict[nextCourseNumber] = 1

	def getFrequency(self):
		return self.frequency

	def getProffessor(self):
		return self.proffessor
	
	def getTimeConflictDict(self):
		return self.timeConflictDict

	#Returns course number
	def getCourseNumber(self):
		return self.courseNumber

	#Returns level of the course
	def getLevel(self):
		return self.level

	#Returns importance index
	def getImportanceIndex(self):
		return self.importanceIndex

	#Returns the title of the course
	def getTitle(self):
		return self.title

	def getSchedule(self):
		return self.finalSchedule

	def getNotAvailableAtList(self):
		return self.notAvailableAt

	#Formulae for importanceIndex: sum / sqrt(numEnrolled)
	def incrementImportanceIndex(self, weight):
		self.importanceIndex += weight / math.sqrt(self.numEnrolled)

	def setSchedule(self, schedule):
		self.finalSchedule = schedule

	def addNewDateInSchedule(self, newDate):
		self.finalSchedule.append(newDate)

	def addNotAvailableTime(self, newDate):
		self.notAvailableAt.append(newDate)


