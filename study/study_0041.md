# 11. Animation changeWidth

## A. 소스내역

&lt;!DOCTYPE html&gt;

&lt;html&gt;

&lt;head&gt;

  &lt;meta charset="UTF-8"&gt;

  &lt;title&gt;CSS Animation&lt;/title&gt;
  
  &lt;style&gt;

    .animation {
        width: 300px;
        height: 300px;
        background-color: yellow;
        
        animation-name: changeWidth;
        animation-duration: 3s;                                /* 3개 항목은 Transition과 동일함 */
        animation-timing-function: linear;
        animation-delay: 1s;
        animation-iteration-count: 6;                    /* infinite 무한반복 */
        animation-direction: alternate;                  /* normal -&gt;,  reverse &lt;-,  alternate 왕복 */
    }
    
    @keyframes changeWidth {                        /* animation과 keyframes는 세트 */
        from {                                                /* from -&gt; to,  300에서 600으로 변화함 */
            width: 300px;                                   
        }
        to {
            width: 600px;
        }
    }

  &lt;/style&gt;
  
&lt;/head&gt;

&lt;body&gt;

  &lt;div class="animation"&gt;&lt;/div&gt;

&lt;/body&gt;

&lt;/html&gt;                                             



<br><br>

## B. 실제 사항

<!DOCTYPE html>
<html>
<head>

  <meta charset="UTF-8">
  <title>CSS Animation</title>
  
  <style>

    .animation {
        width: 300px;
        height: 300px;
        background-color: yellow;
        
        animation-name: changeWidth;
        animation-duration: 3s;                                /* 3개 항목은 Transition과 동일함 */
        animation-timing-function: linear;
        animation-delay: 1s;
        animation-iteration-count: 6;                    /* infinite 무한반복 */
        animation-direction: alternate;                  /* normal ->,  reverse <-,  alternate 왕복 */
    }
    
    @keyframes changeWidth {                        /* animation과 keyframes는 세트 */
        from {                                                /* from -> to,  300에서 600으로 변화함 */
            width: 300px;                                   
        }
        to {
            width: 600px;
        }
    }

  </style>
  
</head>
<body>

  <div class="animation"></div>

</body>
</html>        