import pdfkit

def getYear():
    return("""2023-2024""")

def getStudent():
    return ("""JW""")

def getCourses():
    return("""<li>English III</li>
      <li>Pre-Calculus</li>
      <li>Physics</li>
      <li>IB German A Lit HL Yr 1</li>
      <li>US Gov't/Econ</li>
      <li>TOK I</li>
      <li>Ceramics II</li>
      <li>Dig Photo I</li>
      <li>Fun Art</li>
      <li>Sculpture</li>""")


page = f"""
<html>
  <head>
    <style>
      body, p, ul, li {{
        font-family: "Calibri", Arial, sans-serif;
        font-size: 11pt;
        line-height: 1.5; /* Improve readability */
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
        padding-right: 70px;
        padding-left: 70px;      
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
    <h1 class="center bold padding-up">{getYear()} COURSE RECOMMENDATIONS</h1>
    <h2 class="left padding">Considerations as you review your course recommendations:</h2>
    <ul class="list-bullet padding">
      <li class="indent">Your teachers considered many factors when determining their recommendations for you. If you have any questions, talk to your current teacher in that department.</li>
      <li class="indent">Your recommended courses are subject to change if your academic work changes significantly.</li>
      <li class="indent">You do not need to be recommended for most elective courses, but some have prerequisites.</li>
    </ul>
    <h2 class="left padding">Considerations as you request courses:</h2>
    <ul class="list-bullet padding">
      <li class="indent">Consider your overall load, not just each individual course.</li>
      <li class="indent">Balance and perspective in your life is important, but also challenge yourself appropriately.</li>
      <li class="indent">Select coursework that engages you intellectually and meets your goals for college and beyond. Colleges expect you to challenge yourself while maintaining strong grades.</li>
      <li class="indent"><b>Consider the total number of Honors, AP, and IB courses you request.</b></li>
    </ul>
    <p class="left padding">(Requesting a course for which you were NOT recommended will trigger the relevant department to consider your request.)</p>
    <h3 class="center bold underline">Course Recommendations</h3>
    <h4 class="center underline bold">{getStudent()}</h4>
    <ul class="center list-no-style">
        {getCourses()}
    </ul>
    <p class="padding">I, _________________________________, confirm that I have reviewed my course recommendations for 2023-2024 and requested courses while considering all of the above information.</p>
    <p class="padding padding-down"><b>Student Signature: </b>_________________________________________</p>
    <p class="padding">I confirm that I have reviewed my child's course recommendations for 2023-2024 and I approve the courses requested while considering all of the above information.</p>
    <p class="padding padding-down"><b>Parent Signature: </b>______________________________________________</p>
    <p class="padding">I confirm that I have reviewed my advisee's course recommendations for 2023-2024 and I approve the courses requested while considering all of the above information.</p>
    <p class="padding padding-down"><b>Advisor Signature: </b>______________________________________________</p>
    <p class="padding">I confirm that I have reviewed my counselee's course recommendations for 2023-2024 and I approve the courses requested while considering all of the above information.</p>
    <p class="padding"><b>College Counselor Signature (for rising 12th grade only): </b>________________________________________</p>
  </body>
</html>
"""

pdfkit.from_string(page, 'output.pdf')

