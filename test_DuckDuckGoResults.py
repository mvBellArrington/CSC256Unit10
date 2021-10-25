import requests
import pytest

url = 'https://api.duckduckgo.com/?q=presidents+of+the+united+states&format=json'
response = requests.get(url)
my_json = response.json()


lastName_of_presidents = ['Washington', 'Adams', 'Jefferson', 'Madison', 'Monroe', 'Adams', 'Jackson', 'Buren', 'Harrison', 'Tyler', 'Polk', 'Taylor', 'Fillmore', 'Pierce', 'Buchanan', 'Lincoln', 'Johnson', 'Grant', 'Hayes', 'Garfield', 'Arthur', 'Cleveland', 'Harrison', 'Cleveland', 'McKinley', 'Roosevelt', 'Taft', 'Wilson', 'Harding', 'Coolidge', 'Hoover', 'Roosevelt', 'Truman', 'Eisenhower', 'Kennedy', 'Johnson', 'Nixon', 'Ford', 'Carter', 'Reagan', 'Bush', 'Clinton', 'Bush', 'Obama', 'Trump', 'Biden']

# Test if all the presidents are in at least one DuckDuckGo result
def test_all_president_in_api_result(my_json, lastName_of_presidents):
	isIn = {}
	inResponse = False
	for president in lastName_of_presidents:
		for topic in my_json['RelatedTopics']:
			if president in topic['Text']:
				inResponse = True
		isIn[president] = inResponse
	print(isIn)
	
				



	 
			
		