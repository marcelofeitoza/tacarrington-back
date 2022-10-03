import bs4, requests, os

def downloadLatestDataset():
  baseUrl = "https://cdaweb.gsfc.nasa.gov/pub/data/wind/mfi/mfi_h2/2022/"
  soup = bs4.BeautifulSoup(requests.get(baseUrl).text, 'html.parser')
  links = []

  for link in soup.find_all('a'):
    if link.get('href').endswith('.cdf'):
      links.append(link.get('href'))

  # download the latest dataset
  latestDataset = links[-1]
  print("Downloading latest dataset: " + latestDataset)
  # show the progress bar
  r = requests.get(baseUrl + latestDataset, stream=True)
  
  # save the dataset as latest.cdf
  open('./data/latestDataset.cdf', 'wb').write(r.content)



def downloadAllDatasets():
  baseUrl = "https://cdaweb.gsfc.nasa.gov/pub/data/wind/mfi/mfi_h2/2022/" # 
  soup = bs4.BeautifulSoup(requests.get(baseUrl).text, 'html.parser')
  links = []

  for link in soup.find_all('a'):
    if link.get('href').endswith('.cdf'):
      links.append(link.get('href'))

  for dataset in links:
    # check if it's already downloaded
    if dataset in os.listdir('./datasets'):
      print("Dataset " + dataset + " already downloaded")
    else:
      print("Downloading dataset: " + dataset)
      r = requests.get(baseUrl + dataset, stream=True)
      open('./datasets/' + dataset, 'wb').write(r.content)