# 12. Animation rotation

## A. 소스내역

&lt;!DOCTYPE html&gt;

&lt;html&gt;

&lt;head&gt;

  &lt;meta charset="UTF-8"&gt;

  &lt;title&gt;CSS Transform, Animation&lt;/title&gt;
  
  &lt;style&gt;

    .box1 {
        width: 300px;
        height: 300px;
        background-color: red;
        
        animation: rotation 1500ms linear infinite alternate;    /* animation정의 */
    }

    @keyframes rotation {                             /* keyframes 매핑 :  from - to */
        from {
            transform: rotate(-10deg);
        }
        
        to {
            transform: rotate(10deg);
        }
    }

  &lt;/style&gt;
  
&lt;/head&gt;

&lt;body&gt;

  &lt;div class="box1"&gt;&lt;/div&gt;

&lt;/body&gt;

&lt;/html&gt;                                           



<br><br>

## B. 실제 사항

<!DOCTYPE html>
<html>
<head>

  <meta charset="UTF-8">
  <title>CSS Transform, Animation</title>
  
  <style>

    .box1 {
        width: 300px;
        height: 300px;
        background-color: red;
        
        animation: rotation 1500ms linear infinite alternate;    /* animation정의 */
    }

    @keyframes rotation {                             /* keyframes 매핑 :  from - to */
        from {
            transform: rotate(-10deg);
        }
        
        to {
            transform: rotate(10deg);
        }
    }

  </style>
  
</head>
<body>

  <div class="box1"></div>

</body>
</html>