# 9. Transform

## A. 소스내역

&lt;!DOCTYPE html&gt;

&lt;html&gt;

&lt;head&gt;

  &lt;meta charset="UTF-8"&gt;

  &lt;title&gt;CSS Transform&lt;/title&gt;
  
  &lt;style&gt;                                      /* 3종 : transform,  transition,  animation */
  
    .transform {                               /* 브라우저 하위 호환성을 위한 prefix : 코드가 엄청 늘어남 */
       width: 100px;
       height: 100px;
       background-color: red;
       
       margin: 200px 0 0 200px;
       transform: rotate(45deg);                            /* 회전: 음수가능 */
       transform: scale(2,3);                                  /* 확대비율 */
       transform: translate(100px, 200px);                /* 이동 */
       transform: skew(10deg, 20deg)                     /* 입체적 각도, x축, y축 */
    }
  &lt;/style&gt;
  
&lt;/head&gt;

&lt;body&gt;

  &lt;div class="transform"&gt;&lt;/div&gt;                            /* 마진, 패딩으로 처리했던 것,  translate로 가능해짐 */

&lt;/body&gt;

&lt;/html&gt;                                                          



<br><br>

## B. 실제 사항

<!DOCTYPE html>
<html>
<head>

  <meta charset="UTF-8">
  <title>CSS Transform</title>
  
  <style>                                      /* 3종 : transform,  transition,  animation */
    .transform {                               /* 브라우저 하위 호환성을 위한 prefix : 코드가 엄청 늘어남 */
       width: 100px;
       height: 100px;
       background-color: red;
       
       margin: 200px 0 0 200px;
       transform: rotate(45deg);                            /* 회전: 음수가능 */
       transform: scale(2,3);                                  /* 확대비율 */
       transform: translate(100px, 200px);                /* 이동 */
       transform: skew(10deg, 20deg)                     /* 입체적 각도, x축, y축 */

    }
  </style>
  
</head>
<body>

  <div class="transform"></div>                            /* 마진, 패딩으로 처리했던 것,  translate로 가능해짐 */

</body>
</html>                                                          