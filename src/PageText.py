
def formatCourses(courses):
    list_items = ''.join(f'<li>{course}</li>\n' for course in courses if course == course and course != "nan")
    return list_items

def getPageText(name, courses, year): 
    return (f"""
<html>
  <head>
    <style>
      body, p, ul, li {{
        font-family: "Calibri", Arial, sans-serif;
        font-size: 11pt;
        line-height: 1.15; /* Improve readability */
        word-wrap: break-word;
        background-color: white;
      }}
      h1 {{
        font-size: 20pt;
        margin-bottom: 0.5em; /* Space below headings */
      }}
      h2 {{
        font-size: 16pt;
        margin-bottom: 0.4em;
      }}
      h3 {{
        font-size: 14pt;
        margin-bottom: 0.3em;
      }}
      h4 {{
        font-size: 12pt;
        margin-bottom: 0.3em;
      }}
      b {{
        font-weight: bold;
        
      }}
      .bold {{
        font-weight: bold;
      }}
      .underline {{
        text-decoration: underline;
      }}
      .center {{
        text-align: center;
      }}
      .left {{
        text-align: left;
      }}
      .padding{{
        padding-right: 35px;
        padding-left: 35px;      
     }}
     .padding-up{{
        padding-top: 30px;
     }}
      .padding-down{{
        padding-bottom: 10px;
     }}
      .indent {{
          margin-left: 40px;     
    }}

      .list-bullet {{
        list-style-type: square;
        text-wrap: wrap;
        margin: 4;
      }}
      .list-no-style {{
        list-style-type: none;
        padding-left: 4;
      }}

    </style>
  </head>
  <body>
    <h1 class="center bold padding-up">{year} COURSE RECOMMENDATIONS</h1>
    <h2 class="left padding">Considerations as you review your course recommendations:</h2>
    <ul class="list-bullet padding">
      <li class="indent">your teachers considered many factors when determining their
          recommendations for you and we encourage you to follow their
          recommendations. If you have any questions about your recommendation,
          we encourage you to talk to your current teacher in that
          department.</li>
      <li class="indent">Your recommended courses are subject to change if your academic work for the last part of the school year changes
          significantly</li>
      <li class="indent">You do not need to be recommended for most elective courses (but some have prerequisites)</li>
    </ul>
    <h2 class="left padding">Considerations as you request courses:</h2>
    <ul class="list-bullet padding">
      <li class="indent">consider not just each individual course, but your overall load</li>
      <li class="indent">try to have a sense of balance and perspective in your life, but also
          appropriately challenge yourself</li>
      <li class="indent">select coursework that will engage you intellectually as well as
          position you to meet your goals for college matriculation and beyond.
          Typically, colleges are expecting that you have challenged yourself
          with the curriculum available to you while still maintaining strong
          grades.</li>
      <li class="indent"><b>seriously consider the total number of Honors, AP, and IB courses you
          request</b></li>
    </ul>
    <p class="left padding">(requesting a course for which you were NOT recommended will trigger
        the relevant department to consider your request)</p>
    <h3 class="center bold underline">Course Recommendations</h3>
    <h4 class="center underline bold">{name}</h4>
    <ul class="center list-no-style">
        {formatCourses(courses)}
    </ul>
    <p class="padding">I, _________________________________, confirm that I have reviewed my
        course recommendations for {year} and requested courses (on opposite
        side of this paper) while considering all of the above
        information.</p>
    <p class="padding padding-down"><b>Student Signature: </b>_________________________________________</p>
    <p class="padding">I confirm that I have reviewed my child&rsquo;s course recommendations
        for {year} and I approve the courses requested (on opposite side of
        this paper) while considering all of the above information.</p>
    <p class="padding padding-down"><b>Parent Signature: </b>______________________________________________</p>
    <p class="padding">I confirm that I have reviewed my advisee's course recommendations for {year} and I approve the courses requested while considering all of the above information.</p>
    <p class="padding padding-down"><b>Advisor Signature: </b>______________________________________________</p>
    <p class="padding">I confirm that I have reviewed my advisee&rsquo;s/counselee&rsquo;s
        course recommendations for {year} and I approve the courses requested
        (on opposite side of this paper) while considering all of the above
        information.</p>
    <p class="padding"><b>College Counselor Signature (for rising 12th grade only): </b>_________________________________________</p>
    <p class="padding">___________________________________________________________________________________________________________________</p>
    <p class="padding">___________________________________________________________________________________________________________________</p>
    <p class="padding">___________________________________________________________________________________________________________________</p>
    <p class="padding">___________________________________________________________________________________________________________________</p>
  </body>
</html>
""")

