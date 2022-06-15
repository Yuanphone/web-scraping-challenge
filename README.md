# web-scraping-challenge
## Mission to Mars
In this challenge, we built a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page. 
### Part  1: Scraping
Complete the initial scraping using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.

Create a Jupyter Notebook file called mission_to_mars.ipynb. Use this file to complete all your scraping and analysis tasks. 

#### NASA Mars News

Scrape the Mars News Site and collect the latest News Title and Paragraph Text. Assign the text to variables that you can reference later.

#### JPL Mars Space Images—Featured Image

Visit the URL for the Featured Space Image site here.

Use Splinter to navigate the site and find the image URL for the current Featured Mars Image, then assign the URL string to a variable called featured_image_url.

Be sure to find the image URL to the full-sized .jpg image.

Be sure to save a complete URL string for this image.

### Mars Facts

Visit the Mars Facts webpage and use Pandas to scrape the table containing facts about the planet including diameter, mass, etc.

Use Pandas to convert the data to a HTML table string.

### Mars Hemispheres

Visit the astrogeology site to obtain high-resolution images for each hemisphere of Mars.

click each of the links to the hemispheres in order to find the image URL to the full-resolution image.

Save the image URL string for the full resolution hemisphere image and the hemisphere title containing the hemisphere name. Use a Python dictionary to store the data using the keys img_url and title.

Append the dictionary with the image URL string and the hemisphere title to a list. This list will contain one dictionary for each hemisphere.

### Part 2: MongoDB and Flask Application
Use MongoDB with Flask templating to create a new HTML page that displays all the information that was scraped from the URLs above.

Start by converting the Jupyter notebook into a Python script called scrape_mars.py by using a function called scrape. This function should  execute the scraping code from above and return one Python dictionary containing all the scraped data.

Next, create a route called /scrape that will importthe scrape_mars.py script and call the scrape function.

Store the return value in Mongo as a Python dictionary.

Create a root route / that will query the Mongo database and pass the Mars data into an HTML template for displaying the data.

Create a template HTML file called index.html that will take the Mars data dictionary and display all the data in the appropriate HTML elements. 
## screenshots for the Application
<img width="930" alt="html_screenshot1" src="https://user-images.githubusercontent.com/100816322/173713083-d3d381e5-90af-44e7-9fb2-fc557b68ad4f.PNG">
<img width="925" alt="html_screenshot2" src="https://user-images.githubusercontent.com/100816322/173713110-fdf188ca-ca5e-45c4-8742-668d4e43dbbd.PNG">
<img width="926" alt="html_screenshot3" src="https://user-images.githubusercontent.com/100816322/173713213-8d6b5ae6-ddbf-48bd-99f8-50af05226201.PNG">




