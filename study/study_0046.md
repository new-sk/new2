# 14. 뷰포트

## A. 소스내역

&lt;!DOCTYPE html&gt;

&lt;html&gt;

&lt;head&gt;

  &lt;meta charset="UTF-8"&gt;

  &lt;meta name="viewport" content="width=device-width, initial-scale=1.0"&gt;
  
  &lt;title&gt;미디어쿼리&lt;/title&gt;
  
  &lt;style&gt;

    .media {
      width: 500px;
      height: 500px;
      background-color: yellow;
      
      border: solid 10px red;
    }

  @media (min-width: 320px) and (max-width: 800px) {

      .media {
        width: 300px;
        height: 300px;
        
        border: none;    /* 상속 안 받을래요 */
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
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  
  <title>미디어쿼리</title>
  
  <style>
    .media {
      width: 500px;
      height: 500px;
      background-color: yellow;
      
      border: solid 10px red;
    }

  @media (min-width: 320px) and (max-width: 800px) {
      .media {
        width: 300px;
        height: 300px;
        
        border: none;    /* 상속 안 받을래요 */
      }
  }
  </style>
  
</head>
<body>

  <div class="media"></div>

</body>
</html>


