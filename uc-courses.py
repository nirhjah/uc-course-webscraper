import requests
from bs4 import BeautifulSoup
  
URL = "https://www.canterbury.ac.nz/study/subjects/software-engineering/"
r = requests.get(URL)
  
soup = BeautifulSoup(r.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib

ex = soup.find('ul', attrs = {'id':'unique_2659__ul_04CB37EDBAE6463AB90DAC10466D8967'})

course_dict = {}
links = []


#def splitting coures adding to dictionary with link, return course code
def splitting_course(course):
    #course_dict = {}
    #links = []
    i = course.find('a')
    split_course = course.text.split()
    course_code = split_course[0] + "" + split_course[1]
    links.append(i.get('href'))
    course_dict[course_code] = i.get('href')
    return course_code





pick_year = input("Which year would you like to search for, 1st, 2nd, 3rd or 4th year: ")
if pick_year == "1st year":
    print("Available 1st Year Courses:")
    should_be = soup.find('div', attrs = {'id':'collapse3'})
    first_year = should_be.find_all('div', class_='section')[1]
    first_year_courses = first_year.find_all('li')
    for course in first_year_courses:
        i = course.find('a')

        split_course = course.text.split()
        course_code = split_course[0] + "" + split_course[1]
        print(course_code)
       # links.append(i.get('href'))
       # course_dict[course_code] = i.get('href')
elif pick_year == "2nd year":
    print("Available 2nd Year/1st Pro Software Engineering Courses:")
    should_be = soup.find('div', attrs = {'id':'collapse3'})
    section = should_be.find_all('div', class_='section')[2]
    all_years = section.find_all('ul')[1]
    second_year_options = section.find_all('ul')[2]
    second_year = all_years.find_all('li')

    for course in second_year:
        print(splitting_course(course))
        # i = course.find('a')

        # split_course = course.text.split()
        # course_code = split_course[0] + "" + split_course[1]
        # print(course_code)
        # links.append(i.get('href'))
        # course_dict[course_code] = i.get('href')

        #if more than one course in a line like math220 or emth210


    print("And one of the following: ")
    for course in second_year_options:
        print(splitting_course(course))








# print("Available 2nd Year/1st Pro Software Engineering Courses:")
# for course in ex:
#     i = course.find('a')
    
#    # print(i)
#     split_course = course.text.split()
#     course_code = split_course[0] + "" + split_course[1]
#     print(course_code)
#     links.append(i.get('href'))
#     course_dict[course_code] = i.get('href')
    
    
    # print(course.text, i.get('href')) #gets course name and link to the course
     # get course code    
    
while True:
    pick_course = input("\nWhich course would you like to view the prerequisites for? ") #or just view information
    if pick_course == 'quit':
        break
    elif pick_course not in course_dict:
        print("Course not valid!")
        
    else:
        course_url = course_dict[pick_course]  
        r = requests.get(course_url)
        soup2 = BeautifulSoup(r.content, 'html5lib')

        html_prereq_code = soup2.find(id='ctl00_ContentPlaceHolder1_PCRRepeater_ctl00_PCRDescriptionLabel') #2nd-4th years


        preq_list = html_prereq_code.find_all('a')
        for prereq in preq_list:
            prereq_course = prereq.text
            print(prereq_course)









#for line in prereqs_html:
    #print(line.find_all('a'))
    
  #  print(line)
 #  # print(i.get('href'))
    
    
   # spilt_prereq = line.text.split()
    #print(split_prereq)

    
    #prereq_course = line.text
    #print(prereq_course)
    




#<span id="ctl00_ContentPlaceHolder1_PCRRepeater_ctl00_PCRDescriptionLabel">(1) <a href="GetCourseDetails.aspx?course=COSC121&amp;year=2021">COSC121</a>; (2) <a href="GetCourseDetails.aspx?course=COSC122&amp;year=2021">COSC122</a>; RP: <a href="GetCourseDetails.aspx?course=MATH120&amp;year=2021">MATH120</a></span>


#course_url = "https://www.canterbury.ac.nz/study/subjects/software-engineering/"
      
#soup = BeautifulSoup(r.content, 'html5lib')    
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   # links.append(i.get('href'))
    



#print(links)    



   # links = []
   # for link in soup.findAll('a'):
    #    links.append(link.get('href'))

#print(ex.prettify())







#ex = soup.find_all(id="2nd–4th years")
#ex = soup.find_all(class_="sectiontitle")