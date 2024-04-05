
def formatCourses(courses):
    list_items = ''.join(f' <p class="c6"><span class="c7">{course}</span></p>\n' for course in courses if course == course and course != "nan")
    return list_items

def getPageText(name, courses, year): 
    return (f"""
<html>
  <head>
    <style>
            /* latin */
      @font-face {{
        font-family: 'Calibri';
        font-style: normal;
        font-weight: 400;
        src: url(https://fonts.gstatic.com/l/font?kit=J7afnpV-BGlaFfdAhLEY6w&skey=a1029226f80653a8&v=v15) format('woff2');
        unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304, U+0308, U+0329, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;
      }}
      /* latin */
      @font-face {{
        font-family: 'Calibri';
        font-style: normal;
        font-weight: 700;
        src: url(https://fonts.gstatic.com/l/font?kit=J7aanpV-BGlaFfdAjAo9_pxqHw&skey=cd2dd6afe6bf0eb2&v=v15) format('woff2');
        unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304, U+0308, U+0329, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;
      }}
ul.lst-kix_2a91me569hfb-2 {{
    list-style-type: none;
  }}
  ul.lst-kix_o088gqhwfpjj-7 {{
    list-style-type: none;
  }}
  ul.lst-kix_oploub2xta1h-8 {{
    list-style-type: none;
  }}
  ul.lst-kix_2a91me569hfb-3 {{
    list-style-type: none;
  }}
  ul.lst-kix_o088gqhwfpjj-8 {{
    list-style-type: none;
  }}
  ul.lst-kix_oploub2xta1h-7 {{
    list-style-type: none;
  }}
  ul.lst-kix_2a91me569hfb-4 {{
    list-style-type: none;
  }}
  ul.lst-kix_o088gqhwfpjj-5 {{
    list-style-type: none;
  }}
  ul.lst-kix_oploub2xta1h-6 {{
    list-style-type: none;
  }}
  ul.lst-kix_2a91me569hfb-5 {{
    list-style-type: none;
  }}
  ul.lst-kix_o088gqhwfpjj-6 {{
    list-style-type: none;
  }}
  ul.lst-kix_2a91me569hfb-0 {{
    list-style-type: none;
  }}
  ul.lst-kix_2a91me569hfb-1 {{
    list-style-type: none;
  }}
  ul.lst-kix_o088gqhwfpjj-0 {{
    list-style-type: none;
  }}
  ul.lst-kix_o088gqhwfpjj-3 {{
    list-style-type: none;
  }}
  ul.lst-kix_o088gqhwfpjj-4 {{
    list-style-type: none;
  }}
  ul.lst-kix_o088gqhwfpjj-1 {{
    list-style-type: none;
  }}
  ul.lst-kix_o088gqhwfpjj-2 {{
    list-style-type: none;
  }}
  .lst-kix_o088gqhwfpjj-7 > li:before {{
    content: "\0025c6   ";
  }}
  .lst-kix_o088gqhwfpjj-6 > li:before {{
    content: "\0025cb   ";
  }}
  .lst-kix_o088gqhwfpjj-8 > li:before {{
    content: "\0025cf   ";
  }}
  ul.lst-kix_2a91me569hfb-6 {{
    list-style-type: none;
  }}
  ul.lst-kix_2a91me569hfb-7 {{
    list-style-type: none;
  }}
  ul.lst-kix_2a91me569hfb-8 {{
    list-style-type: none;
  }}
  .lst-kix_q4urlw6sdrnh-0 > li:before {{
    content: "\0025cf   ";
  }}
  .lst-kix_q4urlw6sdrnh-1 > li:before {{
    content: "\0025cf   ";
  }}
  .lst-kix_q4urlw6sdrnh-2 > li:before {{
    content: "\0025cf   ";
  }}
  .lst-kix_q4urlw6sdrnh-4 > li:before {{
    content: "\0025cf   ";
  }}
  .lst-kix_oploub2xta1h-6 > li:before {{
    content: "\0025cb   ";
  }}
  .lst-kix_q4urlw6sdrnh-3 > li:before {{
    content: "\0025cf   ";
  }}
  .lst-kix_oploub2xta1h-7 > li:before {{
    content: "\0025c6   ";
  }}
  ul.lst-kix_oploub2xta1h-1 {{
    list-style-type: none;
  }}
  ul.lst-kix_oploub2xta1h-0 {{
    list-style-type: none;
  }}
  .lst-kix_2a91me569hfb-5 > li:before {{
    content: "\0025cf   ";
  }}
  .lst-kix_q4urlw6sdrnh-6 > li:before {{
    content: "\0025cf   ";
  }}
  .lst-kix_oploub2xta1h-8 > li:before {{
    content: "\0025cf   ";
  }}
  ul.lst-kix_oploub2xta1h-5 {{
    list-style-type: none;
  }}
  ul.lst-kix_oploub2xta1h-4 {{
    list-style-type: none;
  }}
  .lst-kix_2a91me569hfb-6 > li:before {{
    content: "\0025cb   ";
  }}
  .lst-kix_2a91me569hfb-7 > li:before {{
    content: "\0025c6   ";
  }}
  ul.lst-kix_oploub2xta1h-3 {{
    list-style-type: none;
  }}
  .lst-kix_q4urlw6sdrnh-5 > li:before {{
    content: "\0025cf   ";
  }}
  ul.lst-kix_oploub2xta1h-2 {{
    list-style-type: none;
  }}
  .lst-kix_2a91me569hfb-8 > li:before {{
    content: "\0025cf   ";
  }}
  .lst-kix_q4urlw6sdrnh-7 > li:before {{
    content: "\0025cf   ";
  }}
  .lst-kix_2a91me569hfb-4 > li:before {{
    content: "\0025c6   ";
  }}
  .lst-kix_q4urlw6sdrnh-8 > li:before {{
    content: "\0025cf   ";
  }}
  .lst-kix_2a91me569hfb-2 > li:before {{
    content: "\0025cf   ";
  }}
  .lst-kix_2a91me569hfb-3 > li:before {{
    content: "\0025cb   ";
  }}
  ul.lst-kix_q4urlw6sdrnh-0 {{
    list-style-type: none;
  }}
  .lst-kix_oploub2xta1h-5 > li:before {{
    content: "\0025cf   ";
  }}
  ul.lst-kix_q4urlw6sdrnh-2 {{
    list-style-type: none;
  }}
  ul.lst-kix_q4urlw6sdrnh-1 {{
    list-style-type: none;
  }}
  .lst-kix_2a91me569hfb-0 > li:before {{
    content: "\002794   ";
  }}
  .lst-kix_2a91me569hfb-1 > li:before {{
    content: "\0025c6   ";
  }}
  ul.lst-kix_q4urlw6sdrnh-4 {{
    list-style-type: none;
  }}
  ul.lst-kix_q4urlw6sdrnh-3 {{
    list-style-type: none;
  }}
  .lst-kix_oploub2xta1h-4 > li:before {{
    content: "\0025c6   ";
  }}
  ul.lst-kix_q4urlw6sdrnh-6 {{
    list-style-type: none;
  }}
  ul.lst-kix_q4urlw6sdrnh-5 {{
    list-style-type: none;
  }}
  ul.lst-kix_q4urlw6sdrnh-8 {{
    list-style-type: none;
  }}
  ul.lst-kix_q4urlw6sdrnh-7 {{
    list-style-type: none;
  }}
  .lst-kix_oploub2xta1h-3 > li:before {{
    content: "\0025cb   ";
  }}
  .lst-kix_oploub2xta1h-0 > li:before {{
    content: "\002794   ";
  }}
  .lst-kix_oploub2xta1h-2 > li:before {{
    content: "\0025cf   ";
  }}
  .lst-kix_oploub2xta1h-1 > li:before {{
    content: "\0025c6   ";
  }}
  .lst-kix_o088gqhwfpjj-3 > li:before {{
    content: "\0025cb   ";
  }}
  .lst-kix_o088gqhwfpjj-4 > li:before {{
    content: "\0025c6   ";
  }}
  .lst-kix_o088gqhwfpjj-5 > li:before {{
    content: "\0025cf   ";
  }}
  .lst-kix_o088gqhwfpjj-1 > li:before {{
    content: "\0025c6   ";
  }}
  .lst-kix_o088gqhwfpjj-2 > li:before {{
    content: "\0025cf   ";
  }}
  li.li-bullet-0:before {{
    margin-left: -18pt;
    white-space: nowrap;
    display: inline-block;
    min-width: 18pt;
  }}
  .lst-kix_o088gqhwfpjj-0 > li:before {{
    content: "\002794   ";
  }}
  ol {{
    margin: 0;
    padding: 0;
  }}
  table td,
  table th {{
    padding: 0;
  }}
  .c4 {{
    margin-left: 36pt;
    padding-top: 0pt;
    padding-left: 0pt;
    padding-bottom: 0pt;
    line-height: 1.15;
    orphans: 2;
    widows: 2;
    text-align: left;
  }}
  .c7 {{
    color: #000000;
    font-weight: 400;
    text-decoration: none;
    vertical-align: baseline;
    font-size: 11pt;
    font-family: "Calibri";
    font-style: normal;
  }}
  .c17 {{
    margin-left: 36pt;
    padding-top: 0pt;
    padding-bottom: 0pt;
    line-height: 1.15;
    orphans: 2;
    widows: 2;
    text-align: left;
  }}
  .c2 {{
    color: #000000;
    font-weight: 700;
    text-decoration: none;
    vertical-align: baseline;
    font-size: 14pt;
    font-family: "Calibri";
    font-style: normal;
  }}
  .c13 {{
    color: #000000;
    font-weight: 400;
    text-decoration: none;
    vertical-align: baseline;
    font-size: 11pt;
    font-family: "Arial";
    font-style: normal;
  }}
  .c5 {{
    -webkit-text-decoration-skip: none;
    color: #000000;
    text-decoration: underline;
    vertical-align: baseline;
    text-decoration-skip-ink: none;
    font-style: normal;
  }}
  .c18 {{
    padding-top: 0pt;
    padding-bottom: 0pt;
    line-height: 1.15;
    orphans: 2;
    widows: 2;
    text-align: left;
  }}
  .c6 {{
    padding-top: 0pt;
    padding-bottom: 0pt;
    line-height: 1;
    orphans: 2;
    widows: 2;
    text-align: center;
  }}
  .c1 {{
    padding-top: 0pt;
    padding-bottom: 0pt;
    line-height: 1;
    orphans: 2;
    widows: 2;
    text-align: left;
  }}
  .c15 {{
    padding-top: 0pt;
    padding-bottom: 0pt;
    line-height: 1.15;
    orphans: 2;
    widows: 2;
    text-align: center;
  }}
  .c14 {{
    color: #000000;
    text-decoration: none;
    vertical-align: baseline;
    font-style: normal;
  }}
  .c19 {{
    background-color: #ffffff;
    max-width: 540pt;
    padding: 36pt 36pt 36pt 36pt;
  }}
  .c3 {{
    font-size: 14pt;
    font-family: "Calibri";
    font-weight: 700;
  }}
  .c9 {{
    background-color: #ffffff;
    font-family: "Calibri";
    font-weight: 400;
  }}
  .c10 {{
    font-size: 14pt;
    font-family: "Calibri";
    font-weight: 400;
  }}
  .c0 {{
    padding: 0;
    margin: 0;
  }}
  .c8 {{
    font-weight: 700;
    font-family: "Calibri";
  }}
  .c16 {{
    font-weight: 400;
    font-family: "Calibri";
  }}
  .c21 {{
    font-size: 8pt;
  }}
  .c12 {{
    font-style: italic;
  }}
  .c11 {{
    height: 11pt;
  }}
  .c20 {{
    font-size: 11pt;
  }}
  .title {{
    padding-top: 0pt;
    color: #000000;
    font-size: 26pt;
    padding-bottom: 3pt;
    font-family: "Arial";
    line-height: 1.15;
    page-break-after: avoid;
    orphans: 2;
    widows: 2;
    text-align: left;
  }}
  .subtitle {{
    padding-top: 0pt;
    color: #666666;
    font-size: 15pt;
    padding-bottom: 16pt;
    font-family: "Arial";
    line-height: 1.15;
    page-break-after: avoid;
    orphans: 2;
    widows: 2;
    text-align: left;
  }}
  li {{
    color: #000000;
    font-size: 11pt;
    font-family: "Arial";
  }}
  p {{
    margin: 0;
    color: #000000;
    font-size: 11pt;
    font-family: "Arial";
  }}
  h1 {{
    padding-top: 20pt;
    color: #000000;
    font-size: 20pt;
    padding-bottom: 6pt;
    font-family: "Arial";
    line-height: 1.15;
    page-break-after: avoid;
    orphans: 2;
    widows: 2;
    text-align: left;
  }}
  h2 {{
    padding-top: 18pt;
    color: #000000;
    font-size: 16pt;
    padding-bottom: 6pt;
    font-family: "Arial";
    line-height: 1.15;
    page-break-after: avoid;
    orphans: 2;
    widows: 2;
    text-align: left;
  }}
  h3 {{
    padding-top: 16pt;
    color: #434343;
    font-size: 14pt;
    padding-bottom: 4pt;
    font-family: "Arial";
    line-height: 1.15;
    page-break-after: avoid;
    orphans: 2;
    widows: 2;
    text-align: left;
  }}
  h4 {{
    padding-top: 14pt;
    color: #666666;
    font-size: 12pt;
    padding-bottom: 4pt;
    font-family: "Arial";
    line-height: 1.15;
    page-break-after: avoid;
    orphans: 2;
    widows: 2;
    text-align: left;
  }}
  h5 {{
    padding-top: 12pt;
    color: #666666;
    font-size: 11pt;
    padding-bottom: 4pt;
    font-family: "Arial";
    line-height: 1.15;
    page-break-after: avoid;
    orphans: 2;
    widows: 2;
    text-align: left;
  }}
  h6 {{
    padding-top: 12pt;
    color: #666666;
    font-size: 11pt;
    padding-bottom: 4pt;
    font-family: "Arial";
    line-height: 1.15;
    page-break-after: avoid;
    font-style: italic;
    orphans: 2;
    widows: 2;
    text-align: left;
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
    <ul class="center list-no-style">
    <p class="c6"><span class="c3 c5">Course Recommendations</span></p>
    <p class="c6 c11"><span class="c5 c3"></span></p>
    <p class="c6"><span class="c5 c3"> {name} </span></p>
        {formatCourses(courses)}
    </ul>
    <p class="c1 c11"><span class="c7"></span></p>
    <p class="c1 c11"><span class="c14 c16 c21"></span></p>
    <p class="c1">
      <span class="c7"
        >I, _________________________________, confirm that I have reviewed my
        course recommendations for {year} and requested courses (on opposite
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
        for {year} and I approve the courses requested (on opposite side of
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
        course recommendations for {year} and I approve the courses requested
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
        >&nbsp;________________________________________________________________</span
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