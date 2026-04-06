https://github.com/DataTalksClub/machine-learning-zoomcamp/tree/master/05-deployment

Note - content is outdated as statedd in the git. The recommendation is to watch the content still and then follow a workshop accessible here: 

https://github.com/DataTalksClub/machine-learning-zoomcamp/tree/master/05-deployment/workshop

# Module 5 - Deployment

## Summary

- The learning module has been much more fragmented and required to look at two different parts
- Anyways, I have learnt about docker fundamentals and have a basic idea of how to create my own docker image and start off the container
- The main idea behind docker is to create almost a virtual machine that help easily to share working code with all the environments etc required to run it. Great for transportability.
- In the meantime, also leaern more about package managers
    - For PyPI specific, uv is a great option. 
    - Conda and PyPI are kind of two different app stores, where PyPI is python specific
    - Python wheels - kind of ziped files, some of them alraedy compiled and suitable for my machine; compiled files are much faster to install because you don't need to comile
- Docker combined with uv makes it easy to run the code that someone else has done or to share my own code. Also quite light weight solution.
- FastAPI introduction was great - now I get much better how the internet works in general with IPs, ports, UTPs etc and that communication is happening based on HTTP protocol and that most of the time I will use GET request and sometimes POST. 
    - GET is only for getting content
    - POST is for sending data and getting back something
    - Got a glance at RESTful API principles: essentially urls are nouns and http methods are verbs.
