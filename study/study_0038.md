# 8. CSS 주요속성

## 8.1 CSS 주요속성

&lt;!DOCTYPE html&gt;

&lt;html&gt;

&lt;head&gt;

  &lt;meta charset="UTF-8"&gt;

  &lt;title&gt;CSS 주요 속성&lt;/title&gt;
  
  &lt;style&gt;

  .paragraph {

  width: 500px;    &lt;!--  비율로도 지정 가능  100% --&gt;

  height: 500px;

  background: green;   &lt;!-- 배경관련 다른 것들도 한꺼번에 정의 가능 : yellow url no-repeat, left --&gt;

  font-size: 50px;

  font-family: Times, Arial, sans-serif;   &lt;!-- 브라우저에 따라 폰트 없을 수도 있음. 앞에 것 먼저 선택됨, 마지막은 보통 s폰트 --&gt;

  font-style: italic;

  border: 2pt solid red;        

  background: yellow url(elice_logo.png) no-repeat center;

  }

  &lt;/style&gt;
  
&lt;/head&gt;

&lt;body&gt;
  
  &lt;h1 class="paragraph"&gt;Nice to meet you&lt;/h1&gt;
  
&lt;/body&gt;

&lt;/html&gt;



<br>

## 8.2 실제 사항

<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>CSS 주요 속성</title>
  
  <style>
    .paragraph {
      width: 500px;    <!--  비율로도 지정 가능  100% -->
      height: 500px;
      background: green;   <!-- 배경관련 다른 것들도 한꺼번에 정의 가능 : yellow url no-repeat, left -->
      font-size: 50px;
      font-family: Times, Arial, sans-serif;   <!-- 브라우저에 따라 폰트 없을 수도 있음. 앞에 것 먼저 선택됨, 마지막은 보통 s폰트 -->
      font-style: italic;
    
      border: 2pt solid red;        
      background: yellow url(elice_logo.png) no-repeat center;
    }
  </style>
  
</head>
<body>
  
  <h1 class="paragraph">Nice to meet you</h1>
  
</body>
</html>