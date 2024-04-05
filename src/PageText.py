
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
  <body class="c19 doc-content">
    <p class="c15">
      <span class="c3">2024-2025 </span
      ><span class="c3">COURSE RECOMMENDATIONS</span>
    </p>
    <p class="c11 c18"><span class="c13"></span></p>
    <p class="c18">
      <span class="c10">Considerations as you </span
      ><span class="c3">review your course recommendations</span
      ><span class="c14 c10">:</span>
    </p>
    <ul class="c0 lst-kix_2a91me569hfb-0 start">
      <li class="c4 li-bullet-0">
        <span class="c7"
          >your teachers considered many factors when determining their
          recommendations for you and we encourage you to follow their
          recommendations. If you have any questions about your recommendation,
          we encourage you to talk to your current teacher in that
          department.</span
        >
      </li>
      <li class="c4 li-bullet-0">
        <span class="c16">your recommended courses are subject to cha</span
        ><span class="c16">nge </span
        ><span class="c9"
          >if your academic work for the last part of the school year changes
          significantly</span
        >
      </li>
      <li class="c4 li-bullet-0">
        <span class="c7"
          >you do not need to be recommended for most elective courses (but some
          have prerequisites)</span
        >
      </li>
    </ul>
    <p class="c18">
      <span class="c10">Considerations as you </span
      ><span class="c3">request courses</span><span class="c10 c14">:</span>
    </p>
    <ul class="c0 lst-kix_2a91me569hfb-0">
      <li class="c4 li-bullet-0">
        <span class="c7"
          >consider not just each individual course, but your overall load</span
        >
      </li>
      <li class="c4 li-bullet-0">
        <span class="c7"
          >try to have a sense of balance and perspective in your life, but also
          appropriately challenge yourself</span
        >
      </li>
      <li class="c4 li-bullet-0">
        <span class="c7"
          >select coursework that will engage you intellectually as well as
          position you to meet your goals for college matriculation and beyond.
          Typically, colleges are expecting that you have challenged yourself
          with the curriculum available to you while still maintaining strong
          grades.</span
        >
      </li>
      <li class="c4 li-bullet-0">
        <span class="c14 c8 c20"
          >seriously consider the total number of Honors, AP, and IB courses you
          request</span
        >
      </li>
    </ul>
    <p class="c17">
      <span class="c16"
        >(requesting a course for which you were NOT recommended will trigger
        the relevant department to consider your request)</span
      >
    </p>
    <p class="c6"><span class="c3 c5">Course Recommendations</span></p>
    <p class="c6 c11"><span class="c5 c3"></span></p>
    <p class="c6"><span class="c5 c3">Student x</span></p>
    <p class="c6"><span class="c7">English III</span></p>
    <p class="c6"><span class="c7">Pre-Calculus</span></p>
    <p class="c6"><span class="c7">Physics</span></p>
    <p class="c6"><span class="c7">IB German A Lit HL Yr 1</span></p>
    <p class="c6"><span class="c7">US Gov&#39;t/Econ</span></p>
    <p class="c6"><span class="c7">TOK I</span></p>
    <p class="c6"><span class="c7">Ceramics II</span></p>
    <p class="c6"><span class="c7">Dig Photo I</span></p>
    <p class="c6"><span class="c7">Fun Art</span></p>
    <p class="c6"><span class="c7">Sculpture</span></p>
    <p class="c1 c11"><span class="c7"></span></p>
    <p class="c1 c11"><span class="c14 c16 c21"></span></p>
    <p class="c1">
      <span class="c7"
        >I, _________________________________, confirm that I have reviewed my
        course recommendations for 2024-2025 and requested courses (on opposite
        side of this paper) while considering all of the above
        information.</span
      >
    </p>
    <p class="c1">
      <span class="c14 c8 c20"
        >Student Signature: _________________________________________</span
      >
    </p>
    <p class="c1 c11"><span class="c7"></span></p>
    <p class="c1">
      <span class="c7"
        >I confirm that I have reviewed my child&rsquo;s course recommendations
        for 2024-2025 and I approve the courses requested (on opposite side of
        this paper) while considering all of the above information.</span
      >
    </p>
    <p class="c1">
      <span class="c8">Parent Signature: </span
      ><span class="c7">_____________________________________________</span>
    </p>
    <p class="c1 c11"><span class="c7"></span></p>
    <p class="c1">
      <span class="c7"
        >I confirm that I have reviewed my advisee&rsquo;s/counselee&rsquo;s
        course recommendations for 2024-2025 and I approve the courses requested
        (on opposite side of this paper) while considering all of the above
        information.</span
      >
    </p>
    <p class="c1">
      <span class="c8">Advisor Signature:</span
      ><span class="c7"
        >&nbsp;_____________________________________________</span
      >
    </p>
    <p class="c1">
      <span class="c8">College Counselor Signature </span
      ><span class="c8 c12">(for rising 12th grade only)</span
      ><span class="c8">: </span
      ><span class="c7">______________________________________</span>
    </p>
    <p class="c1">
      <span class="c8">Notes from Advisor/College Counselor:</span
      ><span class="c7"
        >&nbsp;_________________________________________________________________</span
      >
    </p>
    <p class="c1">
      <span class="c7"
        >_________________________________________________________________________________________________</span
      >
    </p>
    <p class="c1">
      <span class="c7"
        >_________________________________________________________________________________________________</span
      >
    </p>
    <p class="c1">
      <span class="c16"
        >_________________________________________________________________________________________________</span
      >
    </p>
  </body>
</html>
""")