import streamlit as st
import requests
import json
import pandas as pd
import matplotlib.pyplot as plt
import reverse_geocoder as rg

def reverseGeocode(coordinates):
    result = rg.search(coordinates)

    return result


class ImmoWeb:
    
    def __init__(self, country='BE', orderBy='relevance', page='1', immo_type='appartement', transaction_type='sale'):
        
        self.country = country
        self.orderBy = orderBy
        self.page = page
        self.immo_type = immo_type
        self.transaction_type = transaction_type



    def appartement(self):
        url = f"https://www.immoweb.be/en/search-results/apartment/for-{self.transaction_type}"

        querystring = {"countries":self.country,"hasRecommendationActivated":"true","page":self.page,"orderBy":self.orderBy,"searchType":"similar"}

        headers = {
          "authority": "www.immoweb.be",
          "accept": "application/json, text/plain, */*",
          "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
          "cookie": "__cf_bm=z1GTYl.UYRn1EeBp.kCTvP16aVhlPsqLx300ZmQ1Vd8-1654004679-0-ATbtS0HymxYwb2L9z4UZ9x0ZXhI9FRI63LiPA9gZmwwcQ+XcJk3JPVa2reFS6dmqXpPImNCg7FpgQwXHcOa5Wno=; XSRF-TOKEN=eyJpdiI6IjZNSnlLUTBkMm1wdEFqWnR4aXJXMUE9PSIsInZhbHVlIjoiNi9WWlJRM3dZL2ZTNndEcy96T3ZJQWRnbXRXMmFncmwwVlhrTXlsbSt3Njd3SGR2aE5nZURtbWRRU3A0SkszMEVrUEtMRTNrZ3NkcXd2aGZRUkUycFl4OVZMKy9uM3hQSHJLOHVyU3dEMWVGYXVsaVkrQVFpSFhyMzZ4aGNLc0ciLCJtYWMiOiJiZTEzMWE0NWRhMWI3Y2FjYzQyMjA2NzVmM2EyMTczYTJhYzllZWI0YTc4MjM0MDFkNDE2NjMyZjI4NDE3ZTEzIn0%3D; immoweb_session=eyJpdiI6ImRWSVZVL21reUtja3QreUZmY3BWbVE9PSIsInZhbHVlIjoic1hvQkE5a0dkNHFoaHY4ckNHSEJlak9PbGVNQlh6QjFqdjh3S2ZMNndiRWhDVkpJRGYxK2JDbEorWW1EbEdXN1N2KzZMdktSZkpSL21UQUNaMDJ3M2VDWU9wRnhxYTlPdzBwNHhUalEvWVkwRThWd01aRFV6c3lYdlM4Qm9qMVUiLCJtYWMiOiIyMDRhMWNkOWQ3OWQ4YzhmZmM5MzQ0YjI2NmVlNTdhZjU5YTI1MmUyODQzMjMyMGEzZDk2NGQwOTdiM2VlNTU1In0%3D; search_postal_code=eyJpdiI6IjNuR0t6UzR3MjZMc25BcmlzaFhPVnc9PSIsInZhbHVlIjoiZzlPNkw2Wi9HajQ1U1FsdlJ3UHUrTDVOYWg4OTI5dUJOeFo3b1BydU9RTHJranJIY21WbEEwY0QvN25SUTNUcCIsIm1hYyI6ImIxNmQ1MDU0NDYxYmEwNTEyZDJjZWYzYTA3OTQ2NGNhOTQ1MTA0MGYxOWM3MzJlYzA1YzMzNjQzMTVmMjBkNTIifQ%3D%3D; search_property_type=eyJpdiI6Im5lSHhrNUhnY3llS1RtZVdkdyt1Ymc9PSIsInZhbHVlIjoidDJ4YlhIalFVbXMwT2hGK3dnS0hOVWVIK1BFNWZiT2dTSUdmYVpxamhuOXdoM3ZLdExSUlZOQ2hQWHhlRjU4R3owR0tONDBQYml1U1Q1bzh0OTdhbmc9PSIsIm1hYyI6Ijc5OTU3MmIwMTkyNzUxZmUyYWM0MTA4NGY2ODg2NzQ5MmRlYmMxNzVhZTFhZWFkOGZmYzM1ZTFiNThlZTY5NDIifQ%3D%3D; search_transaction_type=eyJpdiI6ImZHbXRYSkdrQ25TWG9oWjduajZmNUE9PSIsInZhbHVlIjoia1RIcTlIVG55RE0zb1JHMjdQL3ZNQ0k5eVl3a1NlbXdZRkhyd3N5dWc4SlZ6d3g1K2czTFZlZEZ1ZGh1aFl6WDhya2R2OWVuVjhOQ0pCRERkbHhlcEE9PSIsIm1hYyI6IjhmZjY0NDAwOGYxNmMzOTFmMjg2ZjViZDYwYmIyOTVhZGRjYTg2Y2I3OWVmYTYzYjc5NzE3OTUxODdkZmZhNjYifQ%3D%3D; search_locality=eyJpdiI6IlREclplYzBQenRCZUtSVGlrTjRvRUE9PSIsInZhbHVlIjoiZGdwRm1Ycit2RjlqT1diT1RsekcvNDBJRkViZkFZUDFGUzQ4TC9HUHlSZmZrU0hqOGd6THY1WnloNFhBTVYxVSIsIm1hYyI6IjlkMDFjOWIzZmZkNGMwMmIzNmZkNWZjOWY3NWM5YjhlYjRlYmQ4Y2RhYTNhMmY5YjJlODgwMjNkMmZkNGZiODIifQ%3D%3D; search_province=eyJpdiI6Im41MlkwMS9qTnQvZFU1Um9NM1dBaUE9PSIsInZhbHVlIjoiemg1dnVLNUhucEdOMmtXOVpkNzJHejFOclNyVVNGN2JhZnFRZjBqMmJscGxnTlpJcXJTeHRJTDh1eHJoSVN5T0JPRmovbjFtMUhIb01ESEEvTmJEaVE9PSIsIm1hYyI6IjNlNzEyZjRjY2IxZjg1ZGFjNjZjNDM2YmFjOWI0MjFhOGYwOGQ2ZTVkYTA1MTAzZjhlODY5Y2UyODZhNWY5NTEifQ%3D%3D",
          "not-modify-cookies": "true",
          "referer": "https://www.immoweb.be/en/search/apartment/for-sale?countries=BE",
          "sec-fetch-dest": "empty",
          "sec-fetch-mode": "cors",
          "sec-fetch-site": "same-origin",
          "sec-gpc": "1",
          "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36",
          "x-xsrf-token": "eyJpdiI6IjZNSnlLUTBkMm1wdEFqWnR4aXJXMUE9PSIsInZhbHVlIjoiNi9WWlJRM3dZL2ZTNndEcy96T3ZJQWRnbXRXMmFncmwwVlhrTXlsbSt3Njd3SGR2aE5nZURtbWRRU3A0SkszMEVrUEtMRTNrZ3NkcXd2aGZRUkUycFl4OVZMKy9uM3hQSHJLOHVyU3dEMWVGYXVsaVkrQVFpSFhyMzZ4aGNLc0ciLCJtYWMiOiJiZTEzMWE0NWRhMWI3Y2FjYzQyMjA2NzVmM2EyMTczYTJhYzllZWI0YTc4MjM0MDFkNDE2NjMyZjI4NDE3ZTEzIn0="
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        data = response.json()
        results = []
        for i in data['results']:
            # Type (Appt or House)
            property_type = i['property']['type']
            # Location
            property_country = i['property']['location']['country']
            property_region = i['property']['location']['region']
            property_latitude = i['property']['location']['latitude']
            property_longitude = i['property']['location']['longitude']
            # Price
            property_price = i['price']['mainValue']
            # Surface
            property_land_surface = i['property']['landSurface']
            property_habitable_surface = i['property']['netHabitableSurface']
            # Bedrooms
            property_bedrooms = i['property']['bedroomCount']
            property_rooms_count = i['property']['roomCount']

            # Reverse geocoding
            property_geocoding = reverseGeocode((property_latitude, property_longitude)) 
            results.append({
                            'id': i['id'],
                            'property_type': property_type,
                            'property_country': property_country,
                            'property_region': property_region,
                            'property_price': property_price,
                            'property_land_surface': property_land_surface,
                            'property_habitable_surface': property_habitable_surface,
                            'property_bedrooms': property_bedrooms,
                            'property_rooms_count': property_rooms_count,
                            'property_latitude': property_latitude,
                            'property_longitude': property_longitude,
                            'GEO_city': property_geocoding[0]['name'],
                            'GEO_administration': property_geocoding[0]['admin1'],
                            'GEO_admin2': property_geocoding[0]['admin2']
                            })
        return results



st.title('ImmoWeb Properties')

input_pages = st.slider(label='pages to show', min_value=1, max_value=50, value=2, step=1)

bulk_data = []

for i in range(0, input_pages):
    bulk_data.append(ImmoWeb(country='BE', orderBy='relevance', page=i, immo_type='appartement', transaction_type='sale').appartement())
c_data = []
for i in bulk_data:
    for j in i:
        c_data.append(j)

df = pd.DataFrame(c_data)
df['property_sqm_price'] = df['property_price'] / df['property_habitable_surface']
st.dataframe(df)

st.markdown(input_pages)



