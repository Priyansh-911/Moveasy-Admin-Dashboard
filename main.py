# import taipy
from taipy.gui import Gui
from app import itemsInStore
import pandas as pd


def read_df(data_path: str):
    df = pd.read_csv(data_path)
    return df


dataset1 = read_df("./Datasets/eb1fa0a4-e095-476b-af46-382094ddda53.csv")
dataset2 = read_df("./Datasets/e333a07c-9d92-4b9a-a856-9eb29055f772.csv")

listPoints = itemsInStore()
lats = []
longs = []

data = {"lat": [], "lon": []}

datas = []
key1 = 'lat'
key2 = 'lon'
for i in listPoints:
    # print("THIS is")
    # print(i["lats"], i["long"])
    lats.append(i["lats"])
    longs.append(i["long"])

    data.update({'lat': lats, 'lon': longs})
    datas.append(lats)
    datas.append(longs)

print(datas)

# print(listPoints)


marker = {"size": 10, "color": "red", "symbol": "triangle-se-open-dot"}
# layer = "india-political"

center={
  "latitude": 20.593684,
  "longitude": 78.962880
}
zoom=4
boundaries=[
  {
    "latitudes": [37.7749, 37.7590, 37.7909, 37.8120],
    "longitudes": [-122.4194, -122.4471, -122.3930, -122.3799]
  }
]



# data = {"lat": [20.7329684, 28.7519188], "lon" : [77.1189375, 77.11893711]}

layout = {
  "height": 1000,
  "width": 1000,
 "title": "Bus mappings", "showlegend": True,
          "geo": {"location": "INDIA", "countrycolor": "77d", "resolution": 50, "showland": True, "showocean": False,
                  "landcolor": "4a4", "oceancolor": "77d", "lataxis": {"range": [8, 37]},
                  "lonaxis": {"range": [68, 97]}}}

# properties = { "data": datas, "type": "scattergeo", "mode": "marker", "marker": marker, "layout": {"geo": {"scope": "india"}}}


line = {
    "width": 2,
    "color": "red"
}

section1 = """

#ADMIN Dashboard
##Mapping of all the buses available

<|{data}|chart|type=scattergeo|mode=markers|lat=lat|lon=lon|marker={marker}|center={center}|zoom={zoom}|boundaries={boundaries}|layout={layout}|>
<br>
</br>


##<u>Data of all the things related to Public Transportations </u>
---

<|layout|columns = 2 2 |

###<u> Data of bus stops available </u>
###<u> Data of Earning from Buses from 2015 - 2022 </u>

<|{dataset1}|table|width=99%|>

<|{dataset2}|table|width=99%|>
|>

"""

Gui(page=section1).run(dark_mode=False)
