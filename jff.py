from EducationYear import EducationYear
from Subject import Subject
from Crosssection import CrossSection
from Student import Student


class BRSPoints:
    def __init__(self, subject: Subject, year: EducationYear, cross_section: CrossSection, points: int):
        self.subject = subject
        self.year = year
        self.cross_section = cross_section
        self.points = points

    def __str__(self):
        template = 'Student: {} Subject: {} Year: {} Srez: {} Points: {}'
        return template.format(self.student.fio, self.subject.name, str(self.year.beginYear) + '-' + str(self.year.endYear),
                               self.cross_section.name, self.points)
