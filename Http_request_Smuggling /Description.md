HTTP/1.0 --> This suppose when you are having a website and it has30 images then for loading each image 
this would send a request to the server this makes user performance very less and takes time 

HTTP/1.1 --> Here connection is opened and sends requests and everything is done then it closes it  

Frontend Server                                    Backend Server 
- This helps in using the website that when        - This handles the logic and the data
  the users open it this sends html,css              checks the login,store data , reads databases and
  javascript,images and fonts                        processes payments 
ex: ngnix,apache,vercel,netify                      ex: node.js,java,php

###What is HTTP request smuggling 
This occurs when frontend server and backend server disagree about the http request ends and next one begins and this confusion leads to the hide a second request inside the first one 

* This confusion occurs to determine where exactly does the request body ends HTTP/1.1 provides
  2 common ways to do that
  - Content length
   ```
   POST /login HTTP/1.1
      Host: example.com
      Content-Length: 10
        abcdefghij
   ```
   The server reads exactly 10 bytes
  - Transfer Encoding Chunked
    ```
      POST /login HTTP/1.1
      Host: example.com
      Transfer-Encoding: chunked
      5
      hello
      0
    ```
  The server reads the data in chunks and stops when it sees the 0

  Until this is fine but the request has the both content length and the transfer encoding then the
  frontend trusts the content length and then the backend trusts the transfer encoding . They interpret
  the same bytes differently

  So the data disintercept adds the extra data to the next request

  HTTP request smuggling may lead to the attacks like
  Bypassing security controls
  Accessing restricted pages
  Stealing other users' responses (response queue poisoning)
  Cache poisoning
  Session hijacking
  Web cache deception
  Cross-user attacks

  * request is passed through the multiple servers and then the server may interpt the sHTTP request differently
    * Content length is specified because it must know where the request need to end or else it may
      interpret the next request as also data so it must know where exactly does that end
  HTTP/2 --> This is safe from http request smuggling
There are 2 types of http/2 requests
--> HTTP/2 end to end
- THis is safe fromm smuggling here browser sends it goes to frontend server and then backend server
  no protocol conversion happens here
  http/2 uses the binary frames which has the id and lengths no chnace of http smuggling
--> HTTP/2 downgrading
  - here frontend servers support http/2 and then backend support the http/1
  - The frontend recieves the http/2 and then converts into the http/1.1 before forwadind this refered
    as downgrading and then this is also risky once if the countent length is misconfigured then this
    again leads to the smuggling
    
  
