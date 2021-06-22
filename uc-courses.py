import requests
from bs4 import BeautifulSoup
  
URL = "https://www.canterbury.ac.nz/study/subjects/software-engineering/"
r = requests.get(URL)
  
soup = BeautifulSoup(r.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib
#print(soup.prettify())

ex = soup.find('ul', attrs = {'id':'unique_2659__ul_04CB37EDBAE6463AB90DAC10466D8967'})


course_dict = {}

links = []

print("Available 2nd Year/1st Pro Software Engineering Courses:")
for course in ex:
    i = course.find('a')
    
   # print(i)
    split_course = course.text.split()
    course_code = split_course[0] + "" + split_course[1]
    print(course_code)
    links.append(i.get('href'))
    course_dict[course_code] = i.get('href')
    
    
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

        html_prereq_code = soup2.find(id='ctl00_ContentPlaceHolder1_PCRRepeater_ctl00_PCRDescriptionLabel')


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