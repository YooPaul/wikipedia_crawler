import wikipedia
import requests
import json
import wptools
import pickle
import sys
import urllib.request as req
import urllib
def save_obj(obj, name ):
    with open('dict/'+ name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def load_obj(name ):
    with open('dict/' + name + '.pkl', 'rb') as f:
        return pickle.load(f)

WIKI_REQUEST = 'http://en.wikipedia.org/w/api.php?action=query&prop=pageimages&format=json&piprop=original&titles='

def get_wiki_image(search_term):
    try:
        #wkpage = wikipedia.page(search_term)
        title = search_term#wkpage.title
        response  = requests.get(WIKI_REQUEST+title)
        json_data = json.loads(response.text)
        #print(json_data)
        img_link = list(json_data['query']['pages'].values())[0]['original']['source']
        return img_link        
    except:
        return 0

#wiki_image = get_wiki_image('1880s')
#print(wiki_image)
if len(sys.argv) != 2:
  print("1 Argument required")
  exit()
page_name = sys.argv[1]
page = wikipedia.page(page_name, auto_suggest=False)#'1880s')
content = page.content
try:
  end_ind = content.index('== References ==')
except:
  end_ind = -1
if end_ind != -1:
  content = content[:end_ind]
links = page.links
print('Page title: ' + page.title)
#start_ind = content.index('== ' + sys.argv[2] + ' ==')#'== Politics ==')#'== People ==')
#end_ind = content.index('== ' + sys.argv[3] + ' ==')#'== References ==')
#content = content[start_ind:end_ind]
data = {}
TEMPLATE = "https://en.wikipedia.org/w/api.php?action=query&prop=templates&titles=%s&tllimit=500&format=json"
for link in links:
  if link not in content:
    continue
  print(link)
  #if not link.isascii():
  #  continue
  url = TEMPLATE % urllib.parse.quote(link.replace(' ', '_'))
  uf = req.urlopen(url)
  template = str(uf.read())
  if 'person' not in template and 'Person' not in template and 'Birth date' not in template:
    continue
  img = get_wiki_image(link)
  if img == 0:
    continue
    #print(link)
  p = wptools.page(link, silent=True).get_parse()#'Leopold II of Belgium').get_parse()
  infobox = p.data['infobox']
  data[link] = (img, infobox)
save_obj(data, sys.argv[1])
print(len(data))
    #print(str(infobox['birth_date']))
