# 10. Transition

## A. 소스내역

&lt;!DOCTYPE html&gt;

&lt;html&gt;

&lt;head&gt;

  &lt;meta charset="UTF-8"&gt;

  &lt;title&gt;CSS Transtion&lt;/title&gt;
  
  &lt;style&gt;

    .transition {
        width: 100px;
        height: 100px;
        background-color: red;
        
        transition-property: width;               /* 변경되는 속성 */
        transition-duration: 2s;                   /* 변경되는데 소요되는 시간 */
        transition-timing-function: linear;      /* 변경 방식 설정 */
        transition-delay: 1s;                        /* 변경이 시작되는데 드는 delay */
        
        transition: width 0.1s linear 2s;      /* 하나로 작성 가능, 순서 상관없으나, duration이 먼저 */
    }
    
    .transition:hover {     /* 가상선택자 hover쓸대 띄워쓰기 조심, 마우스 위, 여러개 미리 지정되어 있음 */
        width: 300px;
    }

  &lt;/style&gt;
  
&lt;/head&gt;

&lt;body&gt;

  &lt;div class="transition"&gt;&lt;/div&gt;

&lt;/body&gt;

&lt;/html&gt;                                                    



<br><br>

## B. 실제 사항

<!DOCTYPE html>
<html>
<head>

  <meta charset="UTF-8">
  <title>CSS Transtion</title>
  
  <style>

    .transition {
        width: 100px;
        height: 100px;
        background-color: red;
        
        transition-property: width;               /* 변경되는 속성 */
        transition-duration: 2s;                   /* 변경되는데 소요되는 시간 */
        transition-timing-function: linear;      /* 변경 방식 설정 */
        transition-delay: 1s;                        /* 변경이 시작되는데 드는 delay */
        

        transition: width 0.1s linear 2s;      /* 하나로 작성 가능, 순서 상관없으나, duration이 먼저 */

    }
    
    .transition:hover {     /* 가상선택자 hover쓸대 띄워쓰기 조심, 마우스 위, 여러개 미리 지정되어 있음 */
        width: 300px;
    }

  </style>
  
</head>
<body>

  <div class="transition"></div>

</body>
</html>                                                  