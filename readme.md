    Zuaya


This is a REST API that allows users go get a list of cuisines in Zuaya restaurant, while also allowing to add a new cuisine, update an existing cuisine, and delete a cuisine

This app was implemented using django REST framework, qnd deployed on the following link: https://young-brushlands-41321.herokuapp.com/cuisines/

You can get a list of cuisines by issuing a GET request, add a new cuisine by issuing a POST request, with the details of the cuisine to be added, change an existing cuisine by issuing a PUT request, and finally deleting an exisiting cuisine by issuing a DELETE request. 

Most of the code was taken from the django REST framework tutorial the pycharm default django project and the Heroku example project, a new model and view for the cuisine was then added.