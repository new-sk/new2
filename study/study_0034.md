# 4. css

## 4.1 css

&lt;!DOCTYPE html&gt;

&lt;html&gt;

&lt;head&gt;

  &lt;meta charset="UTF-8"&gt;

  &lt;title&gt;CSS 연동 방법&lt;/title&gt;
  
  &lt;style&gt;                  &lt;!--  internal 방법:  head tag안에 정의  --&gt;

  h3 {color:red;}

  &lt;/style&gt;
  
  &lt;link rel="stylesheet" href="index.css"&gt;  &lt;!--  external 방법: head tag안에서 외부 CSS 파일 연결 --&gt;
  
&lt;/head&gt;

&lt;body&gt;

  &lt;h3&gt;Hello world&lt;/h3&gt;   &lt;!--  inline 방법:  각 태그에 style속성 정의 --&gt;

  &lt;h3 style="color:blue;"&gt;Hello world&lt;/h3&gt;   
  
&lt;/body&gt;

&lt;/html&gt;



<br>

## 4.2 실제 사항

<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>CSS 연동 방법</title>
  
  <style>                  <!--  internal 방법:  head tag안에 정의  -->
      h3 {color:red;}
  </style>
  
  <link rel="stylesheet" href="index.css">  <!--  external 방법: head tag안에서 외부 CSS 파일 연결 -->
  
</head>
<body>

  <h3>Hello world</h3>   <!--  inline 방법:  각 태그에 style속성 정의 -->
  <h3 style="color:blue;">Hello world</h3>   
  
</body>
</html>