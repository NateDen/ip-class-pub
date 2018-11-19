from flask import Flask, request, render_template, send_from_directory
from flask import redirect, url_for
import records
#import collections

app = Flask(__name__)
db = records.Database('postgresql://denpna01:@knuth.luther.edu/world')
continent_names = []  
country_names = []        
region_names = []        


#this function is for finding out the results and displaying it properly  
@app.route('/results',methods = ['POST'])
def get_info():
    
    identifier = request.form['identifier']
    user_value = request.form['selection']
    
    #for country    
    if identifier == 'country':
        rows = db.query("SELECT * FROM country WHERE name='" + user_value + "';")
        return render_template('country_results.html', list_of_countries = country_names, rows = rows)

    #for region
    if identifier == 'region':
        rows = db.query("SELECT * FROM country WHERE region='" + user_value + "';")        
        return render_template('region_results.html', list_of_regions = region_names, rows = rows)
        
    #for continent
    if identifier == 'continent':
        rows = db.query("SELECT * FROM country WHERE continent='" + user_value + "';")
        return render_template('continent_results.html', list_of_continents = continent_names, rows = rows)  
    
    return render_template('home.html')

@app.route('/query',methods = ['POST'])
#this function is for redirecting and then populating the drop down list in all pages
def redirect():
    user_value = request.form['choice']
    
    #for country    
    if user_value == 'country':
        if len(country_names) == 0:
            rows = db.query('SELECT * FROM country')        
            for country in rows:
                country_names.append(country.name)
            country_names.sort()            
        return render_template('country.html', list_of_countries = country_names)

    #for region
    if user_value == 'region':
        if len(region_names) == 0:
            rows = db.query('SELECT DISTINCT region FROM country')        
            for region in rows:
                region_names.append(region.region)
            region_names.sort()            
        return render_template('region.html', list_of_regions = region_names)

    #for continent
    if user_value == 'continent':
        if len(continent_names) == 0:
            rows = db.query('SELECT DISTINCT continent FROM country')        
            for continent in rows:
                continent_names.append(continent.continent)
            continent_names.sort()            
        return render_template('continent.html', list_of_continents = continent_names)    

@app.route('/')
def hello_world():    
    return render_template('home.html')

if __name__ == '__main__':
    app.debug = True
    debug = True
    app.run(debug = True)