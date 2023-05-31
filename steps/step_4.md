# Step 4:

Previously we discuss setting up the `application` and the `HTML`, here w will discuss the `jinga` technique to set up `.css`, `.js` and other files with `.html`


Replace all `.css`, `.js` and other file location like this command billow

```commandline
"{% static 'js/jquery.min.js' %}"
```

```commandline
"{% static '/css/style.css' %}"
```

Before replacing that make sure in the `static` folder you have created the necessary sub folder 

In this case `css` and `js` are the sub folders


### Your project is ready... Run the server and enjoy 

### Happy learning

### To know more about [Django](https://www.djangoproject.com/) Click [Here](https://www.djangoproject.com/)
### To know more about [APPARKY](https://apparky-soumenmtec-gmailcom.vercel.app/) Clink [Here](https://apparky-soumenmtec-gmailcom.vercel.app/)