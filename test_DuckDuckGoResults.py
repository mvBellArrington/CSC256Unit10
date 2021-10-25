import requests
import pytest


lastName_of_presidents = ['Washington', 'Adams', 'Jefferson', 'Madison', 'Monroe', 'Adams', 'Jackson', 'Buren', 'Harrison', 'Tyler', 'Polk', 'Taylor', 'Fillmore', 'Pierce', 'Buchanan', 'Lincoln', 'Johnson', 'Grant', 'Hayes', 'Garfield', 'Arthur', 'Cleveland', 'Harrison', 'Cleveland', 'McKinley', 'Roosevelt', 'Taft', 'Wilson', 'Harding', 'Coolidge', 'Hoover', 'Roosevelt', 'Truman', 'Eisenhower', 'Kennedy', 'Johnson', 'Nixon', 'Ford', 'Carter', 'Reagan', 'Bush', 'Clinton', 'Bush', 'Obama', 'Trump', 'Biden']

# Test if all the presidents are in at least one DuckDuckGo result
@pytest.mark.parametrize("president", lastName_of_presidents)
def test_all_president_in_api_result(president):
	url = 'https://api.duckduckgo.com/?q=presidents+of+the+united+states&format=json'
	response = requests.get(url)
	my_json = response.json()
	for topic in my_json['RelatedTopics']:
		res = topic['Text'].split()
		if president in res[1]:
			return
		else:
			assert president not in res[1]


	 
			
		