'''
Description
'''
import math
from datetime import time

class Course():
	def __init__(self, title, duration, frequency, proffessor, level, importanceIndex = 0, maxStudents, numEnrolled = 0):
		self.title = title
		self.duration = duration
		self.frequency = frequency
		self.proffessor = proffessor
		self.level = level #3 = 300 level course
		self.importanceIndex = importanceIndex #geometric mean of weights given by students
		self.maxStudents = maxStudents
		self.numEnrolled = numEnrolled #actual number of students enrolled
		self.notAvailableAt = []

	#Formulae for importanceIndex: sum / sqrt(numEnrolled)
	def incrementImportanceIndex(self, weight):
		self.importanceIndex += weight / math.sqrt(numEnrolled)

	#Is given a list of the tuples>>
	#Example(lst = [('M', 08:00:00(time object))])
	def excludeFollowingTimes(self, listOfNotAvailable):
		self.notAvailableAt += listOfNotAvailable

