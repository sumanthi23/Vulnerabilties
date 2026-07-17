## SSRF
Defination:
This vulnerability allows an attacker to make server send requests to locations which are choosen
choosen by the attacker to expose internal systems or any sensitive data

SSRF is vulnerable because servers generally have a ability access some of the internall things to
access so with this vulnerbaility normal users can also access that sensitive data

Server-Side → the request is sent by the server.
Request → it's an HTTP (or sometimes other protocol) request.
Forgery → the attacker forges or manipulates where the server sends that request.

How is this done 
In a typical SSRF attack, an application fetches data from a back-end API based on a user-supplied
URL. If the application fails to validate this URL, an attacker can replace it with an internal
address such as http://localhost/admin. The server then makes the request on the attacker's behalf
because it trusts the supplied URL. If the internal service allows requests from localhost or lacks
proper authorization checks, sensitive information or administrative functionality may be exposed.
This is known as a Server-Side Request Forgery (SSRF) attack
Localhost is the more trusted weapon  to make ssrf more dangerous 

why applications trust requests from localhost
* many websites genrally have reverse proxy suppose if u ask something unintended then it gets
  blockked but with ssrf tht is bypassed
* when the credentials are lost to recover generally this is provided so the admin can recover
* sometimes admin interface is runned on other port and so he thinks safe but the server can access
  it whcih leads to ssrf

what actually is leading to the ssrf 
* Large applications use multiple servers but only the shopping website is exposed on the internet
  and this is connected to the other internal servers and which are nto directly accessed by the
  users so the developers think that as it is not accessible by the users directly so weaken the
  authentication and sensitive data leaved in this way as it leads ssrf


In this type of SSRF, the attacker makes the vulnerable server send requests to other internal back-end
systems instead of localhost. These systems usually have private IP addresses and are not directly accessible from the internet. Since developers often rely on the network for protection, these internal services may haveweaker security or no authentication. The vulnerable server can reach them, retrieve sensitive information, and return it to the attacker.
  
* 
