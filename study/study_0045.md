# 13. 미디어쿼리

## A. 소스내역

&lt;!DOCTYPE html&gt;

&lt;html&gt;

&lt;head&gt;

  &lt;meta charset="UTF-8"&gt;

  &lt;title&gt;미디어쿼리 기초&lt;/title&gt;
  
  &lt;style&gt;
  
    .media {
        width: 500px;
        height: 500px;
        background-color: red;
    }
    
    @media (min-width: 320px) and (max-width: 800px) {      /* 미디어쿼리 : 사이즈 지정 */
        .media {                                                             /* 반응형 : 자연스럽게,  적응형 : 뚝뚝 끊기면서 */
        width: 300px;                                                       /* 크롬 개발자도구 기기 */
        height: 300px;
        background-color: yellow;                                       /* 지정하지 않은 속성은 바깥쪽 미디어 속성을 따라감 */
        
        border: blue solid 10px;
        }
    }
  
  &lt;/style&gt;
  
&lt;/head&gt;

&lt;body&gt;

  &lt;div class="media"&gt;&lt;/div&gt;

&lt;/body&gt;

&lt;/html&gt;



<br><br>

## B. 실제 사항

<!DOCTYPE html>
<html>
<head>

  <meta charset="UTF-8">
  <title>미디어쿼리 기초</title>
  
  <style>
  
    .media {
        width: 500px;
        height: 500px;
        background-color: red;
    }
    


    @media (min-width: 320px) and (max-width: 800px) {      /* 미디어쿼리 : 사이즈 지정 */
        .media {                                                             /* 반응형 : 자연스럽게,  적응형 : 뚝뚝 끊기면서 */
        width: 300px;                                                       /* 크롬 개발자도구 기기 */
        height: 300px;
        background-color: yellow;                                       /* 지정하지 않은 속성은 바깥쪽 미디어 속성을 따라감 */
        
        border: blue solid 10px;
        }
    }
  
  </style>
  
</head>
<body>

  <div class="media"></div>

</body>
</html>
