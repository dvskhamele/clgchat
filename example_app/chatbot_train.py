from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os




def setup():
    chatbot = ChatBot('Bot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    trainer='chatterbot.trainers.ListTrainer')
    #for file in os.listdir('C:/Users/aman/chatbot/english/'):
     #convData = open(r'C:/Users/aman/chatbot/english/' + file,encoding='latin-1').readlines()
    #chatbot.set_trainer(ListTrainer)
    #chatbot.train(convData)
    #print("Training completed")
    
    return chatbot

def trainit(bot1):

    
 
      bot1.train([
"""When library open?""",
"""it opens at 8am and closes at 5pm""""",
])
 
      bot1.train([
"""how sign up the football club?""",
"""You can contact for football club in sports department.
""",
])


 
      bot1.train([
"""When do the mid-terms start?""",
""" it will start in 1.5 to 2 month from start of the sem. """,
])


 
      bot1.train([
"""What is the four-year graduation rate""",
"""Four-Year Graduation Rate: 35 percent for public universities and 53 percent for private non-profit universities,
and Six-Year Graduation Rate: 59 percent for public universities and 65 percent for private non-profit universities""",
])

 
      bot1.train([
"""educational affiiation you hold?""",
"""SVITS is approved by AICTE and Govt. of Madhya Pradesh and is affiliated to Rajiv Gandhi Proudyogiki Vishwavidyalaya (RGPV), Bhopal for engineering courses and to Devi Ahilya Vishwavidyalaya (DAVV), Indore for MBA.""""",
])


 
      bot1.train([
"""""What kind of financial aid assistance do you offer to qualified students?  Do you offer any institutional scholarships or grants?""""",
"""The State Government has started a fee waiver scheme to help the economically poor but meritorious students. Further information regarding this can be obtained from the office of the Registrar. The M.p. Department of Education (ED) offers a variety of federal grants to students attending four-year colleges or universities, community colleges, and career schools. """,
])  

      bot1.train([
"""How do I get a federal grant?"""
"""The State Government has started a fee waiver scheme to help the economically poor but meritorious students. Further information regarding this can be obtained from the office of the Registrar. Almost all of our grants are awarded to students with financial need.  If you are interested in our grants, or in any federal student aid, you have to start by submitting a Free Application for M.p Scholorship form. You have to fill out the Scholorship form every year.  Once you’ve done that, you will get schlorship for your studies."""

])


      bot1.train([
"""What ar deadlines for submitting applications""",
""" The dead line of submitting form will be DECEMBER- JANUARY """,
])
 
      bot1.train([
"""What is the collage's loan default rate?""",
""" Basically the intrest rate for education lone is 11% in many but its depend on banks so you can ask there for this.""",
])


 
      bot1.train([
"""Do you have a preferred list of lenders that you work with?""",
"""Yup! we have two lenders which is Maharastra bank, and State bank of India. """,
])


 
      bot1.train([
"""How much is tuition? """,
"""for Bachelor of Technology [B.Tech] for 4 year(s) program the tution fee will be 2,60,000,
and for Master of Technology [M.Tech] for  2 year(s) program the tution fee will be 1,10,000,
and for Master of Business Administration [MBA] for 2 year(s)  program the tution fee will be 1,10,000,
and for Master of Computer Application [MCA] for  3 year(s)  program the tution fee will be 1,20,000. """,
]) 

      bot1.train([
"""What is fee""",
"""for Bachelor of Technology [B.Tech] for 4 year(s) program the tution fee will be 2,60,000,
and for Master of Technology [M.Tech] for  2 year(s) program the tution fee will be 1,10,000,
and for Master of Business Administration [MBA] for 2 year(s)  program the tution fee will be 1,10,000,
and for Master of Computer Application [MCA] for  3 year(s)  program the tution fee will be 1,20,000. """,
]) 

      bot1.train([
"""fee of BE""",
"""for Bachelor of Technology [B.Tech] for 4 year(s) program the tution fee will be 2,60,000,
""",
]) 

      bot1.train([
"""beCHLORE of engineering fees""",
"""for Bachelor of Technology [B.Tech] for 4 year(s) program the tution fee will be 2,60,000,
""",
]) 
      bot1.train([
"""BE fees""",
"""for Bachelor of Technology [B.Tech] for 4 year(s) program the tution fee will be 2,60,000,
""",
]) 


 
      bot1.train([
"""What, if anything, is included in my tuition? Books? Software?""",
"""Yes you can issue the books form library and can use the softwares of your department freely """,
])

      bot1.train([
"""Do you charge additional tuition or fees for out-of-state students?""",
""" No, We do not have charge any additional fee on student which are out of states.""",
])



      bot1.train([
"""Are there any additional fees like a technology fee or library fee that I need to know about?""",
""" No, You do not have to pay any additional fee for library or technology lab everthing is alread included in tution fee. 
""",
]) 


      bot1.train([
"""What methods of payment do you accept for tuition?""",
""" We basically accept this methods of payment---1) Net Banking, 2) DD(Demand Draft), 3)CASH, 4)CHEQUE""",
])



      bot1.train([
"""Do you offer payment plans""",
"""We basically accept this methods of payment---1) Net Banking, 2) DD(Demand Draft), 3)CASH, 4)CHEQUE""", 
])



      bot1.train([
"""What is the six-year grad rate""",
"""The 6-year graduation rate (150 percent graduation rate) for first-time, full-time undergraduate students who began seeking a bachelor’s degree at a 4-year degree-granting institution in fall 2010 was 60 percent. That is, by 2016 some 60 percent of students had completed a bachelor’s degree at the same institution where they started in 2010. The 6-year graduation rate was 59 percent at public institutions, 66 percent at private nonprofit institutions, and 26 percent at private for-profit institutions. The 6-year graduation rate was 63 percent for females and 57 percent for males; it was higher for females than for males at both public (62 vs. 56 percent) and private nonprofit (68 vs. 63 percent) institutions. However, at private for-profit institutions, males had a higher 6-year graduation rate than females (28 vs. 23 percent). """,
]) 


      bot1.train([
"""What kind of academic services, such as academic advising, tutoring, or career services are available to me?""",

"""We have a placement and career department cell which conduct the session for advising and train for your career. 
""",
])


      bot1.train([
"""Do instructors have experience teaching online?""",
"""Yes we have a trained instructor which have more then 5 years of experience.""",
])



      bot1.train([
"""What kind of response time can I expect if I have a question or problem? 24 hours""",
""" you can ask me any question 24/7. """,
])



      bot1.train([
"""What methods of contact  """,
"""E-mail-- preetjain23@gmail.com""",
])

      bot1.train([
"""contact of depratment """,
"""E-mail-- preetjain23@gmail.com""",
])



      bot1.train([
"""about college""",
"""Sports complex for Indoor games of 10000 sq.ft
It is known for some of the highest placements among all engineering colleges in MP
It is best known by its MOTORSPORT endeavor combined with the technical enthusiasts of the college.""",
])



      bot1.train([
"""What is the average length of time it takes for a student to complete this program?""",
""" The average length of time to completing this programme is 4 year.""",
])



      bot1.train([
"""""Approximately how much time, per week, will I need to devote to one class?""""",
"""You have to give atleast 6hr to one class per week
""""",
])



      bot1.train([
"""about SVITS""",
"""Shri Vaishnav Institute of Technology and Science is approved by AICTE and Govt. of Madhya Pradesh and is affiliated Rajiv Gandhi Proudyogiki Vishwavidyalaya, Bhopal and Devi Ahilya Vishwavidyalaya, Indore for MBA. SVITS is imparting quality education to the students and thus shaping their future. SVITS is an ISO 9001:2008 certified institute (Yr. 2002) and NBA accredited (departments CS, EC & TX) in the Yr. 2006 are the jewels of the SVITS crown.""""",
])


      bot1.train([
"""Foundation Programs""",
"""All the disciplines are fully supported by Physics, Chemistry, Mathematics, and Professional Development. Emphasis on strong fundamentals in pure sciences as well as communication skills is an integral part of the Programs design that is developed in close coordination with the industry, keeping the requirements of the future in mind.

The Science programmes will offer basic and advanced Programs of an inter-disciplinary nature. The advanced Programs will be in cutting-edge areas of nano-science and materials, bio-science communication networks including optical fiber and wireless communication, and compound semiconductors.

""""",
])

      bot1.train([
"""Programs in Wavelets, Optimization Techniques, Advanced Simulation and Reliability will also be offered as electives.""",
"""Engineers are expected to interact with their own professional community as well as with people from allied fields. The Professional Development programmes supplement engineering education with knowledge of social sciences and the inculcation of good communication skills so as to make them more enterprising and competitively oriented to succeed in the outside world.

In all the undergraduate engineering programmes, industrial training (Practice School) is made compulsory to combine the philosophy of working while learning.""""",
])

      bot1.train([
"""B.Tech + MBA (5 Years) Integrated Dual Degree Programme""",
"""The programme covers topics from engineering and technology along with management related topics. Students, apart from their core area of engineering, will be getting knowledge of Marketing, General Management, Research Methodology, Finance, Human Resources, Production, International Business, Operations and Information Technology.

2""""",

])
 


      bot1.train([
"""B.Tech + M.Tech (5 Years) Integrated Dual Degree Programme""",
"""The programme covers basic and advance level Programs of Engineering and Technology in the area of Computer Science Engineering and Electronics & Communication Engineering.""""",
])



      bot1.train([
"""Post Graduate Programmes""",
"""Besides undergraduate programmes, the Institute also offers M.Tech (Post Graduate Programme) and Ph.D. in Engineering. M.Tech programmes are of two years duration and provide core Programs, elective Programs and intensive project work (dissertation) in the respective area of specialization.

The objective of M.Tech programme is to impart advanced level knowledge in the field of specialization making the students suited to better academia as well as industry and assume responsibilities requiring greater research, design and development aptitude.

Through core Programs, the students will acquire advanced knowledge in a chosen field of specialization. The elective Programs will provide them an opportunity to further specialize in the field depending on their interest and future career plans.

For dissertation work, students will be required to take up problems on a particular topic in the field of focus of their study and work. They will be required to submit a dissertation report at the end of the project work compiling their study, findings and contributions. M.Tech dissertation work usually enables students to publish their results.

Project work prepares the student to take up challenging research and development tasks. Regular seminars will also be an integral part of the M.Tech curriculum, wherein students will collect material on specific topics and give presentations.

""""",
])



      bot1.train([
"""M. Tech - Computer Science Engineering""",
"""The programme provides advanced level education in the areas, such as Algorithms, Data Structures, Software Engineering, Learning Sciences & Technology, High Performance Computer Architecture, Advanced Computer Networking, Complexities & Coding Theories, Information Security, Internet & Web Technologies, Computer Graphics, Image Processing, Information Systems, Data Warehousing & Mining, Data Base Management, Advanced Operating Systems, Computational Models, Cognitive Science, Soft Computing, and Human Computer Interaction.""""",
])



      bot1.train([
"""M. Tech - Electronics & Communication Engineering""",
"""The programme covers a number of areas at advanced level, such as Mobile, Wireless, Satellite and Optical Communication and Computer Communication Systems & Networks, Signal Spread Spectrum Communication, Error Control Coding Techniques, Microelectronics, VLSI Design, and Information & Communication Theory through suitable core and elective Programs and extensive project and dissertation work.""""",
])


      bot1.train([
"""Doctoral Programme (Ph. D)""",
"""The Ph.D. programme is available in various specializations, such as Electronics & Communication Engineering, Computer Science Engineering, Information Technology, Electrical Engineering, Civil Engineering, Mechanical Engineering, Chemical Engineering, Engineering Physics, Engineering Chemistry, and Engineering Mathematics. The scholars are required to take up intensive research work under the guidance of a supervisor on a specific problem for a minimum of two years in this programme.""""",
]) 

      bot1.train([
"The research work is expected to result in new findings, contributing to knowledge in the chosen field.""",
"""The doctoral research programme gives an opportunity to students to demonstrate their analytical, innovative and independent thinking, leading to the enhancement of creativity and application of knowledge. The scholars are required to deliver seminars on their research progress regularly and publish their work in refereed journals. Finally, they are required to submit the thesis embodying their research findings for the award of the Ph.D. degree. They will also be required to take some advanced level Programs work.""""",
])


      bot1.train([
"""Financial Assistance""",
"""A limited number of Teaching Assistantships are available to candidates with a high GATE score at the commencement of the M.Tech programme. Partial financial support, in the form of Teaching Assistantships, is available for the M.Tech students during their second year also, which will be based on their academic performance. Financial support is available for Ph.D. students in the form of Research Assistantships.""""",
])


      bot1.train([
"""Evaluation Procedure""",
"""The Institute will follow the continuous evaluation approach at par with leading institutes in the country. Multiple inputs will be obtained for evaluation of student performance through session assignments, quizzes, weekly tests, minor and major tests at the middle and end of each semester, and a holistic view is taken of all these inputs for awarding the final Grade. A dynamic system of weightages for the various academic components, such as project activity, presentations, group behavior, and leadership qualities has been put in place.

Credit based academic programmes, with modular structure offer flexibility to progress at one's own pace. A minimum level of performance is necessary for satisfactory progress

""""",
])
 

      bot1.train([
"""Guest Lectures & Seminars""",
"""Eminent professionals from the country and abroad drawn from academic institutions, research laboratories and industry are invited for delivering lectures and seminars and for interaction with the Institute's fraternity.

""""",
])


      bot1.train([
"""The Curriculum""",
"""The curriculum is updated to integrate changes that are taking place in the environment. The curriculum consists of core and elective Programs

The core Programs package provides students with the foundation of the engineering discipline.

Elective Programs , on the other hand, are offered with an option to specialize in a specific area of interest.

The Institute presently offers specialization in Chemical Engineering, Civil Engineering, Computer Science Engineering, Electrical Engineering, Electronics & Communication Engineering, Information Technology, and Mechanical Engineering.

USEFUL LINKS""""",])


 
      bot1.train([
"""oh thats great""",
"thankyou :)""",
])
      return bot1